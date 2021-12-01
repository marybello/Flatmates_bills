class Bill:
    """
    Objects that contains data about a bill such as total amount and period of the bill
    """
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    This object contains info about the flatmates living in the flat
    """
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        """
        fmate1 = input("Enter the flatmates name: ")
        day1 = int(input(f"Number of days {fmate1} spent in the house: "))
        fmate2 = input("Enter the other flatmate's name: ")
        day2 = int(input(f"Number of days {fmate2} spent in the house: "))
        ratio1 = day1/(day1 + day2)
        ratio2 = day2/ (day1 + day2)
        fmate1_pays = round(bill.amount * ratio1)
        fmate2_pays = round(bill.amount * ratio2)
        return f"{fmate1} is to pay {fmate1_pays} and {fmate2} is to pay {fmate2_pays}"
        """
        weight = self.days_in_house/ (self.days_in_house + flatmate2.days_in_house)
        to_pay = round(bill.amount *weight)
        return str(to_pay)