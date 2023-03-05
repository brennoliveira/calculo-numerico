def bissecao(f, a, b, prec):
    """
    Encontra a raiz da função f no intervalo [a, b] com precisão prec.
    """
    if f(a) * f(b) > 0:
        raise ValueError("A função não muda de sinal no intervalo dado.")
    i = 0
    while b - a > prec:
        i += 1
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    print(f"iterações: {i}")
    return (a + b) / 2


def f(x):
  """
  Função a ser analisada.
  """
  return x**3 - 9*x + 3