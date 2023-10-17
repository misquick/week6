try:
    file_input = input("enter a file name:")

    with open(file_input, 'r') as file:
        for line in file:
            print(line.upper())
    
except FileNotFoundError:
    print("Error, file does not exist")
