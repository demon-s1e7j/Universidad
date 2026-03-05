from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Selenium Manager automatically handles the driver setup
driver = webdriver.Chrome() 

driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
input("AYUDA")
driver.close()

def main():
    print("Hello from primeraentrega!")


if __name__ == "__main__":
    main()
