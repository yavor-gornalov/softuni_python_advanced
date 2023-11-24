from project.table.table import Table


class OutsideTable(Table):
    MIN_NUMBER = 51
    MAX_NUMBER = 100

    def __init__(self, table_number: int, capacity: int):
        super().__init__(table_number, capacity)

    @property
    def table_type(self):
        return "OutsideTable"

    @property
    def min_table_number(self):
        return OutsideTable.MIN_NUMBER

    @property
    def max_table_number(self):
        return OutsideTable.MAX_NUMBER
