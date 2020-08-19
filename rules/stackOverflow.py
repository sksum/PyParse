def getComponents(htmlDoc):
    components = {}
    components["title"] = htmlDoc.find("a", class_ = "question-hyperlink").text
    components["answers"] = []
    details = htmlDoc.findAll(class_ = "post-text")
    for i in range(len(details)):
        if i == 0 :
            components["question"] = details[i].text
        else :
            components["answers"].append(details[i].text);
    return components

