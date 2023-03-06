import bisection as bi
import newton as ne
import secant as se

raiz = bi.bissecao(bi.f, 0, 1, 0.001)
print(raiz)

print("*-"*20)

raiz = ne.newton(ne.f, ne.fd, 0, 0.001)
print(raiz)

print("*-"*20)

raiz = se.secant(se.f, 0, 1, 0.001)
print(raiz)