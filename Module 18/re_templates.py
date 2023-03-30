text = "Even if they are djinns, I will get djinns that can outdjinn them."
result_1 = re.findall(r"\b[aAeEiIoOuUyY]\w*", text)
print("Слова на гласную:", result_1)
result_2 = re.findall(r"\b[^aAeEiIoOuUyY\W]\w*", text)
print("Слова на любой символ, кроме гласной:", result_2)