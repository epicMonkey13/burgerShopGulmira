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

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


# print(FoodItem.num_of_orders)

customer_1 = FoodItem('burger', 'drink', '50000')
customer_2 = FoodItem('drink', 'burger', '60000')

import datetime

my_date = datetime.date(2022, 9, 23)
print(FoodItem.is_workday(my_date))
