#e.g.
from task1 import kwargsAcceptFun
kwargsAcceptFun(ism1="Asadbek", yosh2=25, joy3="Beshariq")
kwargsAcceptFun()
from task2 import typeBasedTransformer
info = {
    'a': 12,
    'b': 3.5,
    'c': "Keyin",
    'd': False,
    'e': [4, 3, 2],
    'f': {"h": 2, "t": 1},
    'g': None,
    'h': (1, 4, 8)
}

rezultat = typeBasedTransformer(info)
print(rezultat)


from task3 import func,funx
if __name__ == "__main__":
    func()
    funx()
    func()
    funx()
    func()
