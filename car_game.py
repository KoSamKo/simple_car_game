# car game

command = ""
started = False

print(
"""
Help:
Start - to start car
Stop - to stop car
Quit - to quit game
"""
)

while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("car is already started")
        else:
            print("car started")
            started = True
    elif command == "stop":
        if not started:
            print("car is already stopped")
        else:
            print("car stopped")
            started = False
    elif command == "quit":
        print("you quit the game :-)")
        break
    else:
        print("Insert valid value please!")
