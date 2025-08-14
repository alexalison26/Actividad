# src/main.py

def es_palindromo(texto):
    # Eliminar espacios y pasar a minúsculas
    texto_limpio = ''.join(c.lower() for c in texto if c.isalnum())
    # Verificar si es igual al inverso
    return texto_limpio == texto_limpio[::-1]

# Programa principal
print("=== Verificador de Palíndromos ===")
frase = input("Ingrese una palabra o frase: ")

if es_palindromo(frase):
    print("✅ Es un palíndromo.")
else:
    print("❌ No es un palíndromo.")
