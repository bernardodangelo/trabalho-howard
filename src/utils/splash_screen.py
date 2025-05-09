from conexion.oracle_queries import OracleQueries
from utils import config

class SplashScreen:

    def __init__(self):
        # Consultas de contagem de registros - inicio
        self.qry_total_funcionarios = config.QUERY_COUNT.format(tabela="funcionarios")
        self.qry_total_ponto = config.QUERY_COUNT.format(tabela="ponto")
        # Consultas de contagem de registros - fim

        # Nome(s) do(s) criador(es)
        self.created_by = """Bernardo D'Angelo
        #              Jefferson Buloto de Souza
        #              João Vithor Lordes Stem Machado
        #              Luciano da Silva Paiva
        #              Nathan Alexandre Vidigal de Souza"""
        self.professor = "Prof. M.Sc. Howard Roatti"
        self.disciplina = "Banco de Dados"
        self.semestre = "2024/2"

    def get_total_funcionarios(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Retorna o total de registros computado pela query
        return oracle.sqlToDataFrame(self.qry_total_funcionarios)["total_funcionarios"].values[0]

    def get_total_ponto(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Retorna o total de registros computado pela query
        return oracle.sqlToDataFrame(self.qry_total_ponto)["total_ponto"].values[0]

    def get_updated_screen(self):
        return f"""
        ########################################################
        #                   SISTEMA DE VENDAS                     
        #                                                         
        #  TOTAL DE REGISTROS:                                    
        #      1 - FUNCIONARIOS:  {str(self.get_total_funcionarios()).rjust(5)}
        #      2 - PONTO:         {str(self.get_total_ponto()).rjust(5)}
        #
        #  CRIADO POR: {self.created_by}
        #
        #  PROFESSOR:  {self.professor}
        #
        #  DISCIPLINA: {self.disciplina}
        #              {self.semestre}
        ########################################################
        """