def slope_style_score(scores):

    scores.sort()
    new_score_list = []

    for i in range(1, len(scores) - 1):

        new_score_list.append(scores[i])

    return round((sum(new_score_list) / len(new_score_list)), 2)


def main():

    print(slope_style_score([94, 95, 95, 95, 90]))
    # 94.66
    print(slope_style_score([60, 70, 80, 90, 100]))
    # 80.0
    print(slope_style_score([96, 95.5, 93, 89, 92]))
    # 93.5

if __name__ == '__main__':
    main()
