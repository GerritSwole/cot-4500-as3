## Question 1  Euler Method

def EulerMethod(f, a, b, f0, n):
    h = (b - a)/n
    a = a
    f0 = f0
    b = b
    for i in range(n):
        f0 = f0 + h*f(a, f0)
        a = a + h
    return print(f0)

def f(t,y):
    return t - y**2

EulerMethod(f,1,4,1,5)


## Question 2 Runge-Kutta Method

def RungeKuttaMethod(f, a, b, f0, n):
    h = (b - a)/n
    a = a
    b = b
    f0 = f0
    for i in range(n):
        k1 = h*f(a, f0)
        k2 = h*f(a + h/2, f0 + k1/2)
        k3 = h*f(a + h/2, f0 + k2/2)
        k4 = h*f(a + h, f0 + k3)
        f0 = f0 + (k1 + 2*k2 + 2*k3 + k4)/6
        a = a + h
    return print(f0)

def f(t,y):
    return t - y**2

RungeKuttaMethod(f,1,4,1,5)
    