class Estadisticas:
    def calcular(self, cadena):
        if cadena == "":
            return [0, None, None, None]
        elif "," in cadena:
            numeros = cadena.split(",")

            minimo = int(numeros[0])
            maximo = int(numeros[0])
            promedio = 0
            for num in numeros:
                inum = int(num)
                if (inum < minimo):
                    minimo = inum
                if (maximo < inum):
                    maximo = inum
                promedio += inum

            promedio /= len(numeros)

            return [len(numeros), minimo, maximo, promedio]
        else:
            return [1, int(cadena), int(cadena), int(cadena)]