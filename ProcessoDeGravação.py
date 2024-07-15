from Processo import processo
from ProcessoDeCalculo import processo_de_calculo
from Fila import fila
#from ProcessoDeCalculo import processo_de_calculo
c = processo_de_calculo

# Inicializa um WritingProcess (Processo de Gravação) com PID, expressão, operandos e operador

class WritingProcess(processo): 
    def __init__(self, pid, expressao, operando1: int, operando2: int, operador):
        super().__init__(pid)
        self.expressao = expressao
        self.operando1 = operando1
        self.operando2 = operando2
        self.operador = operador

# Escreve os operandos, operador e expressão no arquivo computation.txt
# É importante destacar que a ordem na qual os itens são salvos deve ser sempre a mesma para garantir uma leitura sem falhas no futuro
    def execute(self):
        with open('computation.txt', 'a') as f:
            f.write(str(self.operando1) + "\n")
            f.write(str(self.operador) + "\n")
            f.write(str(self.operando2) + "\n")
            f.write(str(self.expressao) + "\n")
        #    f.write("\n")

    


