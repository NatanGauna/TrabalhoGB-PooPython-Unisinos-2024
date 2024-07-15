#Main
from ProcessoDeCalculo import processo_de_calculo
#from fila_de_processos import fila_de_processos
from ProcessoDeGravação import WritingProcess
from ProcessoDeLeitura  import ReadingProcess
from  ProcessodeImpressao  import PrintingProcess

fila_de_processos = []
i = PrintingProcess
c = processo_de_calculo
g = WritingProcess
l = ReadingProcess

# Menu interativo onde é possível gerenciar a fila de processos

def main():

#Primeiro menu de selação 
    resposta = ""
    while resposta != "esc":
    #    for i in fila_de_processos:
  #         print(type(i))
        print("Insira sua escolha:")
        print("C = Criar processo")
        print("E = Executar proximo processo")
        print("P = Executar processo especifico:")
        print("S = salvar fila de processos:")
        print("A = Carregar arquivo de fila de processos")
        print("Esc = Sair")
        resposta = input("")

        if resposta.lower() == "esc":
            break

#menu de criação de proessos
        if resposta == "C" or resposta == "c":

            print("Insira o processo que deseja executar: ")
            print("C = processo de calculo")
            print("G = processo de gravação")
            print("L = processo de leitura")
            print("I = Processo de impressão")

            resposta = input("")

            if resposta == "C" or resposta == "c":
                print("Insira o operador a ser utilizado")
                operador = input("+,-,/,* ")

                print("Insira o primeiro numero")
                operando1 = int(input())

                print("Insira o segundo numero")
                operando2 = int(input())
                c = processo_de_calculo(len(fila_de_processos),operando1, operando2, "", operador)
                fila_de_processos.append(c)
                print(c.pid)
            
            elif resposta == "G" or resposta == "g":
                print("Insira o operador a ser utilizado")
                operador = input("+,-,/,* ")

                print("Insira o primeiro numero")
                operando1 = int(input())

                print("Insira o segundo numero")
                operando2 = int(input())
                calculo = operando1, operador, operando2
                g = WritingProcess(len(fila_de_processos), calculo,  operando1, operando2, operador)
        
                fila_de_processos.append(g)
                print(g.pid)
            
            elif resposta == "L" or resposta == "l":
                l = ReadingProcess(len(fila_de_processos),fila_de_processos)
                fila_de_processos.append(l)
                print("Processo de leitura adicionado á fila_de_processos")
                print(l.pid)
            
            elif resposta == "I" or resposta == "i":
                i = PrintingProcess(len(fila_de_processos), fila_de_processos)
                fila_de_processos.append(i)
                print(i.pid)
#esta opção executa o proximo processo da fila e o retira da mesma
        elif resposta == "E" or resposta =="e":
            fila_de_processos.reverse()
            for a in fila_de_processos:
                if type(a) is WritingProcess:
                    a.execute()
                    print(a.expressao)
                    fila_de_processos.remove(a)
                    break

                elif type(a) is processo_de_calculo:
                    print("Resultado: ")
                    print(a.operando1, a.operador, a.operando2)
                    a.execute(a.operador,a.operando1,a.operando2,"")
                    fila_de_processos.remove(a)
                    break
                
                elif type(a) is ReadingProcess:
                    a.execute()
                    fila_de_processos.remove(a)
                    break
                    
                elif type(a) is PrintingProcess:
                    a.execute()
                    fila_de_processos.remove(a)
                    break
            fila_de_processos.reverse()
#Esta opção procura o process ID inserido na lista e executa o processo associado
        elif resposta == "P" or resposta == "p":
            print("Insira o Process ID do processo")
            PID = input()
            PID = str(PID)
            for i in fila_de_processos:
                i.pid = str(i.pid)
                print(i.pid)
                print(PID)
                if i.pid == PID:
                    print("Achou!")
                    if type(i) is WritingProcess:
                        i.execute()
                        print(i.expressao)
                        fila_de_processos.remove(i)
                        break

                    elif type(i) is processo_de_calculo:
                        print("Resultado: ")
                        print(i.operando1, i.operador, i.operando2)
                        i.execute(i.operador,i.operando1,i.operando2,"")
                        fila_de_processos.remove(i)
                        break
                    
                    elif type(i) is ReadingProcess:
                        i.execute()
                        fila_de_processos.remove(i)
                        break
                        
                    elif type(i) is PrintingProcess:
                        i.execute()
                        fila_de_processos.remove(i)
                        break
                else:
                    print("Procurando...")
#Salva a fila de processos em um arquivo
        elif resposta == "S" or resposta == "s":
            save = open("Fila_processos.txt", "w")
            for i in fila_de_processos:
                if type(i) is processo_de_calculo:
                    save.write("compute" + "\n")
                    save.write(str(i.operando1) + "\n")
                    save.write(str(i.operador) + "\n")
                    save.write(str(i.operando2) + "\n")
                    save.close

                elif type(i) is WritingProcess:
                    save.write("writing" + "\n")
                    save.write(str(i.operando1) + "\n")
                    save.write(str(i.operador)+ "\n")
                    save.write(str(i.operando2)+ "\n")
                    save.close

                elif type(i) is ReadingProcess:
                    save.write("reading" + "\n")
                    save.close
                
                elif type(i) is PrintingProcess:
                    save.write("print" + "\n")
                    save.close
#Carrega o arquivo de uma lista de processos salva       
        elif resposta == "A" or resposta == "a":
            save = open("Fila_processos.txt", "r")
            arquivo = save.readlines()
            contador = 0
            obj = ""

            for i in arquivo:
                while contador <=4:
                    contador += 1
                    if contador == 1:
                        
                        tipo = i.strip()
                        
                        if tipo == "compute":
                            obj = processo_de_calculo
                            
                        elif tipo == "writing":
                            obj = WritingProcess
                            
                        elif tipo == "reading":
                            obj = ReadingProcess(len(fila_de_processos), fila_de_processos)
                            fila_de_processos.append(obj)
                            contador = 0
                            
                        elif tipo == "print":
                            obj = PrintingProcess(len(fila_de_processos), fila_de_processos)
                            fila_de_processos.append(obj)
                            contador = 0
                        break
           
                    elif contador == 2:
                        if tipo == "compute" or tipo == "writing":
                            operando1 = i.strip()
                            operando1 = int(operando1)
                            break
                    
                    elif contador == 3: 
                        if tipo == "compute" or tipo == "writing":
                            operador = i.strip()
                            break
                    
                    elif contador == 4:
                        if tipo == "compute" or tipo == "writing":
                            operando2 = i.strip()
                            operando2 = int(operando2)
                            if tipo == "compute":
                                obj = processo_de_calculo(len(fila_de_processos),operando1, operando2, "", operador)
                                fila_de_processos.append(obj)
                            elif tipo == "writing":
                                expressao = operando1, operador, operando2
                                obj = WritingProcess(len(fila_de_processos), expressao, operando1, operando2,operador)
                                fila_de_processos.append(obj)
                            contador = 0
                            break


            
    
if __name__ == "__main__":
    main()
