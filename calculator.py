class Calculator:
    def add(self,n1,n2):
        try:
            return n1 + n2
        except Exception:
            print("Exception handled , check inputs ")
    def sub(self,n1,n2):
         try:
            return n1 - n2
         except Exception:
             print("Exception handled , check inputs ")
    def mul(self,n1,n2):
        try:
            return n1 * n2
        except Exception :
            print("Exception handled , check inputs ")

    def div(self,n1,n2):
        try:
            return n1 / n2
        except Exception:
            print("Exception handled , check inputs ")
calci = Calculator()

addition_numbers = calci.add(2,3)
substraction_numbers = calci.sub(2,3)
multiplication_numbers = calci.mul(2,3)
division_numbers = calci.div(2,0)
print(addition_numbers)
print(substraction_numbers)
print(multiplication_numbers)
print(division_numbers)