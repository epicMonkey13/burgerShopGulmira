class FoodItem:
    num_of_orders = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        FoodItem.num_of_orders += 1

    def order(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, order_str):
        first, last, pay = order_str.split('-')
        return cls(first, last, pay)




# print(FoodItem.num_of_orders)

customer_1 = FoodItem('burger', 'drink', '50000')
customer_2 = FoodItem('drink', 'burger', '60000')

order_str_1 = 'John-Doe-70000'
order_str_2 = 'Jane-Doe-30000'
order_str_3 = 'Steve-Smith-30000'

new_order_1 = FoodItem.from_string(order_str_1)


print(new_order_1.email)
print(new_order_1.pay)


# # print(customer_1.__dict__)
# customer_1.raise_amount = 1.05
#
# print(customer_1.__dict__)
FoodItem.set_raise_amt(1.05)

# print(FoodItem.raise_amount)
# print(customer_1.raise_amount)
# print(customer_2.raise_amount)
