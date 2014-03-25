# x = [['w', 'w', 'w'], ['o', 'o', 'w'], ['o', 's', 'w']]

# for i in x:
#     for j in range(len(i)):
#         if i[j] == "s" :
#             i[ j] = "SH"
# print(x)


# ['w', 'w', 'w']
# ['o', 'o', 'w']
# ['o', 's', 'w']

def new_direction(move):

    x = [['w', 'w', 'w'], ['o', 'o', 'w'], ['o', 's', 'w']]
    max_path = 2
    UpDown = 2
    LeftRight = 1
    position = x[UpDown][LeftRight]

    if move == "right" and x[UpDown][LeftRight + 1] != "o" and 0 < LeftRight < max_path:

        LeftRight += 1
        position = x[UpDown][LeftRight]
        print("possition updated")


    elif move == "left" and x[UpDown][LeftRight - 1] != "o" and 0 < LeftRight < max_path:

        position = x[UpDown][LeftRight - 1]
        LeftRight -= 1
        print("possition updated")

    elif move == "up" and x[UpDown - 1][LeftRight] != "o" and 0 < UpDown < max_path:
        UpDown -= 1
        position = x[UpDown][LeftRight]
        print("possition updated")


    elif move == "down" and x[UpDown + 1][LeftRight] != "o" and 0 < UpDown < max_path:
        UpDown += 1
        position = x[UpDown][LeftRight]
        print("possition updated")

    else:
        print("illigal move, try different direction")

    return position


def main():
    print(new_direction("right"))


if __name__ == '__main__':
    main()
