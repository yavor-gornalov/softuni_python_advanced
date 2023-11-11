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

    def add_customer(self, customer: Customer):
        if not self.__find_item_by_id(customer.id, self.customers):
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if not self.__find_item_by_id(trainer.id, self.trainers):
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if not self.__find_item_by_id(equipment.id, self.equipment):
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if not self.__find_item_by_id(plan.id, self.plans):
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if not self.__find_item_by_id(subscription.id, self.subscriptions):
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        subscription = self.__find_item_by_id(subscription_id, self.subscriptions)
        customer = self.__find_item_by_id(subscription.customer_id, self.customers)
        trainer = self.__find_item_by_id(subscription.trainer_id, self.trainers)
        plan = self.__find_item_by_id(trainer.id, self.plans)
        equipment = self.__find_item_by_id(plan.equipment_id, self.equipment)

        return "\n".join([str(subscription),
                          str(customer),
                          str(trainer),
                          str(equipment),
                          str(plan)])

    # HELPERS:
    @staticmethod
    def __find_item_by_id(item_id, collection):
        return next((i for i in collection if i.id == item_id), None)
