def bissecao(f, a, b, tol):
    """
    Encontra a raiz da função f no intervalo [a, b] com tolerância de erro tol.
    """
    if f(a) * f(b) > 0:
        raise ValueError("A função não muda de sinal no intervalo dado.")
    
    while b - a > tol:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    
    return (a + b) / 2


def f(x):
  """
  Função a ser analisada.
  """
  return x**3 - 6*x**2 + 11*x - 6