def getComponents(HtmlDoc,type):
    components = {}
    if type == "tutorial":
        components["title"] = HtmlDoc.find(class_="content-title Tutorial-header").text
        components["content"] = HtmlDoc.find(class_="content-body tutorial-content").text
    else : 
        components["title"] = HtmlDoc.find(class_="content-title").text
        components["question"] = HtmlDoc.find(class_="content-body question-content").text
        components["answers"] = HtmlDoc.find(class_="answers answers-container").text

    return components
