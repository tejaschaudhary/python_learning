print("Hello World")
print("Hello"+" World")

var = 'Hello World'

print(var[:5])
print(var[6:])

var1 = 'Hello'*5
lst = [i for i in range(10)]
print(lst)

lst1 = lst + lst
print(lst1)

lst_squares =list(map(lambda x: x**2, lst))
print(lst_squares)

def cube(n):
	return n*n*n

lst_cube = list(map(cube, lst))
print(lst_cube+"kjskfsjkfhsdjkhfsdjkfh")
print("Made some changes)
