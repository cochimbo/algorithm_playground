from TreeNode import TreeNode
from TreeNary import TreeNary
import time
import pathlib
import os

def main():
    tree = TreeNary()
    os.chdir(pathlib.Path(__file__).parent.resolve())
    f = open("palabras_espanyol.txt", "r", encoding="utf8")
    start = time.process_time()
    for x in f:
        tree.insertWord(x.rstrip().strip())
    inCons = ""
    print("Arbol cargado en " + str(time.process_time() - start) + " segundos")
    while (True):
        print("Introduzca texto para ver palabras con dicha precedencia (teclee exit para salir)")
        inCons = input()
        start = time.process_time()
        try:
            node = tree.searchNode(inCons)
            inArray = []
            node.getAllLeafs(inArray, inCons)
            if(inCons == "exit"):
                break
            timesearch = str(time.process_time() - start)
            print("Palabras precedidas de " + inCons + " : ")
            inArray.sort()
            for x in inArray:
                print(x)
            print("Busqueda de " + str(len(inArray)) + " elementos en " + timesearch + " segundos")
        except Exception as e:
            print(e)
if __name__ == "__main__":
    main()
