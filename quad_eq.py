#program to get quare root of given eqaution
a,b,c = int(input("Ax^2 = ")),int(input("bx = ")),int(input("c ="))
d=((b)**2 - (4*a*c))**(1/2)
e,f=(-b+d),(-b-d)
g=(e/(2*a))
h=(e/(2*a))
print("first root =", g)
print("second root =",h)