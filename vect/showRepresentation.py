def vector(self, raw = False):
    return "array({})".format(self.vector) if raw else "{}".format(self.vector)

def matrix(self, raw = False):
    if raw:
        return "{}".format(self.mat) if raw else "{}".format(self.mat)
    else: 
        return "\n".join([str(self.mat[i]) for i in range(self.rows)])