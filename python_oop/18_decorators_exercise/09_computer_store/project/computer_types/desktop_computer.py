from project.computer_types.computer import Computer


class DesktopComputer(Computer):
    @property
    def processors_available(self):
        return {"AMD Ryzen 7 5700G": 500,
                "Intel Core i5-12600K": 600,
                "Apple M1 Max": 1800, }

    @property
    def max_ram(self):
        return 128

    @property
    def computer_type(self):
        return "desktop computer"


if __name__ == "__main__":
    desktop = DesktopComputer("Dell", "Optiplex")
    try:
        print(desktop.configure_computer("Intel Core i5-12600K", 16))
    except ValueError as error:
        print(error)
