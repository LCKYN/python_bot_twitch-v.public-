from regex import D
import requests

from config.apex_legends_config import ApexLegendsConfig
from constant.dpi import DPI
from constant.key_name import KeyName
from constant.time import Time
from constant.url import Url
from time import time as current_time


class ApexLegends:
    def __init__(self) -> None:
        self.name: str = ""
        self.level: int = 0
        self.battle_royale_rank: str = ""
        self.battle_royale_score: int = 0
        self.arena_rank: str = ""
        self.arena_score: int = 0
        self.timestamp: float = 0.0
        self.mouse_sensitivity = 0.9
        self.ads_mouse_sensitivity_multiplier = 1.0
        self.per_optic_ads_sensitivity = False
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
        token = ApexLegendsConfig.TOKEN
        uid = ApexLegendsConfig.UID
        platform = ApexLegendsConfig.PLATFORM

        url = Url.apex_legends_json_url(
            token=token,
            uid=uid,
            platform=platform,
        )

        key_name = KeyName.apex_legends

        raw_json = requests.get(url).json()
        account_data = raw_json[key_name.global_tag]
        battle_royale_data = account_data[key_name.battle_royale_tag]
        arena_data = account_data[key_name.arena_tag]

        # update data
        self.name = account_data[key_name.name_tag]
        self.level = account_data[key_name.level_tag]
        self.battle_royale_rank = battle_royale_data[key_name.rank_name_tag]
        self.battle_royale_score = battle_royale_data[key_name.rank_score_tag]
        self.arena_rank = arena_data[key_name.rank_name_tag]
        self.arena_score = arena_data[key_name.rank_score_tag]
        self.timestamp = current_time()

    def get_battle_royale_data(self):
        self.update_data()

        key_name = KeyName.apex_legends

        raw_output = {
            key_name.name_tag: self.name,
            key_name.rank_name_tag: self.battle_royale_rank,
            key_name.rank_score_tag: self.battle_royale_score,
        }

        output = [
            f"🎮🎮 Username 🎮🎮: {raw_output[key_name.name_tag]}",
            f"🏆🏆 Rank 🏆🏆: {raw_output[key_name.rank_name_tag]}({raw_output[key_name.rank_score_tag]})",
        ]

        return output

    def get_arena_data(self):
        self.update_data()

        key_name = KeyName.apex_legends

        raw_output = {
            key_name.name_tag: self.name,
            key_name.rank_name_tag: self.arena_rank,
            key_name.rank_score_tag: self.arena_score,
        }

        output = [
            f"🎮🎮 Username 🎮🎮: {raw_output[key_name.name_tag]}",
            f"🏆🏆 Rank 🏆🏆: {raw_output[key_name.rank_name_tag]}({raw_output[key_name.rank_score_tag]})",
        ]

        return output

    def get_personal_information(self):
        self.update_data()

        key_name = KeyName.apex_legends

        raw_output = {
            key_name.name_tag: self.name,
            key_name.level_tag: self.level,
            key_name.rank_name_tag: self.battle_royale_rank,
            key_name.rank_score_tag: self.battle_royale_score,
        }

        output = [
            f"🎮🎮 Username 🎮🎮: {raw_output[key_name.name_tag]}",
            f"😎😎 Level 😎😎: {raw_output[key_name.level_tag]}",
            f"🏆🏆 Rank 🏆🏆: {raw_output[key_name.rank_name_tag]}({raw_output[key_name.rank_score_tag]})",
        ]
        return output

    def get_dpi(self):
        per_optic_ads_sensitivity = "On" if self.per_optic_ads_sensitivity else "Off"

        output = [
            f"🐭🐭 DPI 🐭🐭: {DPI.DPI}",
            f"🖱🖱 Mouse Sensitivity 🖱🖱: {self.mouse_sensitivity:.2f}",
            f"🏹🏹 ADS Mouse Sensitivity Multiplier 🏹🏹: {self.ads_mouse_sensitivity_multiplier:.2f}",
            f"🙈🙈 Per Optic ADS Sensitivity 🙈🙈: {per_optic_ads_sensitivity}",
        ]
        return output
