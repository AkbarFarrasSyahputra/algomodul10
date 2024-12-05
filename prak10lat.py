data = [82, 22, 34, 21, 5, 20, 47, 18]
angka = int(input('Angka yang dicari: '))
21
print('Sebelum bubble sort:', data)

n = len(data)
for i in range(n-1):
    for j in range(n-i-1):
        if data[j] > data[j+1]:
            data[j], data[j+1] = data[j+1], data[j]

print('Hasil bubble sort:', data)

a = 0
b = len(data) - 1
found = False

while a <= b:
    mid = (a + b) // 2
    if data[mid] == angka:
        print(f'Angka {angka} ditemukan pada indeks {mid}')
        found = True
        break
    elif data[mid] < angka:
        a = mid + 1
    else:
        b = mid - 1

if not found:
    print(f'Angka {angka} tidak ditemukan')
