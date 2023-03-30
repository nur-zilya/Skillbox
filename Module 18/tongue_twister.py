import re


text = "How much wood would a woodchuck chuck if a woodchuck could chuck wood?"

print("Поиск шаблона в начале строки: ", re.match(r'wo', text))
print("Поиск первого найденного совпадения по шаблону: ", re.search(r'wo', text))
print("Содержимое найденной подстроки: ", re.search(r'wo', text).group(0))
print("Начальная позиция: ", re.search(r'wo', text).start())
print("Конечная позиция: ", re.search(r'wo', text).end())
print("Список всех упоминаний шаблона: ", re.findall(r'wo', text))
print("Текст после замены: ", re.sub(r'wo', 'ЗАМЕНА', text))