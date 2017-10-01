class Estadisticas:
    def calcular(self, cadena):
        if cadena == "":
            return [0, None, None, None]
        elif "," in cadena:
            numeros = cadena.split(",")

            minimo = int(numeros[0])
            maximo = int(numeros[0])
            for num in numeros:
                if (int(num) < minimo):
                    minimo = int(num)
                if (maximo < int(num)):
                    maximo = int(num)

            return [len(numeros), minimo, maximo]
        else:
            return [1, int(cadena), int(cadena)]