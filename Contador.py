frase = input("Digite uma frase: ").lower()

vogais = "aeiou"
contagem = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
total_vogais = 0

for letra in frase:
    if letra in vogais:
        contagem[letra] += 1
        total_vogais += 1

print(f"\nQuantidade total de vogais: {total_vogais}")
print("Contagem por vogal:")
for v, qtd in contagem.items():
    print(f" - {v}: {qtd}")

vogais_encontradas = [v for v, qtd in contagem.items() if qtd > 0]
print("\nVogais encontradas:", ", ".join(vogais_encontradas) if vogais_encontradas else "Nenhuma")

if len(frase.split()) > 1:
    print("\nO texto digitado é uma frase.")
else:
    print("\nO texto digitado não é uma frase.")