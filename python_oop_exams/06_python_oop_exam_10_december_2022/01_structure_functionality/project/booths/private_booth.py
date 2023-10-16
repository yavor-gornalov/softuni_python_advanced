from project.booths.booth import Booth


class PrivateBooth(Booth):
    PRICE_PER_PERSON = 3.5

    def get_price_per_person(self):
        return PrivateBooth.PRICE_PER_PERSON
