import time
import threading
import sys


class Company:
    def __init__(self, name, gen=0, worth=500):
        self.name = name
        self.worth = worth
        self.assets = {"employee": 0, "truck": 0, "store": 0}
        self.gen_per_sec = gen

    def buy(self, asset, amount):
        try:
            asset_gen = {"employee": 10, "truck": 100, "store": 2500}
            assets = {"employee": 100, "truck": 5000, "store": 100000}
            if asset in assets:
                if int((amount * assets[asset])) <= int(self.worth):#pyest says it str
                    self.worth = self.worth - (amount * assets[asset])
                    self.gen_per_sec = self.gen_per_sec + (amount * asset_gen[asset])
                    self.assets[asset] = self.assets[asset] + amount
                else:
                    print("You not have enough money.")
            else:
                print("Invalid asset name.")
        except ValueError:
            pass

    def sell(self, asset, amount):
        try:
            asset_gen = {"employee": 10, "truck": 100, "store": 2500}
            assets = {"employee": 100, "truck": 5000, "store": 100000}
            if asset in assets:
                if int(amount) <= int(self.assets[asset]):#pyest says it str
                    self.worth = self.worth + (amount * assets[asset])
                    self.gen_per_sec = self.gen_per_sec - (amount * asset_gen[asset])
                    self.assets[asset] = self.assets[asset] - amount
                else:
                    print(f"You do not have enough {asset}(s)")
            else:
                print("Invalid asset name.")
        except ValueError:
            pass

    def gen(self):
        self.worth = self.worth + int(self.gen_per_sec)


def main():  # implement command-line arg for setup
    global company
    name = input("What is your company name? ")
    company = Company(name)
    print(f"Congradulations your company {company.name} is worth ${company.worth}")
    thread1 = threading.Thread(target=generate)
    thread1.start()
    thread2 = threading.Thread(target=mainloop)
    thread2.start()


def mainloop():
    while True:
        op = input("buy/sell/check/help: ").lower().strip()
        if op == "buy":
            op_buy()
        elif op == "sell":
            op_sell()
        elif op == "check":
            op_check()
        elif op == "help":
            help()


def op_buy():
    asset = input("Buy what: ").lower().strip()
    amount = int(input("Amount: "))
    company.buy(asset, amount)


def op_sell():
    asset = input("Sell what: ").lower().strip()
    amount = int(input("Amount: "))
    company.sell(asset, amount)


def op_check():
    print(f"{company.name} is worth: {company.worth}")
    print(f"You make ${company.gen_per_sec} per second!")
    for key, value in company.assets.items():
        print(key, " : ", value) 




def help():
    asset_props = [
        "Employee: cost 100, gens 10",
        "Truck: cost 5000, gen 100",
        "Store: cost 100000, gen 2500",
    ]
    print(
        "This is a company building game. \nThe goal is to buy/sell assets which generate money over time. \nHere is a list of assets and their properties: "
    )
    print(*asset_props, sep="\n")


def generate():
    while True:
        if company.worth <= 1000000:
            company.gen()
            time.sleep(1)
        else:
            sys.exit(
                f"\nCongradulations! {company.name} is worth $1000000! You Won the Game!"
            )


if __name__ == "__main__":
    main()
