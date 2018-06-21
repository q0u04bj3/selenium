import unittest, time, os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        PROJECT_DIR = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
        CHROMEDRIVER = os.path.join(PROJECT_DIR, 'chromedriver')
        self.driver = webdriver.Chrome(CHROMEDRIVER)

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        # wait 3 seconds
        time.sleep(3) 
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        time.sleep(3)
        elem.send_keys(Keys.RETURN)
        time.sleep(3)
        assert "No results found." not in driver.page_source


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
