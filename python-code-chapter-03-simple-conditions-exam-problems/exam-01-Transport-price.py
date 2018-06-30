#01.Transport-price-01.png

distance = int(input())
dayOrNight = input()

#01.Transport-price-02.png

price = 0.00

#01.Transport-price-03.png

taxiRate = 0.00

#01.Transport-price-04.png

if dayOrNight == 'day':
    taxiRate = 0.79
else:
    taxiRate = 0.90

#01.Transport-price-05.png

if distance < 20:
    price = 0.70 + distance * taxiRate
elif distance < 100:
    price = distance * 0.09
else:
    price = distance * 0.06

#01.Transport-price-06.png

print(price)

