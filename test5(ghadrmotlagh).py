import math

#کدی که قدر مطلق یه عدد را برگرداند

adad=(float(input("enter your number :")))
def ghadre_motlagh(number):
    if number >= 0:
        return number
    else:
        return -number
print("your number :",ghadre_motlagh(adad))


#------------------------------------------------------
print("سوال 2")

def custom_function(x):
    if 0 < x <= 1:
        return x
    else:
        return math.exp(-x)

x = float(input("لطفاً یک عدد وارد کنید: "))
result = custom_function(x)
print("نتیجه:", result)
