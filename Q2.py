def verifica_letra_a(string):
    count_a = string.lower().count('a')
    
    if count_a > 0:
        return f"A letra 'a' aparece {count_a} vez(es) na string."
    else:
        return "A letra 'a' não foi encontrada na string."

texto = input("Digite algum texto: ")
print(verifica_letra_a(texto))
