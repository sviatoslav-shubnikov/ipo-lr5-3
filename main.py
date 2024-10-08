with open('text.txt', 'r', encoding='utf-8') as file:
    
    list = file.read()

words= list.split()

length=len(words)
print(f'Количество слов в файле равно: {length}')