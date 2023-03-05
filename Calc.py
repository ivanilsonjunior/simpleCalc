class Calc:
    """Calculadora
    Classe que representa uma calculadora basica de dois numeros

    Parameters
    ----------
    a : int
        Primeiro termo
    b : int
        Segundo termo
    """
    def __init__ (self, a, b):
        '''Metodo construtor onde os fatores devem ser informados'''
        self.a = a
        self.b = b

    def soma(self):
        '''Retorna a soma do fator a com o fator b'''
        return self.a + self.b
    
    def subtrai(self):
        '''Retorna a subtracao do fator e o fator b'''
        return self.a - self.b

    def multiplica(self):
        '''Retorna a multiplicacao entre o fator a e o fator b.
        Lembrando que uma multiplicacao eh uma sequencia de somas do fator a com ele mesmo, b vezes.
        Ex:     3 x 3 = 3 + 3 + 3
                4 x 2 = 4 + 4
                1 x 10 = 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1'''
        retorno = 0
        for i in range(self.b):
            retorno += self.a
        return retorno
    
    def divide(self):
        '''Retorna o resultado da divisao de a por b
        '''
        return self.a/self.b
