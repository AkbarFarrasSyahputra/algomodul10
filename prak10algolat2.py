def sort_data(data, n=None): 
    if n is None:
        n = len(data)
    if n == 1:
        return
    for i in range(n - 1):
        if data[i] > data[i + 1]:
            data[i], data[i + 1] = data[i + 1], data[i]
    sort_data(data, n - 1)

def search_data(data, target, start, end): 
    if start > end:
        return -1
    mid = (start + end) // 2
    if data[mid] == target:
        return mid
    elif data[mid] > target:
        return search_data(data, target, start, mid - 1)
    else:
        return search_data(data, target, mid + 1, end)

data = [87, 56, 34, 23, 89, 15, 2, 200, 28, 31]
target = int(input("Masukkan angka yang dicari: "))
print("Data sebelum diurutkan:", data)

sort_data(data)
print("Data setelah diurutkan:", data)

result = search_data(data, target, 0, len(data) - 1)
if result != -1:
    print(f"Angka ditemukan pada urutan ke-{result + 1}")
else:
    print("Angka tidak ditemukan.")
