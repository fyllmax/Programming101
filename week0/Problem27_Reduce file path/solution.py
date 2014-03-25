# Import


# Globals

def reduce_file_path(path):
    path = path.split("/")
    new_path = ""

    i = 0
    while i < len(path) - 1:
        if path[i + 1] == ".." and path[i + 1]:
            path[i] = ""
            path[i + 1] = ""

        elif path[i] == ".":
            path[i] = ""

        elif path[i] != "":
            new_path += "/" + path[i]
        i += 1

    if new_path == "":
        new_path = "/"

    return new_path

# Main


def main():
    print(reduce_file_path("/"))
    print(reduce_file_path("/srv/../"))
    print(reduce_file_path("/srv/www/htdocs/wtf/"))
    print(reduce_file_path("/srv/www/htdocs/wtf"))
    print(reduce_file_path("/srv/./././././"))
    print(reduce_file_path("/etc//wtf/"))
    print(reduce_file_path("/etc/../etc/../etc/../"))
    print(reduce_file_path("/etc//wtf/"))
    print(reduce_file_path("/etc/../etc/../etc/../"))
    print(reduce_file_path("//////////////"))
    print(reduce_file_path("/../"))

# Program Run
if __name__ == '__main__':
    main()
