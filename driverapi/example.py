print("HELLO")
print("HELLO")
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


print("HELLO")
while True:
    try:
        driver = webdriver.Remote("http://firefox:4444/wd/hub", webdriver.DesiredCapabilities.FIREFOX.copy())
        driver.get("http://www.test.org")
        assert "Python" in driver.title
        elem = driver.find_element_by_name("q")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
        driver.close()
    except:
        pass
