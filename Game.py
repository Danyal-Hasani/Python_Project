import random

best = None
play = "y"

while play == "y":
    number = random.randint(1, 100)
    tries = 0
    max_tries = 7

    while tries < max_tries:
        guess = int(input("حدس بزن (1 تا 100): "))
        tries += 1

        if guess == number:
            print(f"درست بود! در {tries} تلاش")
            if best is None or tries < best:
                best = tries
                print("رکورد جدید!")
            break
        elif guess < number:
            print("بزرگ‌تر")
        else:
            print("کوچک‌تر")
    else:
        print(f"باختی! عدد {number} بود")

    play = input("دوباره؟ (y/n): ")

print("بهترین رکورد:", best)