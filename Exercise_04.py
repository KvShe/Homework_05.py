# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
def encoding(text):
    res = ''
    i = 0
    while i < len(text):
        count = 1
        while i + 1 < len(text) and text[i] == text[i + 1]:
            count += 1
            i += 1
        res += str(count) + text[i]
        i += 1
    return res


file_1 = 'Exercise_05_start.txt'
with open(file_1, 'r') as f:
    string = f.readline()

result = encoding(string)

file_2 = 'Exercise_05_end.txt'
with open(file_2, 'w') as f:
    f.writelines(result)
