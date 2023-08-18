from typing import List

from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    def __init__(self, name: str, ):
        self.name = name
        self.customers: List[Customer] = []
        self.dvds: List[DVD] = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def __get_customer_by_id(self, customer_id) -> Customer:
        for customer in self.customers:
            if customer_id == customer.id:
                return customer

    def __get_dvd_by_id(self, dvd_id) -> DVD:
        for dvd in self.dvds:
            if dvd.id == dvd_id:
                return dvd

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int, ):
        current_customer = self.__get_customer_by_id(customer_id)
        current_dvd = self.__get_dvd_by_id(dvd_id)

        if current_dvd in current_customer.rented_dvds:
            return f"{current_customer.name} has already rented {current_dvd.name}"
        if current_dvd.is_rented:
            return "DVD is already rented"
        if current_customer.age < current_dvd.age_restriction:
            return f"{current_customer.name} should be at least {current_dvd.age_restriction} to rent this movie"

        current_customer.rented_dvds.append(current_dvd)
        current_dvd.is_rented = True
        return f"{current_customer.name} has successfully rented {current_dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        current_customer = self.__get_customer_by_id(customer_id)
        current_dvd = self.__get_dvd_by_id(dvd_id)

        if current_dvd not in current_customer.rented_dvds:
            return f"{current_customer.name} does not have that DVD"

        current_dvd.is_rented = False
        current_customer.rented_dvds.remove(current_dvd)
        return f"{current_customer.name} has successfully returned {current_dvd.name}"

    def __repr__(self):
        result = ""
        for customer in self.customers:
            result += f"{customer.__repr__()}\n"
        for dvd in self.dvds:
            result += f"{dvd.__repr__()}\n"
        return result
