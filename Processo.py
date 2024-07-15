#Trabalho Grau B programação orientada a objetos

# Inicializa um objeto Processo com um ID de processo (PID)

class processo:

    def __init__(self, pid):
        self.__pid =  pid

 # Propriedade para obter o PID do processo

    @property
    def pid(self):
        return self.__pid
    
# Setter para alterar o PID do processo

    @pid.setter
    def pid(self,pid):
        self.__pid = pid

# Método para executar o processo (vazio por padrão)

    def execute(self):
        pass
        

    