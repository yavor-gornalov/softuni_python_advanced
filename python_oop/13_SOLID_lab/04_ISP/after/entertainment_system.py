from abc import ABC, abstractmethod
from typing import List


class Connector:
    def __init__(self, type: str):
        self.type = type

    def __repr__(self):
        return self.type


class EntertainmentDevice:
    def __init__(self, name, model):
        self.name = name
        self.model = model
        self.connectors: List[Connector] = []

    def add_connector(self, connector: Connector):
        if not [x for x in self.connectors if x.type == connector.type]:
            self.connectors.append(connector)


class Cable:
    def __init__(self, connector_1: Connector, connector_2: Connector):
        self.connector_1 = connector_1
        self.connector_2 = connector_2

    def connect_devices(self, device_1: EntertainmentDevice, device_2: EntertainmentDevice):
        if self.connector_1 not in device_1.connectors or self.connector_2 not in device_2.connectors:
            return f"Unable to connect devices with {self}"
        return f"{device_1.name} and {device_2.name} are now connected"

    def __repr__(self):
        return f"{self.connector_1}-to-{self.connector_2} cable"


class HDMIConnector(Connector):
    pass


class RCAConnector(Connector):
    pass


class RJ45Connector(Connector):
    pass


class Television(EntertainmentDevice):
    pass


class Router(EntertainmentDevice):
    pass


class GameConsole(EntertainmentDevice):
    pass


# define connectors:
hdmi_connector = Connector("HDMI")
rca_connector = Connector("RCA")
rj_connector = Connector("RJ45")

# define cables:
hdmi_cable = Cable(hdmi_connector, hdmi_connector)
rca_cable = Cable(rca_connector, rca_connector)
rca_to_hdmi_cable = Cable(rca_connector, hdmi_connector)
ethernet_cable = Cable(rj_connector, rj_connector)

tv = Television("Samsung", "Unknown")
tv.add_connector(hdmi_connector)
tv.add_connector(rj_connector)

router = Router("TP Link", "Archer")
router.add_connector(rj_connector)

console = GameConsole("PS5", "xXx")
console.add_connector(rca_connector)

print(hdmi_cable.connect_devices(console, tv))
print(rca_to_hdmi_cable.connect_devices(console, tv))
print(ethernet_cable.connect_devices(console, router))
print(ethernet_cable.connect_devices(tv, router))
