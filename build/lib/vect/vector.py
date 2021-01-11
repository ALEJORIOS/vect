from matMul import matMultiplication
class array:
  """
  Array class
  """

  def __init__(self, v, ismat = False):
    self.vector = v
    self.l = len(v)
    try:
      self.w = len(v[0])
      ismat = True
    except:
      self.w = 1
    self.ismat = ismat
    self.types = [type(self.vector[i]) for i in range(self.l)]
    if all(list == i for i in self.types):
      self.vector = [array(i) for i in self.vector]
      self.ismat = True
    if all(array == i for i in self.types):
      self.ismat = True
  def __repr__(self):
    if self.ismat:
      return "array({})".format("\n".join([str(i) for i in self.vector]))
    return "array({})".format(self.vector)
  def __str__(self):
    if self.ismat:
      return "{}".format("\n".join([str(i) for i in self.vector]))
    else:
      return "{}".format(self.vector)
  def __getitem__(self,index):
    return self.vector[index]
  def __setitem__(self,index,value):
    self.vector[index] = value
  def __len__(self):
    return len(self.vector)
  
  #Math Operations
  add = lambda x,y: x+y
  sub = lambda x,y: x-y
  mul = lambda x,y: x*y
  div = lambda x,y: x/y
  mod = lambda x,y: x%y
  exp = lambda x,y: x**y

  def operations(ope, reverse = False):
    def function(func):
        def wrapper(self, other):
            r = []
            if type(other) != array:
                other = array([other])
            for i in range(max(len(self.vector),len(other.vector))):
                if reverse:
                  r.append(ope(other.vector[i%other.l], self.vector[i%self.l]))
                else:
                  r.append(ope(self.vector[i%self.l],other.vector[i%other.l]))
            return array(r)
        return wrapper
    return function
  
  @operations(add)
  def __add__(self, other):
    return

  @operations(add, True)
  def __radd__(self, other):
    return

  @operations(sub)
  def __sub__(self, other):
    return

  @operations(sub, True)
  def __rsub__(self, other):
    return

  @operations(mul)
  def __mul__(self, other):
    return

  @operations(mul, True)
  def __rmul__(self, other):
    return

  @operations(div)
  def __truediv__(self, other):
    return

  @operations(div, True)
  def __rtruediv__(self, other):
    return

  @operations(exp)
  def __pow__(self, other):
    return

  @operations(exp, True)  
  def __rpow__(self, other):
    return

  @operations(mod)
  def __mod__(self, other):
    return

  @operations(mod, True)  
  def __rmod__(self, other):
    return

  def __matmul__(self, other):
    if self.w != other.l:
      raise Exception("The columns in the first matrix must be the same as the rows in the second")
    product = [[0 for i in range(other.w)] for j in range(self.l)]
    for i in range(self.l):
      for j in range(other.w):
        for k in range(self.w):
          product[i][j] = product[i][j] + self.vector[i][k] * other.vector[k][j]
    return product

  def __round__(self, ndigits = 2):
    return [round(i,ndigits) for i in self]
  def __bool__(self):
    return bool(self)
  def col(self, ind):
    if type(ind) == int:
      return [self.vector[i][ind] for i in range(self.l)]
    if type(ind) == list or type(ind) == range:
      return [[self.vector[i][j] for i in range(self.l)] for j in ind]
  def row(self, ind):
    if type(ind) == int:
      return self.vector[ind]
    if type(ind) == list or type(ind) == range:
      return [self.vector[i] for i in ind]
  def __version__(self):
    return "This library was created for ARINS project, January 2021"
    
