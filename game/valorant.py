import requests

from config.valorant_config import ValorantConfig
from constant.dpi import DPI
from constant.key_name import KeyName
from constant.time import Time
from constant.url import Url
from time import time as current_time


class Valorant:
    def __init__(self) -> None:
        self.name: str = ""
        self.tag: str = ""
        self.level: int = 0
        self.rank: str = ""
        self.elo: int = 0
        self.timestamp: float = 0.0
        self.sensitivity_aim = 0.35
        self.scoped_sensitivity_multiplier = 0.7

        self.update_data()

    def __getattr__(self, name):
        def _missing(*args, **kwargs):
            print(f"{type(self).__name__} missing method {name}, args : {args}, kwargs :  {kwargs}")
            return f"{type(self).__name__} has no {name}"

        return _missing

    def update_data(self):
        # ignore, when data is up to date
        if current_time() - self.timestamp < Time.UPDATE_PERIOD:
            return

        # get person data via rest API
        username = ValorantConfig.USERNAME
        tag = ValorantConfig.TAG
        region = ValorantConfig.REGION

        rank_url = Url.valorant_rank_url(username=username, tag=tag, region=region)
        stat_url = Url.valorant_stat_url(username=username, tag=tag)

        key_name = KeyName.valorant

        rank_json = requests.get(rank_url).json()[key_name.data]
        stat_json = requests.get(stat_url).json()[key_name.data]

        self.name = rank_json[key_name.name]
        self.tag = rank_json[key_name.tag]
        self.level = stat_json[key_name.account_level]
        self.rank = rank_json[key_name.currenttierpatched]
        self.elo = rank_json[key_name.elo]
        self.timestamp = current_time()

    def get_rank(self):
        self.update_data()

        output = [
            f"🎮🎮 Username 🎮🎮: {self.name}#{self.tag}",
            f"🏆🏆 Rank 🏆🏆: {self.rank} (elo: {self.elo})",
        ]
        return output

    def get_personal_information(self):
        self.update_data()

        output = [
            f"🎮🎮 Username 🎮🎮: {self.name}#{self.tag}",
            f"😎😎 Level 😎😎: {self.level}",
            f"🏆🏆 Rank 🏆🏆: {self.rank} (elo: {self.elo})",
        ]
        return output

    def get_dpi(self):

        output = [
            f"🐭🐭 DPI 🐭🐭: {DPI.DPI}",
            f"🖱🖱 Mouse Sensitivity 🖱🖱: {self.sensitivity_aim:.2f}",
            f"🏹🏹 ADS Mouse Sensitivity Multiplier 🏹🏹: {self.scoped_sensitivity_multiplier:.2f}",
        ]
        return output
