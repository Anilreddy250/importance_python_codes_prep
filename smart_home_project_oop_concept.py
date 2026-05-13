# 1. The Base Class: SmartDevice
# Every device in a home has a name and a power status. We define these in a parent class so we don't have to rewrite the code for every new gadget.
class SmartDevice:
    def __init__(self, name):
        self.name = name
        self._is_on = False #protected attribute(encapsulation)
    def turn_on(self):
        self._is_on= True
        print(f"[{self.name}] is now ON")
    def turn_off(self):
        self._is_on = False
        print(f"[{self.name}]is now off")

    def status(self):
        state = "ON" if self._is_on else "OFF"
        return f"{self.name}: {state}"
    

# 2. Specialized Devices (Inheritance)
# Now, we create specific devices that inherit from SmartDevice but add their own unique features.
class SmartLight(SmartDevice):
    def __init__(self, name, brightness=100):
        super().__init__(name)
        self.brightness = brightness

    def set_brightness(self, level):
        self.brightness = level
        print(f"[{self.name}] brightness set to {level}%.")

class SmartThermostat(SmartDevice):
    def __init__(self, name, temp=22):
        super().__init__(name)
        self.temp = temp

    def set_temp(self, temp):
        self.temp = temp
        print(f"[{self.name}] temperature set to {temp}°C.")

# 3. The Controller: SmartHome (Composition)
# The "Brain" of the house holds a list of devices. This allows us to perform actions on the entire group at once (Polymorphism).

class SmartHome:
    def __init__(self, home_name):
        self.home_name = home_name
        self.devices = []
    def add_device(self,device):
        self.devices.append(device)
        print(f"Added {device.name} to {self.home_name}")
    def shutdown_all(self):
        print(f"\n---Emergency Shutdown at {self.home_name}-----")
        for device in self.devices:
            device.turn_off()
    def show_report(self):
        print(f"\n---{self.home_name}status Report ----")
        for device in self.devices:
            device.turn_off()
    def show_report(self):
        print(f"\n---{self.home_name} status Report----")
        for device in self.devices:
            print(device.status())

# Create the Home
my_villa = SmartHome("TechAbode")

# Create Devices
living_room_light = SmartLight("Living Room Light")
kitchen_thermostat = SmartThermostat("Kitchen AC")

# Add to Home
my_villa.add_device(living_room_light)
my_villa.add_device(kitchen_thermostat)

# Interact
living_room_light.turn_on()
living_room_light.set_brightness(75)
kitchen_thermostat.turn_on()
kitchen_thermostat.set_temp(18)

# Show current status
my_villa.show_report()

# Global command
my_villa.shutdown_all()