from game.valorant import Valorant


class ValorantMethodMapping:
    def __init__(self) -> None:
        self.valorant = Valorant()

        self.method_mapping = {
            "rank": lambda: self.valorant.get_rank(),
            "info": lambda: self.valorant.get_personal_information(),
            "dpi": lambda: self.valorant.get_dpi(),
        }
