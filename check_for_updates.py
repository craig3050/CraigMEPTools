

# https://raw.githubusercontent.com/craig3050/CraigMEPTools/master/version.txt
# https://raw.githubusercontent.com/craig3050/CraigMEPTools/master/changelog.txt

import requests
from urllib.request import urlopen

class Check_For_Updates:
    #defining constructor
    def __init__(self):
        pass

    def return_version_number(self):
        URL = "https://raw.githubusercontent.com/craig3050/CraigMEPTools/master/version.txt"
        with urlopen(URL) as version_number:
            return str(version_number.read().decode())

    def return_change_log(self):
        URL = "https://raw.githubusercontent.com/craig3050/CraigMEPTools/master/changelog.txt"
        with urlopen(URL) as change_log:
            return str(change_log.read().decode())