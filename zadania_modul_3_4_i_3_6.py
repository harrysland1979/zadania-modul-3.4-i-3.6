liczby_z_kapelusza = [1, 2, 3, 4, 5]

liczby_z_kapelusza[len(liczby_z_kapelusza) // 2] = int(input("Podaj liczbę całkowitą: "))

print(liczby_z_kapelusza)

liczby_z_kapelusza.pop()

print(liczby_z_kapelusza)

print(len(liczby_z_kapelusza))

beatles = []

print(beatles)

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

print(beatles)

nowi_czlonkowie = ["Stu Sutcliffe", "Pete Best"]
for muzyk in nowi_czlonkowie:
    beatles.append(muzyk)

print(beatles)

nowi_czlonkowie = ["Stu Sutcliffe", "Pete Best"]
for muzyk in nowi_czlonkowie:
    del beatles[beatles.index(muzyk)]

print(beatles)

beatles.insert(3, "Ringo Starr")

print(beatles)

print("The Fab", len(beatles))

moja_lista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
unikalne_liczby = []

for liczba in moja_lista:
    if liczba not in unikalne_liczby:
        unikalne_liczby.append(liczba)
        moja_lista = unikalne_liczby

print("Lista tylko z unikalnymi elementami:")
print(moja_lista)