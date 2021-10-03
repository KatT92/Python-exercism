class Matrix:
    def __init__(self, matrix_string):
        self.matrix = [[int(i) for i in r.split()] for r in matrix_string.split("\n")]

    def row(self, index):
        return self.matrix[index]

    def column(self, index):
        column = list(zip(*self.matrix[index]))
        return column




