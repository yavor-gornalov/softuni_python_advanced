from typing import List

from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers: List[Customer] = []
        self.trainers: List[Trainer] = []
        self.equipment: List[Equipment] = []
        self.plans: List[ExercisePlan] = []
        self.subscriptions: List[Subscription] = []

    @staticmethod
    def obj_in_list(obj, array):
        for element in array:
            is_equal = True
            for prop, value in obj.__dict__.items():
                if prop == "id":
                    continue
                is_equal = element.__dict__[prop] == value
                if not is_equal:
                    break
            if is_equal:
                return True
        return False

    @staticmethod
    def find_object_by_id(object_id, array):
        for obj in array:
            if obj.id == object_id:
                return obj

    def add_customer(self, customer: Customer):
        # TODO check if specific object in self.object_list, but what would happened
        #  if we have new instance with same attributes?
        if not self.obj_in_list(customer, self.customers):
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if not self.obj_in_list(trainer, self.trainers):
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if not self.obj_in_list(equipment, self.equipment):
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if not self.obj_in_list(plan, self.plans):
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if not self.obj_in_list(subscription, self.subscriptions):
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        subscription = self.find_object_by_id(subscription_id, self.subscriptions)
        customer = self.find_object_by_id(subscription.customer_id, self.customers)
        trainer = self.find_object_by_id(subscription.trainer_id, self.trainers)
        plan = [p for p in self.plans if p.trainer_id == trainer.id][0]
        equipment = self.find_object_by_id(plan.equipment_id, self.equipment)

        result = (f"{subscription}\n"
                  f"{customer}\n"
                  f"{trainer}\n"
                  f"{equipment}\n"
                  f"{plan}\n")

        return result
