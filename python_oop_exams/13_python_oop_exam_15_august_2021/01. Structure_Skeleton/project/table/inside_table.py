from project.table.table import Table


class InsideTable(Table):
    MIN_NUMBER = 1
    MAX_NUMBER = 50

    def __init__(self, table_number: int, capacity: int):
        super().__init__(table_number, capacity)

    @property
    def table_type(self):
        return "InsideTable"

    @property
    def min_table_number(self):
        return InsideTable.MIN_NUMBER

    @property
    def max_table_number(self):
        return InsideTable.MAX_NUMBER
