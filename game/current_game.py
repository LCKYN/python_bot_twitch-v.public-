import requests

from config.twitch_api_config import TwitchApiConfig
from constant.key_name import KeyName
from constant.url import Url


class CurrentGame:
    def get_current_game(self):
        url = Url.current_twitch_information_url(TwitchApiConfig.USER_ID)
        headers = Url.current_twitch_information_header(
            bearer_token=TwitchApiConfig.TOKEN["access_token"],
            client_id=TwitchApiConfig.TOKEN["client_id"],
        )

        key_name = KeyName().current_game

        response = requests.request("GET", url, headers=headers, data={}).json()
        game_name = response[key_name.data][0][key_name.game_name]

        return game_name
