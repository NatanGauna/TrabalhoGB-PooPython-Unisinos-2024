from Processo import processo
from ProcessoDeCalculo import processo_de_calculo

#c = processo_de_calculo()

# Inicializa um ReadingProcess (Processo de Leitura) com PID e uma fila de processos

class ReadingProcess(processo): 
    def __init__(self, pid, fila_de_processos):
        super().__init__(pid)
        self.fila_de_processos = fila_de_processos

# Executa a leitura dos processos a partir do arquivo computation.txt e adiciona a fila de processos

    def execute(self):
        with open("computation.txt", 'r') as f:
            linhas = f.readlines()
          #  print(linhas)
            contador = 0
    #O programa utiliza um contador para ler cada linha do arquivo
    #As informações do arquivo possuem uma ordem, que é seguida pelo programa
            for linha in linhas:
                while contador <=4:
                    contador += 1
                    #print(contador)
                    if contador == 1:
                        operando1 = linha.strip()
                       # print(linha)
                        if operando1.isdigit():
                            operando1 = int(operando1)
                        break

                    elif contador == 2:
                        operador = linha.strip()
                      #  print(linha)
                        break

                    elif contador == 3:
                        operando2 = linha.strip()
                     #   print(linha)
                        if operando2.isdigit():
                            operando2 = int(operando2)
                        break

                    elif  contador == 4:
                        print("Processo adicionado")
                      #  print(linha)
                        contador = 0
                        processo = processo_de_calculo(len(self.fila_de_processos), operando1, operando2,"",operador)
                        self.fila_de_processos.append(processo)
                        break
            f.close()            
        f = open("computation.txt", 'w')
        f.close()