import os
import glob


def ext_count(fpath, fname):
    # fpath = os.getcwd()
    dpath = "*" + fname
    count = 0
    os.chdir(fpath)
    for file in glob.glob(dpath):
        count += 1
    return count


    # for file in os.listdir(fpath):
    #     if file.endswith(fname):
    #         count += 1

    # return count

# Main
def main():
    print(ext_count("/home/andre/Documents/HackBulgaria/week2", ".py"))
    print(ext_count("/home/andre/Documents/HackBulgaria/week2", ".txt"))
    print(ext_count("/home/andre/Documents/HackBulgaria/week2", ".md"))


# Program run
if __name__ == "__main__":
    main()
