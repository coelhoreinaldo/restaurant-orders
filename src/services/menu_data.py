class MenuData:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path

    def load_data(self):
        with open(self.source_path, "r") as file:
            lines = file.readlines()
            lines = [line.strip().split(",") for line in lines]
            lines.pop(0)
            return lines


teste = MenuData("data/menu_base_data.csv")
print(teste.load_data())
