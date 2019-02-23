class Concept_Line(object):

    def __init__(self, cuantity, description, amount, total):
        self.cuantity = cuantity
        self.description = description 
        self.amount = amount
        self.total = total
        if self.cuantity != "" && self.total == "":
            self.total = self.cuantity * self. amount


    @property
    def cuantity(self):
        return self.cuantity

    @property
    def description(self):
        return self.description

    @property
    def amount(self):
        return self.amount

    @property
    def total(self):
        return self.total

    
    
