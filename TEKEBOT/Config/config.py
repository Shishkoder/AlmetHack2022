import json


def getToken() -> str:
    """
    Function to get bot token

    Returns:
        str: Bot token
    """
    with open("TEKEBOT\Config\config.json", "r", encoding="utf-8") as file_cfg:
        cfg_dict = json.load(file_cfg)

    return cfg_dict['BOT_TOKEN']


def getAdminIdList() -> list[int, int]:
    """
    Function to get a list of administrators

    Returns:
        list[int, int]: list of administration
    """
    with open("TEKEBOT\Config\config.json", "r", encoding="utf-8") as file_cfg:
        cfg_dict = json.load(file_cfg)

    return cfg_dict['ADMIN_ID']


def get_service_channel_chat_id() -> int:
    """
    Function to get chat_id 

    Returns:
        int: chat_id 
    """
    with open("TEKEBOT\Config\config.json", "r", encoding="utf-8") as file_cfg:
        cfg_dict = json.load(file_cfg)
    
    return cfg_dict['CHAT_SERVICE_CHANNEL']
