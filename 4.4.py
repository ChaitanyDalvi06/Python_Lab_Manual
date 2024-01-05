class Store:
    def __init__(self):
        self.products = {}

    def add_product(self, code, name, price):
        self.products[code] = {'name': name, 'price': price}

    def display_menu(self):
        print("Menu:")
        print("Code\tName\tPrice")
        for code, product in self.products.items():
            print(f"{code}\t{product['name']}\t₹{product['price']}")

    def generate_bill(self, order):
        total_amount = 0
        print("\n------------------ RECEIPT ------------------")
        print("Code\tName\tPrice\tQuantity\tTotal")
        for code, quantity in order.items():
            product = self.products[code]
            item_total = quantity * product['price']
            total_amount += item_total
            print(f"{code}\t{product['name']}\t₹{product['price']}\t{quantity}\t\t₹{item_total}")

        print("\nTotal Amount: ₹{:.2f}\n".format(total_amount))


def main():
    store = Store()