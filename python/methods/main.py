import bisection as bi
import newton as ne
import secant as se
import falsePosition as fp

prec = 0.001

raiz = bi.bissecao(bi.f, 0, 1, prec)
print(raiz)

print("*-"*20)

raiz = ne.newton(ne.f, ne.fd, 0, prec)
print(raiz)

print("*-"*20)

raiz = se.secant(se.f, 0, 1, prec)
print(raiz)

print("*-"*20)

raiz = fp.falsePosition(fp.f, 0, 1, prec)
print(raiz)