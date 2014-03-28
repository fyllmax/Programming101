from glob import glob
from subprocess import call


def run_all_tests():
    tests = glob('*/test.py')
    for test in tests:
        call("python3 " + test, shell=True)
    return True


def main():
    run_all_tests()

if __name__ == '__main__':
    main()
