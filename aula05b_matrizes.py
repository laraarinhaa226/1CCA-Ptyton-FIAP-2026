from numba.cuda.printimpl import print_item

musicas = [
    ["Chicago", "Michael Jackson"],
    ["Sorry", "Justin Bieber"],
    ["Judas", "Lady gaga"]
]
print(musicas[1][0])

for musica in musicas:
   for info in musica:
       print(info)

   print()

