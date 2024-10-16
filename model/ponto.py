class Ponto:
    def __init__(self, id_ponto, funcionario, data_ponto, hora_entrada, hora_saida=None, total_horas=None):
        self.id_ponto = id_ponto
        self.funcionario = funcionario 
        self.data_ponto = data_ponto
        self.hora_entrada = hora_entrada
        self.hora_saida = hora_saida
        self.total_horas = total_horas

    def registrar_saida(self, hora_saida):
        self.hora_saida = hora_saida
        self.total_horas = self.calcular_total_horas()

    def calcular_total_horas(self):
        if self.hora_saida and self.hora_entrada:
            diferenca_tempo = self.hora_saida - self.hora_entrada
            total_horas = diferenca_tempo.total_seconds() / 3600  # Converte de segundos para horas
            return round(total_horas, 2)
        return None