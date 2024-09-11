from moore_automatas import Moore
import re


parse = Moore


input_values = [

    "variable = 093564",
    "variable = 011101",
    "variable = 12312001",
    "variable = 657",
    "string = 1420",
    "variable 0110",
    "variable = 16221A",
    "variable=1010"

]

for item in input_values:

    tokens = re.findall(r'[A-Za-z_]+|[^\s\w]|[0-9]', item)

    print('\n'+ item +'\n')
    parse.Moore_Machine(tokens)
    print("---------------------------------------------")
