#deprecated beta version of the scraper
# DONT USE

import instaloader
import config


bot = instaloader.Instaloader()

for account in config.ACCOUNTS :
    profile = instaloader.Profile.from_username(bot.context, account)
    posts = profile.get_posts()
    #comments = profile.get_comments()

    count = 0

    for post in posts :
        if post.is_video:
            print("Downloading video posts {"+str(count+1)+"}")
            #comments = post.get_comments()
            #for comment in comments :
               # comment
            bot.download_post(post, target=profile.username)

            count += 1
            if count == config.FETCH_LIMIT:
                break

import instaloader
import sys
import os





# Now try to import the config module
try:
    import config
    print("config module imported successfully")
except ImportError as e:
    print("Error importing config module:", e)
    sys.exit(1)

# Print the attributes from the config file for debugging
print(f"USERNAME: {getattr(config, 'USERNAME', 'Not found')}")
print(f"PASSWORD: {getattr(config, 'PASSWORD', 'Not found')}")
print(f"ACCOUNTS: {getattr(config, 'ACCOUNTS', 'Not found')}")
print(f"FETCH_LIMIT: {getattr(config, 'FETCH_LIMIT', 'Not found')}")

bot = instaloader.Instaloader()

# Ensure the configuration attributes are available
if hasattr(config, 'USERNAME') and hasattr(config, 'PASSWORD') and hasattr(config, 'ACCOUNTS') and hasattr(config, 'FETCH_LIMIT'):
    bot.login(config.USERNAME, config.PASSWORD)

    for account in config.ACCOUNTS:
        profile = instaloader.Profile.from_username(bot.context, account)
        posts = profile.get_posts()

        count = 0

        for post in posts:
            if post.is_video:
                print(f"Downloading video post {count+1}")
                bot.download_post(post, target=profile.username)

                # Extract and print comments
                comments = post.get_comments()
                for comment in comments:
                    print(f"Comment by {comment.owner.username}: {comment.text}")

                count += 1
                if count == config.FETCH_LIMIT:
                    break
else:
    print("Configuration attributes missing in config.py")
