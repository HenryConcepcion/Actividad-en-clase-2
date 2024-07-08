"oso,perro,10,5 son animales"

palabras = "oso,perro,10,5 son animales".split(",")
oso_count = 0
for palabra in palabras:
  if palabra == palabra[::-1]:
    print(f"{palabra} es un palindromo")
  else:
    print(f"{palabra} no es un palindromo")
  if palabra.lower() == "oso":
    oso_count += 5
print(f"tenemos {oso_count} osos")
print("oso y peroo son animales")