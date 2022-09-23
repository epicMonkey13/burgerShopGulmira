BURGER_PRICE = 6.00
BURGER_CONDIMENTS = ["tomato", "lettuce", "onion", "cheese"]
DRINK_TYPES = ["fanta", "coca cola", "sprite"]
DRINK_SIZES = [12, 16, 20]
DRINK_PRICES = [1.00, 2.00, 3.00]
SIDE_PRICE = 3.00
SIDES = ["fries", "coleslaw", "salad"]
COMBO_DISCOUNT = 2.00


class FoodItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return "Item: " + self.name + "\n" + "Price: £" + str(self.price) + "\n"

    def get_price(self):
        return self.price


class burger(FoodItem):
    def __init__(self, name, price):
        super(burger, self).__init__(name, price)
        self.condiments = []

    def add_condiment(self, condiment):
        if condiment not in self.condiments:
            self.condiments.append(condiment)

    def __str__(self):
        s = super(burger, self).__str__()
        s = s + "Condiments:" + ", ".join(self.condiments)
        return s


class drink(FoodItem):
    def __init__(self, name, size, price):
        super(drink, self).__init__(name, price)
        self.size = size

    def __str__(self):
        s = super(drink, self).__str__()
        s = s + "Size: " + str(self.size) + "mg"
        return s


class side(FoodItem):
    def __init__(self, name, price):
        super(side, self).__init__(name, price)


class combo(FoodItem):
    def __init__(self, name, b, d, s, discount):
        self.name = name
        self.burger = b
        self.drink = d
        self.side = s
        self.discount = discount
        self.price = self.burger.get_price() + self.drink.get_price() + self.side.get_price() - self.discount

    def __str__(self):
        s = ""
        s = s + "Combo: " + self.name + "\n"
        s = s + str(self.burger) + "\n" + str(self.drink) + "\n" + str(self.side) + "\n"

        s = s + "Discount: $" + str(self.discount) + "\n"
        s = s + "Combo Price After Discount: £" + str(self.price) + "\n"

        return s


class order:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_price(self):
        price = 0.0
        for item in self.items:
            price = price + item.get_price()
        return price

    def __str__(self):
        s = [str(item) for item in self.items]
        return "\n".join(s)

    def display(self):
        print("===============")
        print("Order summary")
        print("Order for " + self.name)
        print("Items in the order: ")

        for item in self.items:
            print("--------")
            print(str(item))
        print("--------")
        print("Total : £" + str(self.get_price()))
        print("===============")

    def order_many(self):
        print("Welcome to Gulmira's Burger Shop")
        q1 = input("Please enter your name")
        order_received = order(q1)
        print("Your order is on the way")
        done = False
        while done == False:
            item = order_once(self)
            order_received.add_item(item)
            q1 = input("Would you like to add anything? (Enter n if nothing else.) ")
            if q1.lower() == "n":
                done = True
        return order_received

    def order_once():
        possible_options = [1, 2, 3, 4]
        print("Type 1 for a Burger")
        print("Type 2 for a Drink")
        print("Type 3 for a Side")
        print("Type 4 for a Combo")
        choice = None
        while choice == None:
            q1 = input("Please enter your choice: ")
            if int(q1) in possible_options:
                choice = int(q1)
        item = None
        if choice == 1:
            item = get_burger_order()
        elif choice == 2:
            item = get_drink_order()
        elif choice == 3:
            item = get_side_order()
        elif choice == 4:
            item = get_combo_order()
        return item

    def get_burger_order(self):
        b = burger("Burger", BURGER_PRICE)
        q1 = input("Would you like any condiments on your burger? (Enter y for yes) ")
        if q1.lower() == "y":
            for condiment in BURGER_CONDIMENTS:
                q = input("Do you want " + str(condiment) + "? (Enter y or n): ")
                if q.lower() == "y":
                    b.add_condiment(condiment)
                return b

    def get_drink_order(self):
        print("These are the available drinks:")
        print(DRINK_TYPES)
        print("These are the available sizes:")
        print(DRINK_SIZES)
        choice = False
        drink_name = None
        drink_size = None
        drink_price = None
        while choice == False:
            q1 = input("What drink do you want? ")
            if q1.lower() in DRINK_TYPES:
                choice = True
                drink_name = q1.lower()
            else:
                print("Please enter a valid drink.")
        choice = False
        while choice == False:
            q1 = input("What size do you want? " + str(DRINK_SIZES) + ": ")
            if int(q1) in DRINK_SIZES:
                choice = True
                drink_size = int(q1)
            else:
                print("please enter a valid size")
                # locate the price of the drink based on the index of the size:
        drink_price = DRINK_PRICES[DRINK_SIZES.index(drink_size)]
        d = drink(drink_name, drink_size, drink_price)
        return d

    def get_side_order(self):
        print("These are the available sides:")
        print(SIDES)
        choice = False
        side_name = None
        while choice == False:
            q1 = input("What side do you want? ")
            if q1.lower() in SIDES:
                choice = True
                side_name = q1.lower()
            else:
                print("Please enter a valid side.")
        s = side(side_name, SIDE_PRICE)
        return s

    def get_combo_order(self):
        print("Let's get you a combo meal!")
        print("First, let's order the burger for your combo.")
        b = get_burger_order(self)
        print("Now, let's order the drink for your combo.")
        d = get_drink_order(self)
        print("Finally, let's order the side for your combo.")
        s = get_side_order(self)
        c = combo("Combo", b, d, s, COMBO_DISCOUNT)
        # print(str(c))
        return c

    client_order = order_many()
    client_order.display()






