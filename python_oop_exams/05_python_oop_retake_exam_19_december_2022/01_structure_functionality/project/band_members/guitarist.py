from project.band_members.musician import Musician


class Guitarist(Musician):
    TYPE_ = "Guitarist"

    @property
    def skills_available(self):
        return [
            "play metal",
            "play rock",
            "play jazz"
        ]
