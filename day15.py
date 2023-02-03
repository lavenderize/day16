pokemons = ["피카츄", "라이츄", "파이리", "꼬부기", "이상해씨"]


def add_data(pokemons) :
    pokemons.append(None)


def insert_data(idx, pokemons):
    if idx < 0 or idx > len(pokemons):
        print("Out of range!")
        return

    pokemons.append(None)

    for i in range(len(pokemons) - 1, idx, -1):
        pokemons[i] = pokemons[i - 1]
        pokemons[i - 1] = None

    pokemons[idx] = pokemons


def delete_data(idx):
    if idx < 0 or idx > len(pokemons):
        print("Out of range!")
        return

    len_pokemons = len(pokemons)
    pokemons[idx] = None

    for i in range(len_pokemons - idx):
        pokemons.pop()  # 반복하면서 제거 수행

#    for i in range(idx, len_pokemons):
#        # pokemons[i - 1] = pokemons[i]
#        # pokemons[i] = None
#
#        del (pokemons[idx])


# insert_data(1, "치코리타")
# print(pokemons)

delete_data(2)
print(pokemons)



