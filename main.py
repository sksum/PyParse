import sys
from bs4 import BeautifulSoup
import requests
sys.path.append('./rules')
from nodes import nodes
import rules

rawData= [] 
print('ok')
for node in nodes:
    node = requests.get(node).text
    soup = BeautifulSoup(node,"lxml")
    doc = rules.getRule(".com")(soup)
    #print(doc)
    rawData.append(doc)
