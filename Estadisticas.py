class Estadisticas:
    def calcular(self, cadena):
        if cadena == "":
            return [0, None, None]
        elif "," in cadena:
            numeros = cadena.split(",")

            minimo = int(numeros[0])
            for num in numeros:
                if (int(num) < minimo):
                    minimo = int(num)

            maximo = int(numeros[0])
            if( int(numeros[1]) > maximo ):
                maximo = int(numeros[1])

            return [len(numeros), minimo, maximo]
        else:
            return [1, int(cadena), int(cadena)]