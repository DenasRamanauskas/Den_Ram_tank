
class Tank:
    x = 0
    y = 0
    taskai = 100
    kryptis = ""
    kryptys = {"w": "pirmyn", "s": "atgal", "a": "kairėn", "d": "dešinėn"}
    suviai = {"w": 0, "s": 0, "a": 0, "d": 0}

    def pirmyn(self):
        self.y += 1
        self.kryptis = "w"
        self.taskai -= 10
        print("Pirmyn")

    def atgal(self):
        self.y -= 1
        self.kryptis = "s"
        self.taskai -= 10
        print("Atgal")

    def kairen(self):
        self.x -= 1
        self.kryptis = "a"
        self.taskai -= 10
        print("Kairėn")

    def desinen(self):
        self.x += 1
        self.kryptis = "d"
        self.taskai -= 10
        print("Dešinėn")

    def suvis(self):
        self.suviai[self.kryptis] += 1
        self.taskai -= 10

    def info(self):
        self.taskai -= 10
        print("\n")
        print(f"Kryptis: {self.kryptys}")
        print(f"Tanko koordinatės: x: {self.x}, y: {self.y}")
        print(f"Šūviai: {self.suviai}")

    def pabaiga(self):
        if self.taskai < 0:
            print("Taškai baigėsi - žaidimo pabaiga.")
            return 0

tank = Tank()



while True:
    if tank.pabaiga() == 0:
        break
    tank.info()
    print()

    pasirinkimas = input("w - pirmyn \ns - atgal \na - kairėn \nd - dešinėn \ne - šauti \nx - išeiti")
    match pasirinkimas:
        case "w":
            tank.pirmyn()
        case "s":
            tank.atgal()
        case "a":
            tank.kairen()
        case "d":
            tank.desinen()
        case "e":
            tank.suvis()
        case "x":
            print("Viso gero...")
            break