class Estadisticas:
    def calcular(self, cadena):
        if cadena == "":
            return [0, None]
        elif "," in cadena:
            numeros = cadena.split(",")
            return [len(numeros)]
        else:
            return [1]