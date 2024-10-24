from conexion.oracle_queries import OracleQueries

class Relatorio:
    def __init__(self):
        with open("sql/relatorio_funcionarios.sql") as f:
            self.query_relatorio_funcionarios = f.read()

        with open("sql/relatorio_ponto.sql") as f:
            self.query_relatorio_ponto = f.read()

        with open("sql/relatorio_funcionarios_ponto.sql") as f:
            self.query_relatorio_funcionarios_ponto = f.read()

        with open("sql/relatorio_contagem_ponto.sql") as f:
            self.query_relatorio_contagem_ponto = f.read()

    def get_relatorio_funcionario(self):
        oracle = OracleQueries()
        oracle.connect()
        print(oracle.sqlToDataFrame(self.query_relatorio_funcionarios))
        input('Pressione "Enter" para sair do relatório de funcionario.')

    def get_relatorio_ponto(self):
        oracle = OracleQueries()
        oracle.connect()
        print(oracle.sqlToDataFrame(self.query_relatorio_ponto))
        input('Pressione "Enter" para sair do relatório de ponto.')

    def get_relatorio_funcionario_ponto(self):
        oracle = OracleQueries()
        oracle.connect()
        print(oracle.sqlToDataFrame(self.query_relatorio_funcionarios_ponto))
        input('Pressione "Enter" para sair do relatório de funcionários com ponto.')

    def get_relatorio_contagem_ponto(self):
        oracle = OracleQueries()
        oracle.connect()
        print(oracle.sqlToDataFrame(self.query_relatorio_contagem_ponto))
        input('Pressione "Enter" para sair do relatório de funcionários com ponto.')