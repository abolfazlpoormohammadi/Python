import math

def show_menu():
    print("\n--- ماشین حساب پیشرفته ---")
    print("عملیات‌های موجود:")
    print("0. باقی مانده (%)")
    print("1. جمع (+)")
    print("2. تفریق (-)")
    print("3. ضرب (*)")
    print("4. تقسیم (/)")
    print("5. توان (x^y)")
    print("6. جذر (√x)")
    print("7. لگاریتم (log x)")
    print("8. سینوس (sin x)")
    print("9. کسینوس (cos x)")
    print("10. تانژانت (tan x)")
    print("11. خروج")

def get_number(prompt="عدد را وارد کنید: "):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("ورودی نامعتبر است. لطفاً یک عدد وارد کنید.")

def calculator():
    while True:
        show_menu()
        choice = input("انتخاب شما: ")
        if choice == '0':
            a = get_number("عدد اول: ")
            b = get_number("عدد دوم: ")
            print("نتیجه: ", a % b)

        elif choice == '1':
            a = get_number("عدد اول: ")
            b = get_number("عدد دوم: ")
            print("نتیجه: ", a + b)

        elif choice == '2':
            a = get_number("عدد اول: ")
            b = get_number("عدد دوم: ")
            print("نتیجه: ", a - b)

        elif choice == '3':
            a = get_number("عدد اول: ")
            b = get_number("عدد دوم: ")
            print("نتیجه: ", a * b)

        elif choice == '4':
            a = get_number("عدد اول: ")
            b = get_number("عدد دوم: ")
            if b == 0:
                print("خطا: تقسیم بر صفر مجاز نیست.")
            else:
                print("نتیجه: ", a / b)

        elif choice == '5':
            a = get_number("پایه: ")
            b = get_number("توان: ")
            print("نتیجه: ", math.pow(a, b))

        elif choice == '6':
            a = get_number("عدد: ")
            if a < 0:
                print("خطا: جذر عدد منفی مجاز نیست.")
            else:
                print("نتیجه: ", math.sqrt(a))

        elif choice == '7':
            a = get_number("عدد (بزرگ‌تر از 0): ")
            if a <= 0:
                print("خطا: لگاریتم فقط برای اعداد مثبت تعریف شده.")
            else:
                print("نتیجه: ", math.log10(a))

        elif choice == '8':
            a = get_number("درجه زاویه: ")
            rad = math.radians(a)
            print("نتیجه: ", math.sin(rad))

        elif choice == '9':
            a = get_number("درجه زاویه: ")
            rad = math.radians(a)
            print("نتیجه: ", math.cos(rad))

        elif choice == '10':
            a = get_number("درجه زاویه: ")
            rad = math.radians(a)
            print("نتیجه: ", math.tan(rad))

        elif choice == '11':
            print("خروج از برنامه. موفق باشید!")
            break

        else:
            print("گزینه نامعتبر است. لطفاً دوباره تلاش کنید.")
        print("___________________________________________________")
calculator()