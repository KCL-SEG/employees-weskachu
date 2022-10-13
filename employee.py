"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contract, commission = None):
        self.name = name
        self.contract = contract
        self.commission = commission

    def get_pay(self):
        totalPay = 0

        # add contract pay to total pay
        if self.contract[0] == 'salary':
            totalPay += self.contract[1]
        elif self.contract[0] == 'hourly':
            totalPay += self.contract[1] * self.contract[2]

        # add commission pay to total pay
        if self.commission != None:
            if self.commission[0] == 'contract':
                totalPay += self.commission[1] * self.commission[2]
            elif self.commission[0] == 'bonus':
                totalPay += self.commission[1]

        return totalPay

        # print information regarding contract pay for str function
    def print_monthly_info(self):
        if self.contract[0] == 'salary':
            return f'monthly salary of {self.contract[1]}'
        elif self.contract[0] == 'hourly':
            return f'contract of {self.contract[1]} hours at {self.contract[2]}/hour'

        # print information regarding commission pay for str function
    def print_commission_info(self):
        if self.commission != None:
            if self.commission[0] == 'contract':
                return f' and receives a commission for {self.commission[1]} contract(s) at {self.commission[2]}/contract'
            elif self.commission[0] == 'bonus':
                return f' and receives a bonus commission of {self.commission[1]}'
        else:
            return ""

    def __str__(self):
        return f'{self.name} works on a {self.print_monthly_info()}{self.print_commission_info()}. Their total pay is {self.get_pay()}.'


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', ['salary', 4000])

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', ['hourly', 100, 25])

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', ['salary', 3000], ['contract', 4, 200])

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', ['hourly', 150, 25], ['contract', 3, 220])

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', ['salary', 2000], ['bonus', 1500])

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', ['hourly', 120, 30], ['bonus', 600])
