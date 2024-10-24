from model.funcionarios import Funcionarios
from conexion.oracle_queries import OracleQueries

class Constroller_Funcionario:
    def __init__(self):
        pass

    def inserir_funcionario(self) -> Funcionarios:
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        responder_novamente = 's'

        while(responder_novamente.lower() == 's'):
            cpf = str(input("CPF (Novo): "))
            if self.verifica_existencia_funcionario(oracle, cpf):
                nome = input("Nome: ")
                cargo = input("Cargo: ")

                oracle.write(f"insert into funcionarios values ('{cpf}', '{nome}', '{cargo}')")
                df_funcionarios = oracle.sqlToDataFrame(f"select cpf, nome, cargo from funcionarios where cpf = '{cpf}'")
                novo_funcionario = Funcionarios(df_funcionarios.cpf.values[0], df_funcionarios.nome.values[0], df_funcionarios.cargo.values[0])
                print(novo_funcionario.to_string())

                responder_novamente = input('Você deseja adicionar mais um funcionário? [S ou N]: ')
                while(responder_novamente.lower() != 's' and responder_novamente.lower() != 'n'):
                    responder_novamente = input('A opção "'+ responder_novamente +'" não existe. Você deseja adicionar mais um funcionário? [S ou N]: ')
                if (responder_novamente.lower() == 'n'):
                    return novo_funcionario

            else:
                print(f'O CPF "{cpf}" já está cadastrada.')

    def atualizar_funcionario(self) -> Funcionarios:
        oracle = OracleQueries(can_write=True)
        oracle.connect() 
        responder_novamente = 's'

        while(responder_novamente.lower() == 's'):
            cpf = int(input("Digite a CPF do funcionario no qual deseja alterar algo: "))

            if not self.verifica_existencia_funcionario(oracle, cpf):
                escolher_opcao = input('Escolha o que você deseja alterar [N = Nome ou C = Cargo]: ')
                while(escolher_opcao.lower() != 'n' and escolher_opcao.lower() != 'c'):
                    escolher_opcao = input('A opção "' + escolher_opcao  + '" não existe. Escolha o que você deseja alterar [N = Nome ou C = Cargo]: ')
                if (escolher_opcao.lower() == 'n'):
                    novo_nome = input("Nome: ")
                    oracle.write(f"update funcionarios set nome = '{novo_nome}' where cpf = {cpf}")
                elif (escolher_opcao.lower() == 'c'):
                    novo_cargo = input("Cargo: ")
                    oracle.write(f"update funcionarios set cargo = '{novo_cargo}' where cpf = {cpf}")

                df_funcionarios = oracle.sqlToDataFrame(f"select cpf, nome, cargo from funcionarios where cpf = {cpf}")
                funcionario_atualizado = Funcionarios(df_funcionarios.cpf.values[0], df_funcionarios.nome.values[0], df_funcionarios.cargo.values[0])
                print(funcionario_atualizado.to_string())

                responder_novamente = input('Deseja realizar atualizar mais algum funcionario? [S ou N]: ')
                while (responder_novamente.lower() != 's' and responder_novamente.lower() != 'n'):
                    responder_novamente = input('A opção "'+ responder_novamente +'" não existe. Deseja realizar atualizar mais algum funcionario? [S ou N]: ')
                if (responder_novamente.lower() == 'n'):
                    return funcionario_atualizado
            else:
                print(f'O CPF "{cpf}" não existe.')

    def excluir_funcionario(self):
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        responder_novamente = 's'

        while(responder_novamente.lower() == 's'):
            cpf = input("CPF do funcionario que irá remover: ")

            if not self.verifica_existencia_funcionario(oracle, cpf):
                opcao_excluir = input(f"Tem certeza que deseja remover o funcionário com o CPF {cpf} [S ou N]: ")

                while (opcao_excluir.lower() != 's' and opcao_excluir.lower() != 'n'):
                    opcao_excluir = input(f'A opção "{opcao_excluir}" não existe. Tem certeza que deseja remover o funcionário com o CPF {cpf} [S ou N]: ')
                if (opcao_excluir.lower() == 's'):
                    print(f"Atenção, caso possua horários de ponto, também serão excluídos!")
                    opcao_excluir = input(f"Tem certeza que deseja remover o funcionário com o CPF {cpf} [S ou N]: ")
                    
                    while (opcao_excluir.lower() != 's' and opcao_excluir.lower() != 'n'):
                        opcao_excluir = input(f'A opção "{opcao_excluir}" não existe. Tem certeza que deseja remover o funcionário com o CPF {cpf} [S ou N]: ')
                    if (opcao_excluir.lower() == 's'):
                        df_funcionarios = oracle.sqlToDataFrame(f"select cpf, nome, cargo from funcionarios where cpf = {cpf}")
                        oracle.write(f"delete from ponto where cpf = {cpf}")
                        print('Ponto removido com sucesso!')
                        oracle.write(f"delete from funcionarios where cpf = {cpf}")
                        funcionario_excluido = Funcionarios(df_funcionarios.cpf.values[0], df_funcionarios.nome.values[0], df_funcionarios.cargo.values[0])

                        print("Funcionario removido com sucesso!")
                        print(funcionario_excluido.to_string())

                        responder_novamente = input('Deseja remover mais um funcionário? [S ou N]: ')
                        while(responder_novamente.lower() != 's' and responder_novamente.lower() != 'n'):
                            responder_novamente = input('A opção "'+ responder_novamente +'" não existe. Você deseja remover mais um funcionário? [S ou N]: ')
                    elif (opcao_excluir == 'n'):
                        responder_novamente = opcao_excluir
                        print('Remoção do funcionário: "' + cpf + '" cancelada.')
                elif (opcao_excluir == 'n'):
                    responder_novamente = opcao_excluir
                    print('Remoção do funcionário: "' + cpf + '" cancelada.')
            else:
                print(f'O CPF "{cpf}" não existe.')

    def verifica_existencia_funcionario(self, oracle:OracleQueries, cpf:str=None) -> bool:
        df_funcionarios = oracle.sqlToDataFrame(f"select cpf, nome, cargo from funcionarios where cpf = {cpf}")
        return df_funcionarios.empty