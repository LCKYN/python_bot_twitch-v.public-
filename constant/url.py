class Url:
    apex_legends_json_url = (
        lambda token, uid, platform: f"https://api.mozambiquehe.re/bridge?auth={token}&uid={uid}&platform={platform}"
    )

    current_twitch_information_url = lambda uid: f"https://api.twitch.tv/helix/channels?broadcaster_id={uid}"
    current_twitch_information_header = lambda bearer_token, client_id: {
        "Authorization": f"Bearer {bearer_token}",
        "Client-Id": f"{client_id}",
    }

    valorant_stat_url = lambda username, tag: f"https://api.henrikdev.xyz/valorant/v1/account/{username}/{tag}"
    valorant_rank_url = (
        lambda username, tag, region: f"https://api.henrikdev.xyz/valorant/v1/mmr/{region}/{username}/{tag}"
    )
