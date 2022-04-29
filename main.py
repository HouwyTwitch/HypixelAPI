from libs.utils import authorize, loadSettings


SETTINGS = loadSettings()

if __name__ == '__main__':
    scrapper = authorize(SETTINGS['APIKey'])
    ownerID = scrapper.getOwner()
    print(scrapper.getPlayerData(ownerID))
    print(scrapper.getFriends(ownerID))