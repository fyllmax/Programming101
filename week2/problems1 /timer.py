# Imports
import time
# import threading

# Globals

timer = 0
is_running = False
stop = False

# Function


def start_timer(seconds):
    '''
    Initiates the timer for the given seconds
    If you start a started time, this should return False
    '''
    global timer, is_running

    if is_running:
        return False
    else:
        timer = seconds + 1
        is_running = True
        # decrease_time()


def decrease_time():
    '''
    Decreases the timer by 1 second.
    Returns True, if the decreasing is successful
    If the timer is not started, return False
    If the time is over, return False
    '''
    global timer, stop, is_running

    if not is_running or timer == 0:
        return False

    if timer > 0:
        while timer > 0:
            timer -= 1
            print(timer)
            time.sleep(1)
            if stop:
                break

    if timer == 0:
        is_running = False
        print("Deacreasing is successful")
        return True


def is_timer_running():
    '''
    Returns True, if the timer is running
    and there are still seconds left (> 0),
    else False
    '''
    if is_running and timer > 0:
        return True
    else:
        return False


def stop_timer():
    '''
    Stops a running timer
    If the timer is running, return True
    If the timer is not running, return False
    '''
    global stop

    if is_running:
        stop = True
        return True
    else:
        return False


def seconds_left():
    '''
    Returns how many seconds are left from the timer
    If the timer is not started or if if it's finished, return 0
    '''
    if is_running:
        return timer
    else:
        return False

# Main


def main():

    start_timer(10)
    decrease_time()


# Program run
if __name__ == "__main__":
    main()
