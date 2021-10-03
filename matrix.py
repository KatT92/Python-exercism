class Matrix:
    def __init__(self, matrix_string):
        self.matrix = [[int(i) for i in r.split()] for r in matrix_string.split("\n")]
		
    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        return [j[index - 1] for j in self.matrix]

        

          



