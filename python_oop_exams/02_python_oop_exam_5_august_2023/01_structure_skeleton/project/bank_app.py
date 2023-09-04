from typing import List

from project.clients.adult import Adult
from project.clients.base_client import BaseClient
from project.clients.student import Student
from project.loans.base_loan import BaseLoan
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    LOAN_TYPES = {
        "StudentLoan": StudentLoan,
        "MortgageLoan": MortgageLoan
    }

    CLIENT_TYPES = {
        "Student": Student,
        "Adult": Adult
    }

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans: List[BaseLoan] = []
        self.clients: List[BaseClient] = []
        # self.ids: List[str]  # not needed

    def add_loan(self, loan_type: str):
        if loan_type not in self.LOAN_TYPES:
            raise Exception("Invalid loan type!")
        new_loan = self.LOAN_TYPES[loan_type]()
        self.loans.append(new_loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.CLIENT_TYPES:
            raise Exception("Invalid client type!")
        if len(self.clients) >= self.capacity:
            return "Not enough bank capacity."
        new_client = self.CLIENT_TYPES[client_type](client_name, client_id, income)
        self.clients.append(new_client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        loan = self._get_loan_by_type(loan_type)
        client = self._get_client_by_id(client_id)

        exception_message = "Inappropriate loan type!"
        if client.__class__.__name__ == "Student" and loan.__class__.__name__ != "StudentLoan":
            raise Exception(exception_message)
        if client.__class__.__name__ == "Adult" and loan.__class__.__name__ != "MortgageLoan":
            raise Exception(exception_message)

        client.loans.append(loan)
        self.loans.remove(loan)
        return f"Successfully granted {loan_type} to {client.name} with ID {client.client_id}."

    def remove_client(self, client_id: str):
        client = self._get_client_by_id(client_id)
        if not client:
            raise Exception("No such client!")
        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        changed_loans = len([l.increase_interest_rate() for l in self.loans if l.__class__.__name__ == loan_type])
        return f"Successfully changed {changed_loans} loans."

    def increase_clients_interest(self, min_rate: float):
        changed_rates = len([c.increase_clients_interest() for c in self.clients if c.interest < min_rate])
        return f"Number of clients affected: {changed_rates}."

    def get_statistics(self):
        total_clients_count = len(self.clients)
        total_clients_income = sum(c.income for c in self.clients)
        loans_count_granted_to_clients = sum([len(c.loans) for c in self.clients])
        granted_sum = sum([sum([l.amount for l in c.loans]) for c in self.clients])
        loans_count_not_granted = len([l for l in self.loans])
        not_granted_sum = sum([l.amount for l in self.loans])
        avg_client_interest_rate = sum(c.interest for c in self.clients) / len(self.clients) if self.clients else None
        result = f"""Active Clients: {total_clients_count}
Total Income: {total_clients_income:.2f}
Granted Loans: {loans_count_granted_to_clients}, Total Sum: {granted_sum:.2f}
Available Loans: {loans_count_not_granted}, Total Sum: {not_granted_sum:.2f}
Average Client Interest Rate: {avg_client_interest_rate:.2f}"""
        return result

    # helpers
    def _get_client_by_id(self, client_id):
        collection = [c for c in self.clients if c.client_id == client_id]
        return collection[0] if collection else None

    def _get_loan_by_type(self, loan_type):
        collection = [l for l in self.loans if l.__class__.__name__ == loan_type]
        return collection[0] if collection else None
