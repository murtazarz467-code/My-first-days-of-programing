# Even & Odd Number Separator - Professional Version

def split_even_odd(numbers):
    """Function to separate even and odd numbers"""
    even = [n for n in numbers if n % 2 == 0]
    odd  = [n for n in numbers if n % 2 != 0]
    return even, odd

print("=== Welcome to Even & Odd Separator ===")
print("Type 'exit' to quit the program at any time.\n")

while True:
    user_input = input("Enter numbers separated by space: ")
    
    if user_input.lower() == 'exit':
        print("Exiting program. Goodbye!")
        break

    numbers = user_input.split()
    
    try:
        numbers = [int(num) for num in numbers]
    except ValueError:
        print("Please enter only numbers separated by spaces.\n")
        continue
    
    even_numbers, odd_numbers = split_even_odd(numbers)
    
    # Sort lists
    even_numbers.sort()
    odd_numbers.sort()
    
    # Professional output
    print("\n========== Output ==========")
    print(f"Odd numbers ({len(odd_numbers)}):", *odd_numbers)
    print(f"Even numbers ({len(even_numbers)}):", *even_numbers)
    print("============================\n")