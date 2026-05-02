import json
import math 
import os

def calcolator():
    History = "history.json"
    def load_history():
        if os.path.exists(History):
            with open(History,"r") as f:
                return json.load(f)
        return[]
        
    def save_history(history):
        with open(History, "w") as f:
            json.dump(history,f,indent= 4)

    def clear_history():
        if os.path.exists(History):
            os.remove(History)

    # Display menu
    def show_menu():
        print("\n" + "="*40)
        print("ADVANCED PYTHON CALCULATOR 💻")
        print("="*40)
        print(" +    Addition")
        print(" -    Subtraction")
        print(" *    Multiplication")
        print(" /    Division")
        print(" ^    Power")
        print(" sqrt Square root")
        print(" %    Percentage")
        print(" h    Show history")
        print(" c    Clear history 🗑️")
        print(" Q    Quit")
        print("="*40)

    history = load_history()


    while True:
        show_menu()
        operation = input("Choose an operation: ").lower()

        # Quit
        if operation == "q":
            save_history(history)
            print("👋 Goodbye!")
            break

        # Show history
        if operation == "h":
            print("\n📜 History:")
            if not history:
                print("No history yet!")
            else:
                for item in history:
                    print(item)
            input("\nPress Enter to continue...")
            continue

        # Clear history
        if operation == "c":
            confirm = input("Are you sure you want to clear history? (y/n): ")
            if confirm.lower() == "y":
                history.clear()
                clear_history()
                print("✅ History cleared!")
            else:
                print("❌ Cancelled")
            continue

        # Try-except for error handling
        try:
            # Square root operation
            if operation == "sqrt":
                num = float(input("Enter a number: "))
                result = math.sqrt(num)
                text = f"√{num} = {result}"

            else:
                # Get two numbers from user
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))

                if operation == "+":
                    result = num1 + num2
                    text = f"{num1} + {num2} = {result}"

                elif operation == "-":
                    result = num1 - num2
                    text = f"{num1} - {num2} = {result}"

                elif operation == "*":
                    result = num1 * num2
                    text = f"{num1} * {num2} = {result}"

                elif operation == "/":
                    if num2 == 0:
                        print("❌ Cannot divide by zero!")
                        continue
                    result = num1 / num2
                    text = f"{num1} / {num2} = {result}"

                elif operation == "^":
                    result = num1 ** num2
                    text = f"{num1} ^ {num2} = {result}"

                elif operation == "%":
                    result = (num1 / num2) * 100
                    text = f"{num1} % of {num2} = {result}%"

                else:
                    print("❌ Invalid operation!")
                    continue

            # Show result
            print("✅ Result:", result)

            # Add to history and save
            history.append(text)
            save_history(history)

            input("\nPress Enter to continue...")

        except ValueError:
            print("❌ Invalid input! Please enter a number.")
        except Exception as e:
            print(f"❌ Error: {e}")