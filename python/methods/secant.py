def secant(f, x0, x1, prec):
  """
  f -> função analisada
  x0, x1 -> pontos iniciais
  prec -> precisão
  """
  i = 0
  fx0 = f(x0)
  fx1 = f(x1)
  x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
  while abs((x2 - x1) / x2) > prec:
    i += 1
    x0 = x1
    x1 = x2
    fx0 = fx1
    fx1 = f(x1)
    x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
    
    
  print(f"iterações: {i}")
  return x2
  
  
def f(x):
  return x**3 - 9*x + 3