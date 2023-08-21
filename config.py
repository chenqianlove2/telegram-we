master_channel = 'plugins.eh_telegram_master', 'TelegramChannel'
slave_channels = [('plugins.eh_wechat_slave', 'WeChatChannel')]

eh_telegram_master = {
    "token": "6372101591:AAEjbF-12VFPNXniNGAxkWICO3jAPNqXcX8", # YOUR_TELEGRAM_BOT_TOKEN
    "admins": [5903436778],       # YOUR_TELEGRAM_ID
    "bing_speech_api": ["xxx", "xxx"],
    "baidu_speech_api": {
        "app_id": 0,
        "api_key": "xxx",
        "secret_key": "xxx"
    }
}
