while True:   
    try:
        rows = int(input("Enter the number of rows: ")) # Imput from user
        break                                           # Exit loop if input is valid   
    except ValueError:                                  # Handle invalid input   
        print("Invalid input. Please enter a number.")  # Prompt user again

#printing stars from 1 to the given number of rows in increasing order
rows = int(input("Enter the number of rows: "))
for i in range(1, rows + 1):
    print("* " * i)
    
