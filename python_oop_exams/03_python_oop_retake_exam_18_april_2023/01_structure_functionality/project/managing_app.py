from typing import List

from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    VEHICLE_TYPES = {
        "PassengerCar": PassengerCar,
        "CargoVan": CargoVan
    }

    def __init__(self):
        self.users: List[User] = []
        self.vehicles: List[BaseVehicle] = []
        self.routes: List[Route] = []

    @property
    def next_route_id(self):
        return len(self.routes) + 1

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        if self._get_user_by_diving_licence(driving_license_number) is not None:
            return f"{driving_license_number} has already been registered to our platform."
        new_user = User(first_name, last_name, driving_license_number)
        self.users.append(new_user)
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in ManagingApp.VEHICLE_TYPES:
            return f"Vehicle type {vehicle_type} is inaccessible."
        if self._get_vehicle_by_license_plate(license_plate_number) is not None:
            return f"{license_plate_number} belongs to another vehicle."
        new_vehicle = ManagingApp.VEHICLE_TYPES[vehicle_type](brand, model, license_plate_number)
        self.vehicles.append(new_vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        existing_route = self._get_route_by_start_and_end_point(start_point, end_point)
        if existing_route is not None:
            if existing_route.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."
            elif existing_route.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."
            else:
                existing_route.is_locked = True

        new_route = Route(start_point, end_point, length, self.next_route_id)
        self.routes.append(new_route)
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,
                  is_accident_happened: bool):
        user = self._get_user_by_diving_licence(driving_license_number)
        vehicle = self._get_vehicle_by_license_plate(license_plate_number)
        route = self._get_route_by_id(route_id)
        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."
        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."
        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)
        if is_accident_happened:
            vehicle.change_status()
            user.decrease_rating()
        else:
            user.increase_rating()
        return str(vehicle)

    def repair_vehicles(self, count: int):
        collection = sorted([v for v in self.vehicles if v.is_damaged], key=lambda v: (v.brand, v.model))

        count_of_repaired_vehicles = 0
        for vehicle in collection[:count]:
            vehicle.change_status()
            vehicle.recharge()
            count_of_repaired_vehicles += 1

        return f"{count_of_repaired_vehicles} vehicles were successfully repaired!"

    def users_report(self):
        result = ["*** E-Drive-Rent ***"]
        [result.append(str(u)) for u in sorted(self.users, key=lambda u: -u.rating)]
        return '\n'.join(result)

    # helpers
    def _get_user_by_diving_licence(self, driving_license_number):
        collection = [u for u in self.users if u.driving_license_number == driving_license_number]
        return collection[0] if collection else None

    def _get_vehicle_by_license_plate(self, licence_plate):
        collection = [v for v in self.vehicles if v.license_plate_number == licence_plate]
        return collection[0] if collection else None

    def _get_route_by_start_and_end_point(self, start, end):
        collection = [r for r in self.routes if r.start_point == start and r.end_point == end]
        return collection[0] if collection else None

    def _get_route_by_id(self, route_id):
        collection = [r for r in self.routes if r.route_id == route_id]
        return collection[0] if collection else None
