specialRulesDict = {
    "digitalocean.com": "digitalOcean",
    "facebook.com": "facebook",
    "google.com/search": "googleSearch",
    "reddit.com": "reddit",
    "stackoverflow.com": "stackOverflow",
    "youtube.com": "youtube",
    }

def getRule(url):
    if url in specialRulesDict :
        importModule = 'import '+ specialRulesDict[url]
        exec (importModule)
        return eval(specialRulesDict[url]).getComponents
    else :
        import default
        return default.getComponents
