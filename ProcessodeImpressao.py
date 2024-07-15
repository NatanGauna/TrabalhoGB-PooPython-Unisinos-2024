from Processo import processo

# Inicializa um PrintingProcess (Processo de impressão) com PID e uma fila de processos


class PrintingProcess(processo): 
    def __init__(self, pid, fila_de_processos):
        super().__init__(pid)
        self.fila_de_processos = fila_de_processos

    def execute(self):
        for processo in self.fila_de_processos:
            print(f'PID: {processo.pid}, Tipo: {type(processo).__name__}, Atributos: {processo.__dict__} ')
            