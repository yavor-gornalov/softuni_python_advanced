from project.vehicles.base_vehicle import BaseVehicle


class CargoVan(BaseVehicle):
    MAX_MILAGE = 180.00
    ADDITIONAL_DISCHARGE_PERCENTAGE = 5

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, max_mileage=CargoVan.MAX_MILAGE)

    @property
    def _get_max_milage(self):
        return CargoVan.MAX_MILAGE

    @property
    def _get_additional_discharge(self):
        return CargoVan.ADDITIONAL_DISCHARGE_PERCENTAGE
