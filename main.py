import sys
from bs4 import BeautifulSoup
import requests
sys.path.append('./rules')
from nodes import nodes
import rules

node = requests.get(nodes[6]).text
soup = BeautifulSoup(node,"lxml")
print(rules.getRule("blogspot.com")(soup).split())
