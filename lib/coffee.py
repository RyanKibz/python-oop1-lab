#!/usr/bin/env python3

class Coffee:
    def __init__(self,size,price,status="brewed"):
        self._size = "Large"
        self.size = size  
        self.price = price
        self.status = status
        
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        valid_sizes = ["Small", "Medium", "Large"]
        if value not in valid_sizes:
            print("size must be Small, Medium, or Large")
            self._size = value

    def tip(self):
        print("This coffee is great, here’s a tip!")
        if self.price is not None:
            self.price += 1.0

    def repair_shoe(self):
        print("This coffee was made while repairing shoes... here’s a tip!")
print(Coffee)