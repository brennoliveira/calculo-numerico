def falsePosition(f, a, b, prec):
  """
  f -> função analisada
  a -> início do intervalo
  b -> fim do intervalo
  prec -> precisão
  """
  if (f(a) * f(b) > 0):
    raise ValueError("A função não muda de sinal no intervalo dado.")

  i = 0
  fa = f(a)
  fb = f(b)
  while abs(b - a) > prec:
    i += 1
    x = (a * fb) - (b * fa) / (fb - fa)
    fx = f(x)
    if abs(fx) < prec:
      print(f"iterações: {i}")
      return x
    elif fa * fx < 0:
      b = x
      fb = fx
    else:
      a = x
      fa = fx
      
  print(f"iterações: {i}")
  return x


def f(x):
  """
  Função a ser analisada.
  """
  return x**3 - 9*x + 3