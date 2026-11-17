n = int(input("عدد 0 یا 1 را وارد کنید: "))
while n != 0 and n != 1:
    print("ورودی نامعتبر!")
    n = int(input("دوباره وارد کنید: "))

print(n == 1)