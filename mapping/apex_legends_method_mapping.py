from game.apex_legends import ApexLegends


class ApexLegendsMethodMapping:
    def __init__(self) -> None:
        self.apex_legends = ApexLegends()

        self.method_mapping = {
            "rank": lambda: self.apex_legends.get_battle_royale_data(),
            "br": lambda: self.apex_legends.get_battle_royale_data(),
            "arena": lambda: self.apex_legends.get_arena_data(),
            "info": lambda: self.apex_legends.get_personal_information(),
            "dpi": lambda: self.apex_legends.get_dpi(),
        }
