import random

choices = {"1": "سنگ", "2": "کاغذ", "3": "قیچی"}
wins = {"سنگ": "قیچی", "کاغذ": "سنگ", "قیچی": "کاغذ"}

rounds = 5
user_score = 0
pc_score = 0

for r in range(1, rounds + 1):
    print(f"\nدور {r} از {rounds}")
    print("1) سنگ  2) کاغذ  3) قیچی")

    c = input("انتخاب تو: ")
    while c not in choices:
        c = input("نامعتبره، دوباره (1 تا 3): ")

    user = choices[c]
    pc = random.choice(list(choices.values()))
    print(f"تو: {user} | کامپیوتر: {pc}")

    if user == pc:
        print("مساوی")
    elif wins[user] == pc:
        print("این دور رو بردی")
        user_score += 1
    else:
        print("این دور رو باختی")
        pc_score += 1

    print(f"امتیاز: تو {user_score} - کامپیوتر {pc_score}")

print("\n--- نتیجه نهایی ---")
if user_score > pc_score:
    print("تو برنده شدی!")
elif user_score < pc_score:
    print("کامپیوتر برد")
else:
    print("مساوی شدید")