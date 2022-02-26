def function():
  print ('enter')

print((lambda x:x**2 + 5*x +4)(-4))
print("dog")

def function1(named_arg, *dogs):
   print(named_arg)
   print(dogs)
function1(1, 2, 3, 4, 5)

def my_func(x, y=7, *args,**kwargs):
  print(x)
  print(y)
  print(args)
  print(kwargs)
my_func(2, 4, 5, 6, a=7, b=8)

numbers = (1, 2, 3)
a, b, c = numbers
print(a)
print(b)
print(c)

a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(d)

x=6
y=5 if x>=3 else 88
print(y)

_x = 1
st = 'logout' if _x == 1 else 'login'
print(st)
