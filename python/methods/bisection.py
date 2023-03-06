def bissecao(f, a, b, prec):
    """
    f -> função analisada
    a -> início do intervalo
    b -> fim do intervalo
    prec -> precisão
    """
    if f(a) * f(b) > 0:
        raise ValueError("A função não muda de sinal no intervalo dado.")
    i = 0
    while b - a > prec:
        i += 1
        c = (a + b) / 2
        if f(c) == 0:
            print(f"iterações: {i}")
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