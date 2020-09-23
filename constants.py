import os

class Config:
        ENV = bool(os.environ.get('ENV', False))
        if ENV:
                SPOTIFY_MODE = bool(os.environ.get('SPOTIFY_MODE', False))
                BOT_TOKEN = os.environ.get('BOT_TOKEN', None)
                
                API_ID = int(os.environ.get('API_ID', None))
                API_HASH = os.environ.get('API_HASH', None)
                SESSION_KEY = os.environ.get('SESSION_KEY', None)
                
                CMD_PREFIX = os.environ.get('CMD_PREFIX', '\?')
                
                CLIENT_ID = os.environ.get('CLIENT_ID', None)
                CLIENT_SECRET = os.environ.get('CLIENT_SECRET', None)
                
                INITIAL_TOKEN = os.environ.get('INITIAL_TOKEN', None)
                INITIAL_BIO = os.environ.get('INITIAL_BIO', None)
                
                BOTLOG = bool(os.environ.get('BOTLOG', True))
                LOG = os.environ.get('LOG', None)
                
                CONSOLE_LOGGER_VERBOSE = bool(os.environ.get('CONSOLE_LOGGER_VERBOSE', False))
                
                SCREENSHOT_LAYER_ACCESS_KEY = os.environ.get('SCREENSHOT_LAYER_ACCESS_KEY', None)
                OPEN_WEATHER_MAP_APPID = os.environ.get('OPEN_WEATHER_MAP_APPID', None)
                
                KEY = os.environ.get('KEY', '🎶')
                BIOS = [KEY + ' Vibing ; {interpret} - {title} {progress}/{duration}',
                        KEY + ' Vibing : {interpret} - {title}',
                        KEY + ' : {interpret} - {title}',
                        KEY + ' Vibing : {title}',
                        KEY + ' : {title}']
                OFFSET = 1
                # reduce the OFFSET from our actual 70 character limit
                LIMIT = 70 - OFFSET
        else:
                SPOTIFY_MODE = False
                CLIENT_ID = " "
                CLIENT_SECRET = " "
                API_ID = 123456
                API_HASH = " "
                SESSION_KEY = " "
                INITIAL_TOKEN = " "
                INITIAL_BIO = "Existence is painfull! Zoldyck Family™♥️//Spam here @MedevilofMarvel"
                SCREENSHOT_LAYER_ACCESS_KEY = None
                BOT_TOKEN = ' '
                BOTLOG = True 
                LOG = -100
                # the escaping is necessary since we are testing against a regex pattern with it.
                CMD_PREFIX = '\?' 
                # The key which is used to determine if the current bio was generated from the bot ot from the user. This means:
                # NEVER use whatever you put here in your original bio. NEVER. Don't do it!
                CONSOLE_LOGGER_VERBOSE = False

                KEY = '🎶'
                # The bios MUST include the key. The bot will go though those and check if they are beneath telegrams character limit.
                BIOS = [KEY + ' Vibing ; {interpret} - {title} {progress}/{duration}',
                        KEY + ' Vibing : {interpret} - {title}',
                        KEY + ' : {interpret} - {title}',
                        KEY + ' Vibing : {title}',
                        KEY + ' : {title}']

                OPEN_WEATHER_MAP_APPID = ' '
                # Mind that some characters (e.g. emojis) count more in telegram more characters then in python. If you receive an
                # AboutTooLongError and get redirected here, you need to increase the offset. Check the special characters you either
                # have put in the KEY or in one of the BIOS with an official Telegram App and see how many characters they actually
                # count, then change the OFFSET below accordingly. Since the standard KEY is one emoji and I don't have more emojis
                # anywhere, it is set to one (One emoji counts as two characters, so I reduce 1 from the character limit).
                OFFSET = 1
                # reduce the OFFSET from our actual 70 character limit
                LIMIT = 70 - OFFSET
