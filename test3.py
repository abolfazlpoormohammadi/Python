import math

def masahat_d(r):
    return math.pi * r ** 2
shoa = float(input("شعاع دایره را وارد کنید: "))
masahat = masahat_d(shoa)
print("مساحت دایره برابر است با:", masahat)

#-----------------------------------------------------
def formul_1(a,d,c):
    return a/d+c
a =float(input("عدد اول را وارد کنید"))
d =float(input("عدد دوم را وارد کنید"))
c =float(input("عدد سوم را وارد کنید"))
print(formul_1(a,d,c))
#----------------------------------------------------
_a =float(input("عدد اول را وارد کنید"))
_b =float(input("عدد اول را وارد کنید"))
_x =float(input("عدد اول را وارد کنید"))
y=((_b*_x)/(_a/_x))
print("جواب برابر است با",y)
