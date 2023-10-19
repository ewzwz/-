word = ''
comb = ''
while len(word) == 0 or len(comb) == 0:
    print("Введите строку, в которой будет осуществляться поиск")
    word = input()
    print("Введите строку, которую будем искать")
    comb = input()
    if len(word) == 0 and len(comb) == 0:
        print("Вы не ввели никакие строки")
    else:
        if len(word) == 0:
            print("Вы не ввели первую строку")
        else:
            print("Вы не ввели вторую строку")

counter = 0

for i in range(0, len(word) - len(comb) + 1):
    if word[i:i+len(comb)] == comb:
        counter += 1
            
print(f"""Количество вхождений строки "{comb}" в строку "{word}":""", counter)
