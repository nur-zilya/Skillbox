import re

txt = "How much \wwood+?, would a \wwood+?chuck \dwwood+, chuck if a \wwood+?,chuck could chuck \wwood?"

example = re.findall(r"wwood\+\?", txt)
print(example)