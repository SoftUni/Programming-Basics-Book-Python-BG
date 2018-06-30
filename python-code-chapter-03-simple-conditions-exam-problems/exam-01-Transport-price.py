distance = int(input())
dayOrNight = input()

price = 0.00
taxiRate = 0.00

if dayOrNight == 'day':
    taxiRate = 0.79
else:
    taxiRate = 0.90

if distance < 20:
    price = 0.70 + distance * taxiRate
elif distance < 100:
    price = distance * 0.09
else:
    price = distance * 0.06

print(price)

