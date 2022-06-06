class Palindromo:
    __palabra=None
    def __init__(self,palabra=''):
        self.__palabra=palabra
    def esPalindromo(self):
        i=0
        j=-1
        bandera=True
        cantidad=round(len(self.__palabra))
        while i<cantidad and bandera:
            if self.__palabra[i]!=self.__palabra[j]:
                bandera=False
            else:
                i+=1
                j+=1
        return bandera
    def setPalabra(self,palabra):
        self.__palabra=palabra