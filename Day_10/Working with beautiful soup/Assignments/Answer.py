# 1) find out all hyperlinks from a particular site.
'''
import requests
from bs4 import BeautifulSoup

page=requests.get("https://www.newyorker.com/")

soap=BeautifulSoup(page.text,'html.parser')
# print(soap.text)
links=soap.findAll("h3", attrs={"class":"BaseWrap-sc-gjQpdd BaseText-ewhhUZ SmartItemBaseText-iLrjJl SmartItemHed-dDDbYE iUEiRd DXClp dhnQBD eZpsfS smart-item__hed"})

for i in links:
    print(i.text)
'''


# 2) find out "src"s of all the images at a particular site.
import requests
from bs4 import BeautifulSoup

page=requests.get("https://www.newyorker.com/")

soap=BeautifulSoup(page.text,'html.parser')
# print(soap.text)
links=soap.findAll("h3", attrs={"class":"BaseWrap-sc-gjQpdd BaseText-ewhhUZ SmartItemBaseText-iLrjJl SmartItemHed-dDDbYE iUEiRd DXClp dhnQBD eZpsfS smart-item__hed"})

for i in links:
    print(i.src)



# links=soap.findAll("h3", attrs={"class":"BaseWrap-sc-gjQpdd BaseText-ewhhUZ SmartItemBaseText-iLrjJl SmartItemHed-dDDbYE iUEiRd DXClp dhnQBD eZpsfS smart-item__hed"})

# print(links.text)



# 3) go to "https://www.rediff.com/movies"
# and display all "href"s of a particular "div" class.

# 4) go to "https://docs.python.org/3/tutorial/index.html"
# and extract the first paragraph (<p>) of this page and display.






