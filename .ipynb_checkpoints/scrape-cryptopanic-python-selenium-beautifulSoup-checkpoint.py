# we want to go to the site: "https://cryptopanic.com/" and 
# # press on accept button and 
# # list all news titles and related links in a csv or Json file
from selenium import webdriver 
from bs4 import BeautifulSoup 
import csv 
# https://selenium-python.readthedocs.io/locating-elements.html
from selenium.webdriver.common.by import By

# open the chrome explorer
driver = webdriver.Chrome()
url="https://cryptopanic.com/"

driver.get(url)

# from the html/body find tag "a" that contains the text "Accept"
link_button=driver.find_elements(By.XPATH, '//a[text()="Accept"]')
# print(link_button[0].text())

# click on Accept
link_button.click()

# the 2 methods that we can find the element which we want
#---
#0. the "//" means "html/body/"
# test = driver.find_element(By.XPATH, '//div')
# test.get_attribute('outerHTML')
#---
#2. the "./*" means "first level children of current element"
# testchild=driver.find_elements(By.XPATH, "./*")
# len(testchild)
# testchild[0].get_attribute('outerHTML') # this should be 'html' tag.
# testchid2=testchild[0].find_elements(By.XPATH, "./*")
# testchid2[1].get_attribute('outerHTML') # this should be 'body' tag.
# testchid3=testchid2[1].find_elements(By.XPATH, "./*")
# len(testchid3)
# testchid3[0].get_attribute('outerHTML') # this should be 'div.app-layout' tag.
# testchild4=testchid3[0].find_elements(By.XPATH, "./*")
# len(testchild4) # all three 'div' tag in it. if we do not click on accept link_bottom here we have 4 tags.
# testchild4[2].get_attribute('outerHTML') ### this should be 'div.app-right-pane' tag.
#---
#3. go directly to the element.
# test1_child=driver.find_element(By.XPATH, "/html/body/div[1]/div[3]") # maybe, with this method we don't have zero index
# test1_child.get_attribute('outerHTML') ### this should be 'div.app-right-pane' tag.
#=== end of methods
# test2_byClass = driver.find_elements(By.CLASS_NAME, 'news-row')
# test2_byClass[0].find_elements(By.CLASS_NAME,"nc-title")
# =================== from here I decide to get here by BeautifulSoup 
# =================== so after doing an action we can use BeautifulSoup
html = driver.page_source
soup = BeautifulSoup(html,'html.parser')
main_div = soup.find("div",class_="news")
row_div = main_div.find_all("div",class_="news-row")
# len(row_div)
# ref0 = row_div[0].find("a",class_="nc-title")['href']
# title0 = row_div[0].find("a",class_="nc-title").span.span.text.strip()
# url.rstrip("/")+ref0
results=[]
for row in row_div:
    result_row={}
    result_row['news_title']=row.find("a",class_="nc-title").span.span.text.strip()
    result_row['news_link']=url.rstrip("/")+row.find("a",class_="nc-title")['href']
    results.append(result_row) 
# len(results)
# results
domain = "cryptopanic.com"
filename = domain + '.csv'
with open(filename, 'w', newline='') as f: 
    w = csv.DictWriter(f,['news_title','news_link']) 
    w.writeheader() 
    for result_row in results: 
        w.writerow(result_row) 