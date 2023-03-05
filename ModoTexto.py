from Calc import *
class InterfaceTexto:
    '''
    Interface texto da calculadora usa a Classe Calc
    '''
    def __init__(self) -> None:
        self.calc = Calc(a=0,b=0)
        self.display = ""
        self.updateDisplay()
        self.showInterface()
        

    def showInterface(self):
        '''
        Metodo da interface de texto responsavel por mostrar as opcoes para o usuario, o unico print estah neste metodo
        '''
        opcao = -1
        while opcao != 0:
            print (self.menu())
            opcao = int(input("Insira sua opção: "))
            self.tratarOpcao(opcao)

    def menu(self):
        '''
        Menu a ser apresentado para o usuario
        '''
        return "Display: {}\n1 - Definir Fatores \n2 - Soma\n3 - Subtrai\n4 - Multiplica\n5 - Divide\n9 - Ajuda\n0 - Sair".format(self.display)
    
    def tratarOpcao(self,opcao):
        '''
        Resposavel por tratar a opcao informada pelo usuario, qualquer opcao nova eh colocada aqui
        '''
        if(opcao == 1):
            self.calc.a = self.fatorA()
            self.calc.b = self.fatorB()
            self.updateDisplay()
        if(opcao == 2):
            self.updateDisplay("+", self.calc.soma())
        if(opcao == 3):
            self.updateDisplay("-", self.calc.subtrai())
        if(opcao == 4):
            self.updateDisplay("*", self.calc.multiplica())
        if(opcao == 5):
            self.updateDisplay("/", self.calc.divide())        
        if(opcao == 9):
            self.updateDisplay("?", help(Calc))

    def fatorA(self) -> int:
        '''
        Recebe o fator A
        '''
        return int(input("Insira do fator A: "))

    def fatorB(self) -> int:
        '''
        Recebe o fator B
        '''
        return int(input("Insira do fator B: "))

    def updateDisplay(self, operacao=None, resultado=None):
        '''
        Responsavel por atualizar o display do menu, tive que implementar a sobrecarga de metodo na mao pois a maneira mais elegante seria usando multipledispatch, fiz desta maneira para evitar a necessidade de outro pacote, mas a sobrecarga eh feita e tratada a depender da forma com que o metodo eh chamado
        '''
        if operacao == None and resultado == None:
            self.display = "A:{}, B:{}".format(self.calc.a, self.calc.b)
        else:
            self.display = "A:{} {} B:{} = {}".format(self.calc.a, operacao, self.calc.b, resultado)

def principal():
    inter = InterfaceTexto()

if __name__ == "__main__":
    principal()