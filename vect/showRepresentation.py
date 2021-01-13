def vector(self, raw = False):
    return "array({})".format(self.vector) if raw else "{}".format(self.vector)

def matrix(self, raw = False):
    if raw:
        return "array({})".format(self.mat) if raw else "{}".format(self.mat)
    else: 
        salida = "#".join([self.mat[i] for i in range(self.rows)])
        print(type(salida))