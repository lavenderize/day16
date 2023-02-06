# def find_and_insert_data(pokemon, k_count) :
# 	findPos = -1
# 	for i in range(len(pokemons)):
# 		pair = pokemons[i]
# 		if k_count <= pair[1]:
# 			findPos = i
# 			break
# 	if findPos == -1:
# 		findPos = len(pokemons)
#
# 	insert_data(findPos, [pokemon, k_count])
#
#
# def insert_data(position, pokemon):
# 	if position < 0 or position > len(pokemons):
# 		print("데이터를 삽입할 범위를 벗어났습니다.")
# 		return
#
# 	pokemons.append(None)
# 	kLen = len(pokemons)
#
# 	for i in range(kLen - 1, position, -1):
# 		pokemons[i] = pokemons[i - 1]
# 		pokemons[i - 1] = None
#
# 	pokemons[position] = pokemon
#
#
#
# pokemons = [['피카츄', 300], ['꼬부기', 500], ['어니부기', 700], ['거북왕', 1000]]
#
# ## 메인 코드 부분 ##
# if __name__ == "__main__":
#
# 	while True:
# 		pokemon = input("새로운 몬스터 : ")
# 		hp = int(input("체력 : "))
# 		find_and_insert_data(pokemon, hp)
# 		print(pokemons)

class Node:
	def __init__(self):
		self.data = None
		self.link = None

	# def __repr__(self):
	# 	return f'포켓몬스터!'


def print_nodes(start):
    current = start
    if current == None :
        return
    print(current.data, end=' ')
    while current.link is not None:
        current = current.link  # 다음 노드로 이동
        print(current.data, end=' ')
    print()


def insert_nodes(find_data, insert_data):
    global memory, head, current, pre

    if head.data == find_data:  # 첫 번째 노드 삽입
        node = Node()
        node.data = insert_data
        node.link = head
        head = node
        return

    current = head
    while current.link is not None:  # 중간 노드 삽입
        pre = current
        current = current.link
        if current.data == find_data:
            node = Node()
            node.data = insert_data
            node.link = current
            pre.link = node
            return


def delete_nodes(delete_data):
    global memory, head, current, pre

    if head.data == delete_data:
        current = head
        head = head.link
        print("#첫 노드가 삭제됨#")
        del current
        return

    current = head
    while current.link is not None:
        pre = current
        current = current.link
        if current.data == delete_data:
            pre.link = current.link
            print("#중간 노드가 삭제됨#")
            del current
            return

# 삭제할 데이터를 찾지 못한 경우
    print("#삭제할 노드를 찾지 못함#")


def find_nodes(find_data):
    global memory, head, current, pre

    current = head
    if current.data == find_data:
        return current

    while current.link is not None:
        current = current.link
        if current.data == find_data:
            return current

    return Node("nameless")


memory = []
head, current, pre = None, None, None
data_Array = ["피카츄", "라이츄", "꼬부기", "파이리", "이상해"]


if __name__ == "__main__":
    node = Node()
    node.data = data_Array[0]
    head = node
    memory.append(node)

    for data in data_Array[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
#        memory.append(node)

    print_nodes(head)
    insert_nodes("피카츄", "잠만보")
    print_nodes(head)
    insert_nodes("파이리", "어니부기")
    print_nodes(head)

    delete_nodes("잠만보")
    print_nodes(head)
    delete_nodes("꼬부기")
    print_nodes(head)
    delete_nodes("고창석")
    print_nodes(head)
    print(find_nodes("파이리").data)