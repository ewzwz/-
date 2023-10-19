print("Введите строку, в которой будет осуществляться поиск")
word = input()

print("Введите строку, которую будем искать")
comb = input()

counter = 0

for i in range(0, len(word) - len(comb) + 1):
    if word[i:i+len(comb)] == comb:
        counter += 1
        
print(f"""Количество вхождений строки "{comb}" в строку "{word}":""", counter)
