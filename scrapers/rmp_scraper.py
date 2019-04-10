import os
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

wd = webdriver.Chrome()

urls = []
with open("school_links.txt", "r") as f:
    for l in f:
        urls = l.split("/")

j = 0
urls = urls[1:]
for url in urls:
    print(j, len(urls))
    first_url = "http://www.ratemyprofessors.com/" + url

    wd.get(first_url)
    try:
        wd.find_element_by_class_name("close-this").click()
    except:
        print("no close this box")

    total_comments = {}
    try:
        WebDriverWait(wd, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "tbl-read-more-btn")))
    except:
        print("no read more box")
    try:
        element = wd.find_element_by_class_name("tbl-read-more-btn")
        while True:
            try:
                element.click()
                element = wd.find_element_by_id("loadMore")
            except:
                break
    except:
        print("cant load more there aint more")

    ratings_page = BeautifulSoup(wd.page_source, features="html.parser")
    ratings = ratings_page.find("table", attrs={"class": "school-ratings"})
    ratings_scores = ratings_page.find_all("div", attrs={"class": "rating"})

    i = 0
    for score in ratings_scores:
        if "Happiness" in score.contents[-2]:
            total_comments[i] = {}
            sign_place = str(score.contents[1]).find(">")
            happiness_score = str(score.contents[1])[sign_place+1]
            total_comments[i]["score"] = happiness_score
            i += 1
    children = ratings.tbody.findChildren("tr", recursive=False)
    children = children[1:]
    i = 0
    for child in children:
        try:
            if child['id'].isdigit():
                comment = child.p.contents[0].strip()
                total_comments[i]["comment"] = comment
                i += 1
        except:
            continue
    file_name = str(j) + ".json"
    path = os.path.join("comments", file_name)
    print("dumping json")
    with open(path, "w") as outfile:
        json.dump(total_comments, outfile, indent=True)
    j += 1

wd.quit()
