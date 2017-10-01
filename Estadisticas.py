class Estadisticas:
    def calcular(self, cadena):
        if cadena == "":
            return [0, None]
        elif "," in cadena:
            numeros = cadena.split(",")
            if(int(numeros[0]) <= int(numeros[1])):
                return [len(numeros), int(numeros[0])]
            else:
                return [len(numeros), int(numeros[1])]
        else:
            return [1, int(cadena)]