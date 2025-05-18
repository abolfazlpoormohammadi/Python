def revtxt(text):
    revstr1 =("")
    for harf in text:
       revstr1 = harf + revstr1
    return revstr1

reversstring1 = input(str(":متن خود را وارد کنید:"))

istr = revtxt(reversstring1)

print("strig orginal: " , reversstring1)
print("revers string:", istr)