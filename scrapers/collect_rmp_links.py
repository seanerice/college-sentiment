from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

wd = webdriver.Chrome()

wd.get("http://www.ratemyprofessors.com/search.jsp?queryoption=HEADER&queryBy=schoolName&query=")
WebDriverWait(wd, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "filteroptions")))
results_page = BeautifulSoup(wd.page_source, features="html.parser")
steps = results_page.find_all(attrs={"class":"step"})
num_pages = steps[-1].contents

offset = 0
links = []

for i in range(int(num_pages[0])):
    print(offset, int(num_pages[0]))
    url = "http://www.ratemyprofessors.com/search.jsp?query=&queryoption=HEADER&stateselect=&country=&dept=&queryBy=schoolName&facetSearch=&schoolName=&offset="
    url += str(offset) + "&max=20"
    wd.get(url)
    WebDriverWait(wd, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "listings")))
    results_page = BeautifulSoup(wd.page_source, features="html.parser")
    listings = results_page.find_all(attrs={"class": "SCHOOL"})
    
    for l in listings:
        links.append(l.a.get("href"))

    i += 1
    offset += 20

f = open("school_links.txt", "w+")
for l in links:
    f.write(l)

f.close()
"""
wd.get("http://www.ratemyprofessors.com/campusRatings.jsp?sid=795")

wd.find_element_by_class_name("close-this").click()

WebDriverWait(wd, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "tbl-read-more-btn")))

element = wd.find_element_by_class_name("tbl-read-more-btn")
while True:
    try:
        element.click()
        element = wd.find_element_by_id("loadMore")
    except:
        break

html_page = wd.page_source
wd.quit()

soup = BeautifulSoup(html_page)
print(soup.find_all("a", {"class": "report"}))
"""
