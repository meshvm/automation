import requests
from bs4 import BeautifulSoup
import random
import re
import ast
import random

#url = "https://www.atg.party/sc.txt"

def fetch_values(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')
    body = soup.find('body')
    the_contents_of_body_without_body_tags = body.text
    return the_contents_of_body_without_body_tags

#value_of_elem = fetch_values("https://www.atg.party/sc.txt")

def get_data(id_val):
    value_of_elem = fetch_values("https://www.atg.party/sc.txt")
    lst = re.split('=|\n', value_of_elem)
    it = iter(lst)
    res_dct = dict(zip(it, it))
    k = ast.literal_eval(res_dct[id_val])
    return k


def randomizer(subject):
    j = get_data(subject)
    if (isinstance(j,dict)):
        topic, group = random.choice(list(j.items()))
        return (topic, group)
    else:
        location = random.choice(list(j))
        return(location)
if __name__ == "__main__":
    url = "https://www.atg.party/sc.txt"
    fetch_values(url)
    
    randomizer('interests')

