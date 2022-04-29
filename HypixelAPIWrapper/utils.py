from libs.HypixelAPIScrapper import HypixelAPIScrapper
import json

def authorize(apiKey: str) -> HypixelAPIScrapper:
    return HypixelAPIScrapper(apiKey)

def loadSettings(filename: str = 'settings.json') -> dict:
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    return json.loads(content)
        