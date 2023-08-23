"""
This file contains the websites that needs to be checked.

"""

# Tuple of websites to be listed, paired with a fail counter
web_url = (
    ["https://www.jfcmnz.org/",0,''],
    ["https://www.steeliespecialists.co.nz/",0,''],
    ["https://nickskitchen.co.nz/",0,''],
    ["https://the-internet.herokuapp.com/status_codes/301",0,'']
)

# Dictionary of website to organization equivalent
hostnames = {
    "https://www.jfcmnz.org/": "JFCM",
    "https://www.steeliespecialists.co.nz/": "Steelie Specialist",
    "https://nickskitchen.co.nz/": "Nick's Kitchen",
    "https://the-internet.herokuapp.com/status_codes/301": "Heroku App"
}