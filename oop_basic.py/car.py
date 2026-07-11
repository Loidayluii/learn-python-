class Car :
    def __init__(self,model,year,colour,sales):
        self.model = model 
        self.year = year 
        self.colour=colour
        self.sales=sales

    def drive(self):
        print(f"you drive the {self.model}")
    def vision(self):
        print(f"the car is {self.colour}")
    def describe(self):
        print(f"{self.model} , {self.year} , {self.colour} ,{self.sales}")