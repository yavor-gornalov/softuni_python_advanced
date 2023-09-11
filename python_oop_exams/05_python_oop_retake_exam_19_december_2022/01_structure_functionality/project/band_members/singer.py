from project.band_members.musician import Musician


class Singer(Musician):
    TYPE_ = "Singer"

    @property
    def skills_available(self):
        return [
            "sing high pitch notes",
            "sing low pitch notes"
        ]
