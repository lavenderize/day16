pokemons = ["피카츄", "라이츄", "파이리", "꼬부기", "이상해씨"]


def add_data(pokemon) :
    pokemons.append(None)


def insert_data(idx, pokemon):
    if idx < 0 or idx > len(pokemon):
        print("Out of range!")
        return

    pokemons.append(None)

    for i in range(len(pokemons) - 1, idx, -1):
        pokemons[i] = pokemons[i - 1]
        pokemons[i - 1] = None

    pokemons[idx] = pokemon

insert_data(1, "치코리타")
insert_data(3, "잠만보")
print(pokemons)



