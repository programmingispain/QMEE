from os import environ

SESSION_CONFIGS = [
     dict(
         name='centipede_game',
         display_name='Centipede',
         app_sequence=['centipede_game'],
         num_demo_participants=4,
         use_browser_bots=True,
     ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
This is a two-player six-foot centipede game with various representations. 
Since the free-of-charge Heroku server is not stable, please refresh the page if an error occurs.
"""


SECRET_KEY = '3984403655334'

INSTALLED_APPS = ['otree']
