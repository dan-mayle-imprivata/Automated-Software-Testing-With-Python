class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

# will return when you print an example of class (See lesson 24)
    def __str__(self):
        # !r will add quotes for you
        return f"Device {self.name!r} ({self.connected_by})"

    def disconnect(self):
        self.connected = False
        print("Disconnected.")


# printer = Device("Printer", "USB")
# print(printer)
# Device Printer,(USB)
# Disconnected

# Creating a new class Printer that is inheriting from Device class
# super().__init__() will call the init method of the parent class (or super class)
    # this is done instead of rewriting self.name = name, ect
class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__()
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"

    def print(self, pages):
        if not self.connected:
            print("Your printer is not connected!")
            return
        print(f"Printing {pages} pages.")
        self.remaining_pages -= pages


printer = Printer("Printer", "USB", 500)
printer.print(20)
print(printer)
# Printing 20 pages
# Device "Printer" (USB)(480 pages remaining)

printer.disconnect()  # Disconnected.
printer.print(30)  # Your printer is not connected!
