
# match.py menunjukkan cara penggunaan struktur kendali match-case di python
# Contoh penggunaan match-case dengan angka
value = 2
match value:
    case 1:
        print("Value is one")
    case 2:
        print("Value is two")
    case 3:
        print("Value is three")
    case _:
        print("Value is something else")

# Contoh penggunaan match-case dengan string
command = "start"
match command:
    case "start":
        print("Starting the process...")
    case "stop":
        print("Stopping the process...")
    case "pause":
        print("Pausing the process...")
    case _:
        print("Unknown command")
        
# Contoh penggunaan match-case dengan tuple
point = (0, 0)
match point:
    case (0, 0):
        print("Origin")
    case (x, 0):
        print(f"On the X axis at {x}")
    case (0, y):
        print(f"On the Y axis at {y}")
    case (x, y):
        print(f"At point ({x}, {y})")