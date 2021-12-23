from twitter_bot import InternetSpeedTwitterBot

bot = InternetSpeedTwitterBot()
results = bot.get_internet_speed()

download_speed = results["download_speed"]
upload_speed = results["upload_speed"]
if upload_speed < bot.up or download_speed < bot.down:
    bot.tweet_at_provider(upload_speed, download_speed)
else:
    print("Your internet speed is correct.")
