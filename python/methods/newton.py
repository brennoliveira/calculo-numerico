def newton(f, fd, x, prec):
  i = 0
  while abs(f(x)) > prec:
    i+= 1
    
    if fd(x) == 0:
      raise ValueError("Derivada nula")
    x = x - f(x) / fd(x)
  
  print(f"iterações: {i}")
  return x



def f(x):
  return x**3 - 9*x + 3

def fd(x):
  return 3*x**2 - 9

# raiz = newton(f, fd, 0, 0.001)
# print(raiz)