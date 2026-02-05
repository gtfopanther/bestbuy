import products
import store


def list_products(store_obj: store.Store):
    prods = store_obj.get_all_products()
    print("------")
    for i, p in enumerate(prods, start=1):
        print(f"{i}. {p.name}, Price: ${p.price}, Quantity: {p.quantity}")
    print("------")


def start(store_obj: store.Store):
    while True:
        print()
        print("   Store Menu")
        print("   ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ").strip()

        if choice == "1":
            list_products(store_obj)

        elif choice == "2":
            print(f"Total of {store_obj.get_total_quantity()} items in store")

        elif choice == "3":
            # Show products first (demo style)
            list_products(store_obj)
            print("When you want to finish order, enter empty text.")

            shopping_list = []
            active_products = store_obj.get_all_products()

            while True:
                prod_input = input("Which product # do you want? ").strip()

                # Finish on empty text
                if prod_input == "":
                    break

                amount_input = input("What amount do you want? ").strip()

                try:
                    prod_index = int(prod_input)
                    amount = int(amount_input)

                    if prod_index < 1 or prod_index > len(active_products):
                        raise Exception("Invalid product index")

                    if amount <= 0:
                        raise Exception("Invalid amount")

                    product = active_products[prod_index - 1]
                    shopping_list.append((product, amount))
                    print("Product added to list!")

                except Exception:
                    print("Error adding product!")

            if len(shopping_list) == 0:
                # Demo zeigt ggf. nichts; wir lassen es neutral
                continue

            try:
                total_price = store_obj.order(shopping_list)
                print(f"Order cost: {total_price} dollars.")
            except Exception as e:
                print(f"Order failed: {e}")

        elif choice == "4":
            break

        else:
            # Demo erwähnt das meist nicht, aber ist ok
            continue


def main():
    # setup initial stock of inventory
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]
    best_buy = store.Store(product_list)

    start(best_buy)


if __name__ == "__main__":
    main()
