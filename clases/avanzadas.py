class Avanzadas:
    def __init__(self):
        self.n1 = 0
        self.n2 = 0
    
    def leer_numeros(self):
        while True:
            try:
                self.n1 = float(input("\nPrimer número: "))
                break
            except Exception:
                print("Error de captura, volver a intentarlo")
                continue
        while True:
            try:
                self.n2 = float(input("Segundo número: "))
                break
            except Exception:
                print("Error de captura, volver a intentarlo")
                continue
            
    def potencia(self):
        return self.n1 ** self.n2
    
    def resultado(self, resultado):
        print(f"El resultado es: {resultado}")
        with open("resultado_avanzadas.dat", "a") as archivo:
            archivo.write("\nEl resultado es: " + str (resultado) + "\n")