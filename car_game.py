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
            started = True
            print("car started")
    elif command == "stop":
        if not started:
            print("car is already stopped")
        else:
            started = False
            print("car stopped")
    elif command == "quit":
        print("quit game")
        break
    else:
        print("Insert valid value please!")