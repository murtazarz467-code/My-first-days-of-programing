class Coffee:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"


class Order:
    def __init__(self):
        self.items: list[Coffee] = []

    def add_item(self, coffee: Coffee):
        self.items.append(coffee)
        print(f"Added {coffee.name} to your order.")

    def remove_item(self, index: int) -> bool:
        if 0 <= index < len(self.items):
            removed = self.items.pop(index)
            print(f"Removed {removed.name} from your order.")
            return True
        print("Invalid item number.")
        return False

    def total(self) -> float:
        return sum(item.price for item in self.items)

    def show_order(self):
        if not self.items:
            print("No items in your order.")
            return

        print("\n--- Your Order ---")
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item}")
        print(f"Total: ${self.total():.2f}\n")

    def checkout(self):
        if not self.items:
            print("Your cart is empty.")
            return

        self.show_order()
        confirm = input("Proceed to checkout? (yes/no): ").strip().lower()

        if confirm in ("yes", "y"):
            print("Your order has been confirmed. Thank you!")
            self.items.clear()
        else:
            print("Checkout cancelled.")


def print_menu(menu: list[Coffee], menu_actions: dict[str, str]):
    print("\n===== Coffee Menu =====")
    for i, coffee in enumerate(menu, 1):
        print(f"{i}. {coffee}")

    offset = len(menu)
    for i, label in enumerate(menu_actions.values(), offset + 1):
        print(f"{i}. {label}")


def get_choice(prompt: str) -> str:
    return input(prompt).strip()


def main():
    menu = [
        Coffee("Espresso", 2.50),
        Coffee("Latte", 3.50),
        Coffee("Cappuccino", 3.00),
        Coffee("Americano", 2.00),
    ]

    # Action labels are generated dynamically so numbering never
    # falls out of sync with the coffee list above.
    menu_actions = {
        "view": "View Order",
        "remove": "Remove Item",
        "checkout": "Checkout",
        "exit": "Exit",
    }
    action_keys = list(menu_actions.keys())

    order = Order()

    while True:
        print_menu(menu, menu_actions)
        choice = get_choice("Choose an option: ")

        if not choice.isdigit():
            print("Invalid choice. Please enter a number.")
            continue

        choice_num = int(choice)
        total_options = len(menu) + len(menu_actions)

        if not (1 <= choice_num <= total_options):
            print("Invalid choice. Try again.")
            continue

        if choice_num <= len(menu):
            order.add_item(menu[choice_num - 1])
            continue

        action = action_keys[choice_num - len(menu) - 1]

        if action == "view":
            order.show_order()

        elif action == "remove":
            order.show_order()
            if order.items:
                idx = get_choice("Enter item number to remove: ")
                if idx.isdigit():
                    order.remove_item(int(idx) - 1)
                else:
                    print("Invalid input.")

        elif action == "checkout":
            order.checkout()

        elif action == "exit":
            print("Thanks for visiting. Goodbye!")
            break


if __name__ == "_main_":
    main()
