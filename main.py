x = input("Введите строку: ")
x = x.lower()
count = 0

for char in x:
  if char == 'и':
    count += 1

print("В строке буква \"и\" встречается", count, "раз")
