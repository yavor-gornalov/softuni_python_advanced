from project.vehicles.base_vehicle import BaseVehicle


class PassengerCar(BaseVehicle):
    MAX_MILAGE = 450.00
    ADDITIONAL_DISCHARGE_PERCENTAGE = 0

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, max_mileage=PassengerCar.MAX_MILAGE)

    @property
    def _get_max_milage(self):
        return PassengerCar.MAX_MILAGE

    @property
    def _get_additional_discharge(self):
        return PassengerCar.ADDITIONAL_DISCHARGE_PERCENTAGE
