from model.ponto import Ponto
from model.funcionarios import Funcionarios
from controller.controller_funcionarios import Constroller_Funcionario
from conexion.oracle_queries import OracleQueries
from datetime import date
from datetime import datetime
import pandas as pd

class Controller_Ponto:
    def __init__(self):
        self.ctrl_funcionario = Constroller_Funcionario()

    def inserir_data_hora(self) -> Ponto:
        oracle = OracleQueries()
        responder_novamente = 's'

        while(responder_novamente.lower() == 's'):
            self.listar_funcionarios(oracle, need_connect=True)
            cpf = str(input("Digite o CPF do funcionario: "))
            funcionarios = self.valida_funcionario(oracle, cpf)
            if funcionarios == None:
                return None

            "data_hoje = datetime.now().replace(second=0, microsecond=0)"            
            
            # Recupera o cursos para executar um bloco PL/SQL anônimo
            cursor = oracle.connect()
            # Cria a variável de saída com o tipo especificado
            output_value = cursor.var(int)

            data = dict(codigo=output_value, cpf=funcionarios.get_CPF())
            cursor.execute("""
                    begin
                        :codigo := CODIGO_PONTO_SEQ.NEXTVAL;
                        insert into ponto(CODIGO_PONTO, CPF) values(:codigo, :cpf);
                    end;
                    """, data)
            codigo_ponto = output_value.getvalue()
            oracle.conn.commit()
        
            df_ponto = oracle.sqlToDataFrame(f"select codigo_ponto, data_hora from ponto where codigo_ponto = {codigo_ponto}")
            novo_ponto = Ponto(df_ponto.codigo_ponto.values[0], pd.to_datetime(str(df_ponto.data_hora.values[0])), funcionarios)
            print(novo_ponto.to_string())

            responder_novamente = input('Você deseja adicionar mais um ponto? [S ou N]: ')
            while(responder_novamente.lower() != 's' and responder_novamente.lower() != 'n'):
                responder_novamente = input('A opção "'+ responder_novamente +'" não existe. Você deseja adicionar mais um ponto? [S ou N]: ')
            if (responder_novamente.lower() == 'n'):
                return novo_ponto
    
    def atualizar_ponto(self) -> Ponto:
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        responder_novamente = 's'

        while(responder_novamente.lower() == 's'):
            codigo_ponto = input("Código do horário do ponto que irá alterar: ")

            if not self.verifica_existencia_ponto(oracle, codigo_ponto):
                data_str = input("Digite uma data (DD/MM/YYYY hh:mm): ")
                nova_data_hora = datetime.strptime(data_str,"%d/%m/%Y %H:%M")

                oracle.write(f"update ponto set data_hora = TO_DATE('{nova_data_hora.strftime('%d/%m/%Y %H:%M')}', 'DD/MM/YYYY HH24:MI') where codigo_ponto = {codigo_ponto}")
                df_ponto = oracle.sqlToDataFrame(f"select codigo_ponto, data_hora, cpf from ponto where codigo_ponto = {codigo_ponto}")
                funcionario = self.valida_funcionario(oracle, df_ponto.cpf.values[0])
                data_atualizada = Ponto(df_ponto.codigo_ponto.values[0], pd.to_datetime(str(df_ponto.data_hora.values[0])), funcionario)

                print(data_atualizada.to_string())
                responder_novamente = input('Deseja atualizar mais algum ponto? [S ou N]: ')
                while(responder_novamente.lower() != 's' and responder_novamente.lower() != 'n'):
                    responder_novamente = input('A opção "'+ responder_novamente +'" não existe. Deseja realizar atualizar mais algum ponto? [S ou N]: ')
                if (responder_novamente.lower == 'n'):
                    return data_atualizada
            else:
                print(f'O código {codigo_ponto} não existe.')

    def excluir_ponto(self):
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        responder_novamente = 's'

        while(responder_novamente.lower() == 's'):
            codigo_ponto = input("Digite o código do ponto que irá excluir: ")

            if not self.verifica_existencia_ponto(oracle, codigo_ponto):
                df_ponto = oracle.sqlToDataFrame(f"select codigo_ponto, data_hora, cpf from ponto where codigo_ponto = {codigo_ponto}")
                funcionario = self.valida_funcionario(oracle, df_ponto.cpf.values[0])
                opcao_excluir = input(f"Tem certeza que deseja excluir o ponto {codigo_ponto} [S ou N]: ")

                while(opcao_excluir.lower() != 's' and opcao_excluir.lower() != 'n'):
                    opcao_excluir = input(f'A opção "{opcao_excluir}" não existe. Tem certeza que deseja excluir o ponto {codigo_ponto} [S ou N]: ')
                if (opcao_excluir.lower() == "s"):
                    oracle.write(f"delete from ponto where codigo_ponto = {codigo_ponto}")
                    # Cria um novo objeto Produto para informar que foi removido
                    ponto_excluido = Ponto(df_ponto.codigo_ponto.values[0], pd.to_datetime(str(df_ponto.data_hora.values[0])), funcionario)
                    # Exibe os atributos do produto excluído
                    print("Ponto removido com sucesso!")
                    print(ponto_excluido.to_string())

                    responder_novamente = input('Deseja remover mais um ponto? [S ou N]: ')
                    while(responder_novamente.lower() != 's' and responder_novamente.lower() != 'n'):
                        responder_novamente = input('A opção "'+ responder_novamente +'" não existe. Você deseja remover mais um ponto? [S ou N]: ')

                elif (opcao_excluir.lower() == 'n'):
                    responder_novamente = opcao_excluir
                    print('Remoção do funcionário: "' + codigo_ponto + '" cancelada.')
            else:
                print(f'O código "{codigo_ponto}" não existe.')

    def verifica_existencia_ponto(self, oracle:OracleQueries, codigo_ponto:int=None) -> bool:
        df_ponto = oracle.sqlToDataFrame(f"select codigo_ponto, data_hora from ponto where codigo_ponto = {codigo_ponto}")
        return df_ponto.empty

    def listar_funcionarios(self, oracle:OracleQueries, need_connect:bool=False):
        query = """
                select f.cpf
                    ,  f.nome
                    ,  f.cargo
                from funcionarios f
                order by f.nome
                """
        if need_connect:
            oracle.connect()
        print(oracle.sqlToDataFrame(query))
    
    def listar_ponto(self, oracle:OracleQueries, need_connect:bool=False):
        query = """
                select p.codigo_ponto
                    ,  p.data_hora
                    ,  f.nome as funcionarios
                from ponto p
                inner join funcionarios f
                on p.cpf = f.cpf
                order by f.nome, p.data_hora
                """
        if need_connect:
            oracle.connect()
        print(oracle.sqlToDataFrame(query))
        
    def valida_funcionario(self, oracle:OracleQueries, cpf:str=None) -> Funcionarios:
        if self.ctrl_funcionario.verifica_existencia_funcionario(oracle, cpf):
            print(f'O CPF "{cpf}" informada não existe')
            return None
        else:
            oracle.connect()
            df_funcionario = oracle.sqlToDataFrame(f"select cpf, nome, cargo from funcionarios where cpf = {cpf}")
            funcionarios = Funcionarios(df_funcionario.cpf.values[0], df_funcionario.nome.values[0], df_funcionario.cargo.values[0])
            return funcionarios
        
    def valida_ponto(self, oracle:OracleQueries, codigo_ponto:int=None) -> Ponto:
        if self.verifica_existencia_ponto(oracle, codigo_ponto):
            print(f"O código do ponto {codigo_ponto} informado não existe.")
        else:
            oracle.connect()
            funcionario = self.valida_funcionario(oracle, df_ponto.cpf.values[0])
            df_ponto = oracle.sqlToDataFrame(f"select codigo_ponto, data_hora, cpf from ponto where codigo_ponto = {codigo_ponto}")
            ponto = Ponto(df_ponto.codigo_ponto.values[0], df_ponto.data_hora.values[0], funcionario)
            return ponto