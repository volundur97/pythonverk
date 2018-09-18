maxp = 10
minp = 1
stadur = 0
nuverandi_stadur = ""


def move_car(move_s, min_pos, max_pos, now_pos):
    stada = 0
    if move_s == 'r' and now_pos < max_pos:
        stada = now_pos +1
    elif move_s == 'r' and now_pos == max_pos:
        stada = max_pos
    elif move_s == 'l' and now_pos > min_pos:
        stada = now_pos -1
    elif move_s == 'l' and now_pos == min_pos:
        stada = now_pos
    return stada

def print_texti():
    print("l - for moving left")
    print("r - for moving right")
    print("Any other letter for quitting")
    return

stadur= int(input("Input a position between 1 and 10: "))
print_texti()
nuverandi_stadur =input("Input your choice: ")
while nuverandi_stadur == 'r' or nuverandi_stadur == 'l':
    stadur = move_car(nuverandi_stadur, minp, maxp, stadur)
    print("New position is: {}".format(str(stadur)))
    print_texti()
    nuverandi_stadur =input("Input your choice: ")
print("New position is: {}".format(str(stadur)))
