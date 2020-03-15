from selenium.webdriver import Chrome
import pandas as pd

driver = Chrome(r"C:\Users\Remo\PycharmProjects\Prj1\chromedriver_win32\chromedriver.exe")

pages = 2

for page in range(1, pages):

    url = "http://quotes.toscrape.com/js/page/" + str(page) + "/"

    driver.get(url)

    items = len(driver.find_elements_by_class_name("quote"))

    total = []
    for item in range(items):
        quotes = driver.find_elements_by_class_name("quote")
        for quote in quotes:
            quote_text = quote.find_element_by_class_name('text').text[1:-2]
            author = quote.find_element_by_class_name('author').text
            new = ((quote_text, author))
            total.append(new)
    df = pd.DataFrame(total, columns=['quote', 'author'])
    df.to_csv('quoted.csv')
driver.close()

# References:
# https://dev.to/lewiskori/beginner-s-guide-to-web-scraping-with-python-s-selenium-3fl9
# https://dev.to/endtest/a-practical-guide-for-finding-elements-with-selenium-4djf
