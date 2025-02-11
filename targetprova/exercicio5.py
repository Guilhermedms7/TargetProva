# 5) Inverter uma string
def inverter_string(s):
    invertida = ""
    for char in s:
        invertida = char + invertida
    return invertida

string_teste = "Python"
print(f"5) String invertida: {inverter_string(string_teste)}")
