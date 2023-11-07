from typing import List

from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers: List[Customer] = []
        self.dvds: List[DVD] = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    @property
    def rented_dvd_ids(self):
        return [x.id for x in self.dvds if x.is_rented]

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer = self.__get_obj_by_attribute_value("id", customer_id, self.customers)
        if not customer:
            return
        dvd = self.__get_obj_by_attribute_value("id", dvd_id, self.dvds)
        if not dvd:
            return

        if dvd_id in customer.rented_dvd_ids:
            return f"{customer.name} has already rented {dvd.name}"
        if dvd_id in self.rented_dvd_ids:
            return "DVD is already rented"
        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
        customer.rented_dvds.append(dvd)
        dvd.is_rented = True
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = self.__get_obj_by_attribute_value("id", customer_id, self.customers)
        if not customer:
            return
        if dvd_id not in customer.rented_dvd_ids:
            return f"{customer.name} does not have that DVD"

        dvd = self.__get_obj_by_attribute_value("id", dvd_id, customer.rented_dvds)
        customer.rented_dvds.remove(dvd)
        dvd.is_rented = False
        return f"{customer.name} has successfully returned {dvd.name}"

    def __repr__(self):
        result = []
        [result.append(str(x)) for x in self.customers]
        [result.append(str(x)) for x in self.dvds]
        return "\n".join(result)

    # HELPERS:
    @staticmethod
    def __get_obj_by_attribute_value(attr, value, array):
        for obj in array:
            if getattr(obj, attr, None) == value:
                return obj
