class Refiner:
    def __init__(self, name):
        self.name = name
        self.tokens = 0
        self.CI = 0
        self.perks = []
        self.discovered_tempers = set()
        self.inventory = {
            "tools": [],
            "vouchers": [],
            "food": []
        }
    
    def add_tool(self, tool):
        self.inventory["tools"].append(tool)

    def add_voucher(self, voucher):
        self.inventory["vouchers"].append(voucher)

    def add_food(self, food):
        self.inventory["food"].append(food)