from typing import List

from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms: List[Room] = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = 0
        for room in self.rooms:
            total_consumption += room.room_cost + room.expenses

        return f"Monthly consumptions: {total_consumption:.2f}$."

    def pay(self):
        result = []
        for room in self.rooms:
            if room.budget < room.expenses:
                self.rooms.remove(room)
                result.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
            else:
                total_expenses = room.expenses + room.room_cost
                room.budget -= room.expenses + room.room_cost
                result.append(f"{room.family_name} paid {total_expenses:.2f}$ and have {room.budget:.2f}$ left.")

        return "\n".join(result)

    def status(self):
        result = [f"Total population: {sum([r.members_count for r in self.rooms])}"]
        [result.append(str(r)) for r in self.rooms]

        return "\n".join(result)
