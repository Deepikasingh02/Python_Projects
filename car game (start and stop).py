command = ""
started = False
stopped = False
while True:
    command = input(">").lower()
    if command == "start":
        if started:
            print("car is already started")
        else:
            started = True
            print("car started...")
    elif command == "stop":
        if stopped:
            print("car is already stopped")
        else:
            stopped = True
            print("car stopped...")
    elif command == "help":
        print("""
        star-to start the car
        stop- to stop the car
        quit- game over
        """)
    elif command == "quit":
        print("game over")
        break
    else:
        print("sorry i don't understand")
