import bisection as bi
import newton as ne
import secant as se
import falsePosition as fp

prec = 0.001
f = lambda x: x**3 - 9*x + 3
fd = lambda x: 2*x**2 - 9

print("Bisseção")
raiz = bi.bissecao(f, 0, 1, prec)
print(raiz)

print("*-"*20)

print("Falsa Posição")
raiz = fp.falsePosition(f, 0, 1, prec)
print(raiz)

print("*-"*20)

raiz = se.secant(f, 0, 1, prec)
print(raiz)

print("*-"*20)

print("Newton")
raiz = ne.newton(f, fd, 0, prec)
print(raiz)
