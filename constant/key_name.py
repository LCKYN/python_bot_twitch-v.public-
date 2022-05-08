class KeyName:
    apex_legends = {
        "global_tag": "global",
        "name_tag": "name",
        "level_tag": "level",
        "battle_royale_tag": "rank",
        "arena_tag": "arena",
        "rank_name_tag": "rankName",
        "rank_score_tag": "rankScore",
    }
    apex_legends = type("ApexLegendsKeyName", (object,), apex_legends)()

    current_game = {
        "data": "data",
        "game_name": "game_name",
    }
    current_game = type("CurrentGameKeyName", (object,), current_game)()

    valorant = {
        "data": "data",
        "name": "name",
        "tag": "tag",
        "account_level": "account_level",
        "currenttierpatched": "currenttierpatched",
        "elo": "elo",
    }
    valorant = type("ValorantKeyName", (object,), valorant)()
