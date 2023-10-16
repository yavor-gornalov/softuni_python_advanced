from project.booths.booth import Booth


class OpenBooth(Booth):
    PRICE_PER_PERSON = 2.5

    def get_price_per_person(self):
        return OpenBooth.PRICE_PER_PERSON
