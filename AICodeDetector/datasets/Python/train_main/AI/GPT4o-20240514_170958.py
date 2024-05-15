
class EcommerceAgent:
        self.inventory = {}
        self.cart = []

        if item in self.inventory:
            self.inventory[item]['quantity'] += quantity
        else:
            self.inventory[item] = {'price': price, 'quantity': quantity}

        if item in self.inventory and self.inventory[item]['quantity'] >= quantity:
            self.cart.append({'item': item, 'quantity': quantity, 'price': self.inventory[item]['price']})
            self.inventory[item