from numpy.testing.print_coercion_tables import print_new_cast_table

lista_frutas = {"Maça","Morango", "va"}

#listas_frutas[0] = "Maça"
#listas_frutas[1] = "Morango"
#listas_frutas[2] = "Uva"

lista_frutas.append("Jabuticaba")
print(listas_frutas[-1])
print()

tamanho = len(lista_frutas)

for i in range(tamanho):
    print(lista_frutas[i])

print()

for fruta in lista_frutas:
    print(fruta)

print()

msg = "Oi fulano"

for i in range(len(msg)):
    print(msg[i])