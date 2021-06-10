import unittest
import math as mt

class ArbolBinario():
    def __init__(self, lista):
        self.lista = lista
    def height_binary_tree(self):
        return mt.floor(mt.log2(len(self.lista)))
    def node_neightbors(self,objetivo):
        auxlist = self.bfs2()
        
        for j in range(len(auxlist)):
            for i in range(len(auxlist[j])):
                if auxlist[j][i]==objetivo:
                    if i>0:
                        izq=auxlist[j][i-1]
                    else:
                        izq=None
                    if  i<len(auxlist[j]):
                        der=auxlist[j][i+1]
                    else:
                        der=None  
                    
                    return [izq,der]
        return [None,None]
    def bfs2(self):
        auxlist = []
        auxlist2= []

        for i in range(int(self.height_binary_tree())+1):
            auxl1 = []
            for j in range(2**i):
                fr=(2*j+1)/(2**(i+1))
                num=int(mt.floor(len(self.lista)*fr))
        
                
                if auxlist2.count(num)== 0:
                    auxl1.append(self.lista[num])
                    auxlist2.append(num)
            auxlist.append(auxl1)
        return auxlist
    def bfs(self):
        auxlist = []
        auxlist2= []

        for i in range(int(self.height_binary_tree())+1):
            auxl1 = []
            for j in reversed(range(2**i)):
                fr=(2*j+1)/(2**(i+1))
                num=int(mt.floor(len(self.lista)*fr))
        
                
                if auxlist2.count(num)== 0:
                    auxlist.append(self.lista[num])
                    auxlist2.append(num)
        return auxlist        
            
    

class CajaNegraTest (unittest.TestCase):
    def test_prueba1(self):
        lista_prueba = [1,2,3,4,5,6,7,8]
        Arbol = ArbolBinario(lista_prueba)  
        resultado = Arbol.height_binary_tree()
        self.assertEqual(resultado, 3)
    def test_prueba2(self):
        lista_prueba = [1,2,3,4,5,6,7,8]
        Arbol = ArbolBinario(lista_prueba)
        resultado = Arbol.node_neightbors(2)
        self.assertEqual(resultado,[None,4])
    def test_prueba3(self):
        lista_prueba = [-3,-4,1]
        Arbol = ArbolBinario(lista_prueba)   
        resultado = Arbol.bfs()
        self.assertEqual(resultado, [-4,1,-3])
if __name__ == '__main__':


    #lista_prueba = [1,2,3,4,5,6,7,8]
    #Arbol = ArbolBinario(lista_prueba) 
    #print(Arbol.height_binary_tree())  
    #print(Arbol.node_neightbors(2))
    #print(Arbol.bfs())
    
    unittest.main()
            