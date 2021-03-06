import showRepresentation
import copy

class array:
  """
  Array class
  """

  def __init__(self, v):
    self.vector = v
    self.l = len(v)

  #Show vector (Raw)
  def __repr__(self):
    return showRepresentation.vector(self, True)

  #            (With print)
  def __str__(self):
    return showRepresentation.vector(self)

  #Get and set
  def __getitem__(self,index):
    return self.vector[index]

  def __setitem__(self,index,value):
    self.vector[index] = value
    return

  #Length of vector
  def __len__(self):
    return len(self.vector)
  
  #Math Operations
  add = lambda x,y: x+y
  sub = lambda x,y: x-y
  mul = lambda x,y: x*y
  div = lambda x,y: x/y
  fdiv = lambda x,y: x//y
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

  @operations(fdiv)
  def __floordiv__(self, other):
    return

  @operations(fdiv, True)
  def __rfloordiv__(self, other):
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

  def __divmod__(self, other):
    division = []
    module = []
    if type(other) != array:
      other = array([other])
    for i in range(max(len(self.vector),len(other.vector))):
      division.append(array.div(self.vector[i%self.l],other.vector[i%other.l]))
      module.append(array.mod(self.vector[i%self.l],other.vector[i%other.l]))
    return [array(division), array(module)]

  #Matrix Multiplication
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
    
  def __lshift__(self, other):
    if type(other) != int:
      raise Exception("This function only works with an int")
    else:
      return self.vector[other%self.l:]+self.vector[:other%self.l]
    
  def __rshift__(self,other):
    if type(other) != int:
      raise Exception("This function only works with an int")
    else:
      return self.vector[self.l-other%self.l:]+self.vector[:self.l-other%self.l]

  def __abs__(self):
    return array([abs(self[i]) for i in range(self.l)])
  def __version__(self):
    return "This library was created for ARINS project, January 2021"

####################
#START MATRIX CLASS#
####################

class matrix:
  """Matrix class"""
  def __init__(self, mat):
    self.mat = mat
    self.rows = self.len()[0]
    self.columns = self.len()[1]

  #Get and Set
  def __getitem__(self,index):
    return self.mat[index]

  def __setitem__(self,index,value):
    self.mat[index] = value
  
  def __len__(self):
    raise Exception("This function is unavailable, use insted len method")

  def len(self):
    return (len(self.mat), len(self.mat[0]))

  def col(self, ind):
    if type(ind) == int:
      return [self.mat[i][ind%self.columns] for i in range(self.rows)]
    if type(ind) == list or type(ind) == range:
      return array([[self.mat[i][j%self.columns] for i in range(self.rows)] for j in ind])

  def row(self, ind):
    if type(ind) == int:
      return self.mat[ind%self.len()[0]]
    if type(ind) == list or type(ind) == range:
      return array([self.mat[i%self.len()[0]] for i in ind])

  def __str__(self):
    return showRepresentation.matrix(self)

  def __repr__(self):
    return showRepresentation.matrix(self, True)

  #Math Operations
  adds = lambda x,y: x+y
  subs = lambda x,y: x-y
  muls = lambda x,y: x*y
  divs = lambda x,y: x/y
  fdivs = lambda x,y: x//y
  mods = lambda x,y: x%y
  exps = lambda x,y: x**y

  def AddOperations(ope):
    def function(func):
      def wrapper(self, other):
        if self.len() != other.len():
          raise Exception("Two matrices must have the same shape to be added, if you want to add an int or a float to all elements use the sum method")
        else:
          return matrix([[ope(self.mat[i][j], other.mat[i][j]) for j in range(self.columns)] for i in range(self.rows)])
      return wrapper
    return function
  
  def ProductOperations(ope):
    def function(func):
      def wrapper(self, other):
        if self.columns != other.rows:
          raise Exception("The columns in the first matrix must be the same as the rows in the second")
        product = [[0 for i in range(other.columns)] for j in range(self.rows)]
        for i in range(self.rows):
          for j in range(other.columns):
            for k in range(self.columns):
              product[i][j] = product[i][j] + ope(self.mat[i][k], other.mat[k][j])
              product[i][j] = round(product[i][j],4)
        return matrix(product)
      return wrapper
    return function

  @ AddOperations(adds)
  def __add__(self, other):
    return
  
  @ AddOperations(subs)
  def __sub__(self, other):
    return
  
  @ ProductOperations(muls)
  def __mul__(self, other):
    return
  
  @ ProductOperations(muls)
  def __matmul__(self, other):
    return

  @ AddOperations(mods)
  def __mod__(self, other):
    return
  
  @ AddOperations(exps)
  def __pow__(self, other):
    return

  def __truediv__(self, other):
    return matrix(self.mat) * other.inv()

  def operations(ope):
    def function(func):
      def wrapper(self, value):
        return matrix([[round(ope(self.mat[j][i], value), 4) for i in range(self.rows)] for j in range(self.columns)])
      return wrapper
    return function
  
  @operations(adds)
  def sum(self, value):
    return

  @operations(subs)
  def sub(self, value):
    return

  @operations(muls)
  def mul(self, value):
    return

  @operations(divs)
  def div(self, value):
    return

  @operations(fdivs)
  def fdiv(self, value):
    return

  @operations(mods)
  def mod(self, value):
    return

  @operations(exps)
  def pow(self, value):
    return

  def det(self):
    resMat = copy.copy(self.mat)
    for i in range(self.rows):
        for j in range(i+1, self.rows):
            factor = resMat[j][i] / resMat[i][i]

            for k in range(self.rows):
                resMat[j][k] = resMat[j][k] - factor * resMat[i][k]
    product = 1
    for i in range(self.rows):
        product *= resMat[i][i]
    
    return round(product,4)

  def transpose(self):
    resMat = copy.copy(self.mat)
    return matrix([[resMat[i][j] for i in range(self.rows)] for j in range(self.columns)])
  
  def cancel(self, row, column):
    rows = list(range(self.rows))
    rows.pop(row)
    columns = list(range(self.columns))
    columns.pop(column)
    return matrix([[self.mat[j][i] for i in columns] for j in rows])

  def adj(self):
    resMat = create(self.rows, self.columns)
    for i in range(self.rows):
      for j in range(self.columns):
        noCancel = self.cancel(i,j)
        resMat[i][j] = (-1)**(i+j)*(noCancel.det())
    return resMat
  
  def inv(self):
    return ((self.adj()).transpose()).div(self.det())

#Create matrix
def create(rows, columns, content = 0):
  r = []
  for i in range(rows):
    r.append([content for j in range(columns)])
  return matrix(r)




