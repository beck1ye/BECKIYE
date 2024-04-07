from data import pcodes
data = 0
while True:
    code = input()
    if code in pcodes:
        data = data + 200
        print(f"Sizning hisobingizda {data} so'm mablag' mavjud!")
    elif code == "hisobim":
        print(data)
    else:
        print('Error!')
    