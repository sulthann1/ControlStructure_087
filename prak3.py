n = int (input ("Masukan nilai n untuk batas deret Fibonacci :"))

a, b = 0,1

print ("deret fibonacci hingga", n, ":")
while a <= n:
    print (a, end="")
    a,b = b, a + b