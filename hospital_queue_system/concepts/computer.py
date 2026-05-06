class Computer:
    def __init__(self,ram, processor):
        self.ram = ram
        self.processor = processor
        
    def gamming(self):
        return "I am inside game method"


obj = Computer("8GB", "I5 13th Gen")
status=obj.gamming()
print(status)