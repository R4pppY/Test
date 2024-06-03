class Matrix:
    def __init__(self, data):
        self.data = data
        self.a = data[0][0]
        self.b = data[0][1]
        self.c = data[1][0]
        self.d = data[1][1]

    def __str__(self):
        return f"[{self.a} {self.b}]\n[{self.c} {self.d}]"
    
    def __mul__(self, other):
        if isinstance(other, Matrix):
            a1, b1, c1, d1 = self.a, self.b, self.c, self.d
            a2, b2, c2, d2 = other.a, other.b, other.c, other.d

            new_a = a1 * a2 + b1 * c2
            new_b = a1 * b2 + b1 * d2
            new_c = c1 * a2 + d1 * c2
            new_d = c1 * b2 + d1 * d2

            return Matrix([[new_a, new_b], [new_c, new_d]])
        else:
            raise ValueError("Operasi perkalian hanya didukung untuk tipe objek Matrix")
        
matrix1 = Matrix([[7, 2], [3, 4]])
matrix2 = Matrix([[]])
        
    


    



        