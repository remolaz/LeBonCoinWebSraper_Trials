from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import pandas as pd

myOptions = Options()
myOptions.add_argument("--disable-blink-features=AutomationControlled") 
# If the website is loaded with automation tools like Selenium, the value of navigator.webdriver is set to true. 
# This should set the value to false.

driver = Chrome(r"C:\Users\Remo\PycharmProjects\Prj1\chromedriver_win32\chromedriver.exe", options=myOptions)

url = "https://www.leboncoin.fr"

driver.get(url)

items = len(driver.find_elements_by_tag_name("http://schema.org/Offer"))

total = []
for item in range(items):
    quotes = driver.find_elements_by_name("http://schema.org/Offer")
    for quote in quotes:
        quote_text = quote.find_element_by_id("title").text
        author = quote.find_element_by_class_id("href").text
        new = ((quote_text, author))
        total.append(new)
df = pd.DataFrame(total, columns=['quote', 'author'])
df.to_csv('quoted.csv')

driver.close()
