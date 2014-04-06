import os
import glob
import os


def ext_count(fname):
    fpath = os.getcwd()
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
    print(ext_count(".py"))
    print(ext_count(".txt"))
    print(ext_count(".md"))


# Program run
if __name__ == "__main__":
    main()
