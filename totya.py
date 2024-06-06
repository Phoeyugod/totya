import random

def melegtotya():
    szazalek = random.randint(1, 100)
    print(f"togya ennyire hetero {szazalek}%.")
    if szazalek >= 50:
        print("Totya hetero")
    else:
        print("Totya meleg.")

melegtotya()
