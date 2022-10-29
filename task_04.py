# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных

with open('file_task_04_01.txt', 'w') as file:
    file.write(input('Напишите текст необходимый для сжатия: '))
with open('file_task_04_01.txt', 'r') as file:
    my_txt = file.readline()
    txt_comprehensive = my_txt.split()

print(my_txt)

def file_encoding(txt):
    encoding = ''
    prev_char = ''
    count = 1
    if not txt:
        return ''

    for char in txt:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
        return encoding


txt_comprehensive = file_encoding(my_txt)

with open('file_task_04_02.txt', 'w') as file:
    file.write(f'{txt_comprehensive}')
print(txt_comprehensive)