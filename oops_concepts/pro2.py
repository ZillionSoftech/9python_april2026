class Mobile:
    def __init__(self, brand, ram, storge, processor, camera):
        self.brand = brand
        self.ram = ram
        self.storage  = storge

        print("Working fine")

    def sms(self):
        print(f"I am messaging with {self.brand}")

samsung = Mobile("Samsung","8GB","512GB","Snapdragon","200MP")
samsung.sms()
