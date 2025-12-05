class Payment:
    def process(self, type, amount):
        if type == "credit":
            print(f"پرداخت {amount} با کارت")
        elif type == "paypal":
            print(f"پرداخت {amount} با پی‌پال")
        elif type == "crypto":
            print(f"پرداخت {amount} با کریپتو")