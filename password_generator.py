# https://interactivechaos.com/en/python/function/stringprintable
import string
import random
# strip to remove whitespace( \t\n\r\x0b\x0c) from the end of the string
# strip para remover whitespace( \t\n\r\x0b\x0c) do fim da string
characters = string.printable.strip()
print("available characters")
print(characters)
unwanted = input("\nType characters to remove, Enter to skip. \n")

# length od the password
# tamanho da senha
length = int(input("Length of the password\n"))
password = ""
unwanted_characters: dict = {}

# adicionado caracteres  indesejado no dict
# add unwanted  characters to dict
for char in unwanted:
    unwanted_characters[char] = ""

# remove characters contained in the dict
# remover caracteres que estão do dict
replacements = str.maketrans(unwanted_characters)
clean_chars = characters.translate(replacements)

# create password with length informed
# criando senha com o tamanho informado
for c in range(length):
    password += random.choice(clean_chars)

print("Your password")
print(password)
