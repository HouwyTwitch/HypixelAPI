import requests
from libs.exceptions import *
from libs.models import *
from libs.utils import *
import json


class HypixelAPIScrapper():
    def __init__(self, apiKey: str) -> None:
        self.session: requests.session = requests.session()
        self.owner: str = ''
        if type(apiKey) == str: self.headers = {'API-Key': apiKey}
        else: raise WrongAPIKey(ErrorMessages[-3])
        response: requests.Response = self.session.get(APIKeyInfo, headers = self.headers)
        checkStatusCode(response.status_code)
        self.owner = json.loads(response.content)['record']['owner']
    
    def getOwner(self) -> str: return self.owner
    
    def getPlayerData(self, uuid: str) -> dict: return oneParamRequest(Player, 'uuid', uuid, self.session, self.headers)
    
    def getFriends(self, uuid: str) -> dict: return oneParamRequest(Friends, 'uuid', uuid, self.session, self.headers)
        
    def getRecentGames(self, uuid: str) -> dict: return oneParamRequest(RecentGames, 'uuid', uuid, self.session, self.headers)
    
    def getStatus(self, uuid: str) -> dict: return oneParamRequest(Status, 'uuid', uuid, self.session, self.headers)
    
    def getGuild(self, id = None, player = None, name = None) -> dict:
        return threeParamsRequest(Guild, 'id', 'player', 'name', id, player, name, self.session, self.headers)
    
    def getStatus(self, uuid: str) -> dict: return oneParamRequest(RankedSkywars, 'uuid', uuid, self.session, self.headers)
    
    def getResourcesGames(self) -> dict: return simpleGetRequest(ResourcesGames, self.session, self.headers)
        
    def getResourcesAchievements(self) -> dict: return simpleGetRequest(ResourcesAchievements, self.session, self.headers)
    
    def getResourcesChallenges(self) -> dict: return simpleGetRequest(ResourcesChallenges, self.session, self.headers)
    
    def getResourcesQuests(self) -> dict: return simpleGetRequest(ResourcesQuests, self.session, self.headers)
    
    def getResourcesGuildsAchievements(self) -> dict: return simpleGetRequest(ResourcesGuildsAchievements, self.session, self.headers)
        
    def getResourcesVanityPets(self) -> dict: return simpleGetRequest(ResourcesVanityPets, self.session, self.headers)
    
    def getResourcesVanityCompanions(self) -> dict: return simpleGetRequest(ResourcesVanityCompanions, self.session, self.headers)
    
    def getResourcesSkyblockCollections(self) -> dict: return simpleGetRequest(ResourcesSkyblockCollections, self.session, self.headers)
        
    def getResourcesSkyblockSkills(self) -> dict: return simpleGetRequest(ResourcesSkyblockSkills, self.session, self.headers)
    
    def getResourcesSkyblockItems(self) -> dict: return simpleGetRequest(ResourcesSkyblockItems, self.session, self.headers)
    
    def getResourcesSkyblockElection(self) -> dict: return simpleGetRequest(ResourcesSkyblockElection, self.session, self.headers)
    
    def getResourcesSkyblockBingo(self) -> dict: return simpleGetRequest(ResourcesSkyblockBingo, self.session, self.headers)
    
    def getSkyblockNews(self) -> dict: return simpleGetRequest(SkyblockNews, self.session, self.headers)
    
    def getSkyblockAuction(self, uuid = None, player = None, profile = None) -> dict:
        return threeParamsRequest(SkyblockAuction, 'uuid', 'player', 'profile', uuid, player, profile, self.session, self.headers)
    
    def getSkyblockAuctions(self, page: int) -> dict: return oneParamRequest(SkyblockAuctions, 'page', page, self.session, self.headers)
    
    def getSkyblockAuctionsEnded(self) -> dict: return simpleGetRequest(SkyblockAuctionsEnded, self.session, self.headers)
    
    def getSkyblockBazaar(self) -> dict: return simpleGetRequest(SkyblockBazaar, self.session, self.headers)
    
    def getSkyblockProfile(self, profile: str) -> dict: return oneParamRequest(SkyblockProfile, 'profile', profile, self.session, self.headers)
    
    def getSkyblockProfiles(self, uuid: str) -> dict: return oneParamRequest(SkyblockProfiles, 'uuid', uuid, self.session, self.headers)
    
    def getSkyblockBingo(self) -> dict: return simpleGetRequest(SkyblockBingo, self.session, self.headers)
        
    def getBoosters(self) -> dict: return simpleGetRequest(Boosters, self.session, self.headers)
        
    def getCounts(self) -> dict: return simpleGetRequest(Counts, self.session, self.headers)
        
    def getLeaderboards(self) -> dict: return simpleGetRequest(Leaderboards, self.session, self.headers)
        
    def getPunishmentStats(self) -> dict: return simpleGetRequest(PunishmentStats, self.session, self.headers)