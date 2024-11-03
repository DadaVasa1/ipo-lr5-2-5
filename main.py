x = input("Введите строку: ")
count = 0

for char in x:
  if char == 'и':
    count += 1

print("В строке буква \"и\" встречается", count, "раз")
