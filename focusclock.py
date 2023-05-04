import time

def countdown_timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        print("Time remaining: ", seconds // 60, "minutes", seconds % 60, "seconds")
        time.sleep(1)
        seconds -= 1
    print("Time's up! Your focus session is over.")

if __name__ == '__main__':
    minutes = int(input("How many minutes do you want to focus? "))
    countdown_timer(minutes)
