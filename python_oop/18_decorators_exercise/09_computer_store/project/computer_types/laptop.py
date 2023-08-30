from project.computer_types.computer import Computer


class Laptop(Computer):
    @property
    def processors_available(self):
        return {"AMD Ryzen 9 5950X": 900,
                "Intel Core i9-11900H": 1050,
                "Apple M1 Pro": 1200, }

    @property
    def max_ram(self):
        return 64

    @property
    def computer_type(self):
        return "laptop"


if __name__ == "__main__":
    laptop = Laptop("HP", "Probook")
    try:
        print(laptop.configure_computer("AMD Ryzen 9 5950X", 16))
    except ValueError as error:
        print(error)
