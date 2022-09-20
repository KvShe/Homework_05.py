# Напишите программу, удаляющую из текста все слова, содержащие ""абв""
string = 'Мы неабв очень любим Питон иабв абв абв'
substring = 'абв'
string = string.split()
lst = [item for item in string if substring not in item]
print(*lst)
