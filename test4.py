import math
#---------------------exercise 1
print("---------------exercise 1")
def calculate_y(x, y):
    result = (x / y) * math.log(x / y)
    return result

x = int(input("Enter x :"))
y = int(input("Enter y :"))
output = calculate_y(x, y)
print(f"Result: {output}")

#---------------------exercise 2
print("---------------exercise 2")
def s(a):
    b = 1 / (1 + math.exp(-a))
    return y

a = int(input("Enter a :"))
javab = s(a)
print(f"Sigmoid Output: {javab}")

#---------------------exercise 3

print("---------------exercise 3")
def f(c):
    w = math.exp(d) / math.exp(d**2)
    return w

d = int(input("Enter d :"))
javab1 = f(d)
print(f"Result: {javab1}")


#---------------------exercise 4
print("---------------exercise 4")


def g(h):
    if h > 0:
        i = math.sqrt(h * math.log(h))
        return i
    else:
        raise ValueError("h باید بزرگتر از صفر باشد.")

h = int(input("Enter h :"))
try:
    javab2 = g(h)
    print(f"Result: {javab2}")
except ValueError as e:
    print(e)

#---------------------exercise 5

print("---------------exercise 5")

def f(j, k, k1):
    if j == 0:
        raise ValueError("j نباید صفر باشد.")
    m = (1 / j) * (k - k1)
    return m

j = 2
k = 5
k1 = 3
try:
    javab3 = f(j, k, k1)
    print(f"Result: {javab3}")
except ValueError as l:
    print(l)
    #تمرین با استفاده از ابزار هوش مصنوعی چت جی پی تی نوشته شده است
