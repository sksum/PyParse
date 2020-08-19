specialRulesDict = {
    "digitalocean.com": "digitalOcean",
    "facebook.com": "facebook",
    "google.com/search": "googleSearch",
    "reddit.com": "reddit",
    "stackoverflow.com": "stackOverflow",
    "youtube.com": "youtube",
    "instagram.com": "instagram"
    }

def getRule(url):
    if url in specialRulesDict :
        importModule = 'import '+ specialRulesDict[url]
        exec (importModule)
        return eval(specialRulesDict[url]).getComponent
    else :
        import default
        return default.getComponent
