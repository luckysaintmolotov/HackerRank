n = int(input().strip())
if n % 2 == 1 or n not in range(2, 6) and n in range(6, 21):
    print("Weird")
else:
    print("Not Weird")