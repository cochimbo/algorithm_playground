from TreeNary import TreeNary
import time
import pathlib
import os

DECIMALS_TIME = 5

def main():
    tree = TreeNary()
    os.chdir(pathlib.Path(__file__).parent.resolve())
    f = open("palabras_espanyol.txt", "r", encoding="utf8")
    start = time.process_time()
    for x in f:
        tree.insertWord(x.rstrip().strip())
    f.close()
    inCons = ""
    print("Arbol cargado en %d  segundos".format(round(time.process_time() - start, DECIMALS_TIME)))
    while (inCons != "exit"):
        print("Introduzca texto para ver palabras con dicha precedencia (teclee exit para salir)")
        inCons = input()
        start = time.process_time()
        try:
            node = tree.searchNode(inCons)
            inArray = []
            node.getAllLeafs(inArray, inCons)
            if(inCons == "exit"):
                break
            timesearch = time.process_time() - start
            print("Palabras coincidentes y/o precedidas de %s : ".format(inCons))
            inArray.sort()
            for x in inArray:
                print(x)
            print(f"Busqueda de {str(len(inArray))} elementos en {round(timesearch, DECIMALS_TIME)} segundos")
        except Exception as e:
            print(e)
if __name__ == "__main__":
    main()
