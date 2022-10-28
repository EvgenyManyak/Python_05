# 3. Напишите программу, удаляющую из текста все слова, содержащие "абв".

input_str = 'Мы очень оченьабв неабв любим Питон!'.split()
smb = 'абв'
print(input_str)
# print(' '.join([word for word in input_str if smb not in word]))
print(' '.join(list(filter(lambda word: smb not in word, input_str))))
