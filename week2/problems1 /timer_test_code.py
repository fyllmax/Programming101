# Imports
import time

# Globals
timer = 0


# Function

def update(sec):
    global timer
    timer = sec
    while timer > 0:
        timer -= 1
        print(timer)
        time.sleep(1)
        if timer == 0:
        	break

# Main


def main():
    update(60)


# Program run
if __name__ == "__main__":
    main()
