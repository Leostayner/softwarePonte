class Elemento()

    def __init__():
        self.comprimento
        self.area
        self.cos
        self.sen


    def comprimento(self, elemento):
            xa = (self.matrizCordenadas[(self.matrizIndices[elemento - 1][1]) + 1][1])
            yb = (self.matrizCordenadas[(self.matrizIndices[elemento - 1][1]) + 1][2])
            xb = (self.matrizCordenadas[(self.matrizIndices[elemento - 1][2]) + 1][1])
            yb = (self.matrizCordenadas[(self.matrizIndices[elemento - 1][2]) + 1][2])
            return (math.sqr(math.pow(xa - xb, 2) + math.pow(ya - yb, 2))