#classe processo de calculo

from Processo import processo

# Inicializa o processo de cálculo com o PID, operandos e operador

class processo_de_calculo(processo):
    def __init__(self, pid, operando1: int, operando2: int, resultado:int, operador):
        super().__init__(pid)
        
        self.__operando1 = operando1
        self.__operando2 = operando2
        self.__operador = operador
        self.__resultado = resultado
        
    @property
    def operando1(self):
        return self.__operando1
    
    @operando1.setter
    def operando1(self,operando1):
        self.__operando1 = operando1
    

    @property
    def operando2(self):
        return self.__operando2

    @operando2.setter
    def operando2(self, operando2):
        self.__operando2 = operando2


    @property
    def operador(self):
        return self.__operador
    
    @operador.setter
    def operador(self, operador):
        self.__operador = operador


    @property
    def resultado(self):
        return self.__resultado
    
    @resultado.setter
    def resultado(self,resultado):
        self.__resultado = resultado


    def execute(self, operador, operando1, operando2, resultado):
    # As linhas aseguir checam o operador da equação para se certificar de dar o resultado correto
        if operador == "+":
            resultado = operando1 + operando2

        elif  operador == "-":
            resultado = operando1 - operando2
        
        if operador == "*":
            resultado = operando1 * operando2

        elif  operador == "/":
            resultado = operando1 / operando2
        
        resultado = int(resultado)
        print(resultado)
       # return operador




