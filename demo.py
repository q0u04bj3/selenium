# -*- coding: UTF-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest, time, os

class KKBOXTestCase(unittest.TestCase):
    def setUp(self):
    	PROJECT_DIR = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
        CHROMEDRIVER = os.path.join(PROJECT_DIR, 'chromedriver')
        self.driver = webdriver.Chrome(CHROMEDRIVER)
        self.driver.get("https://play.kkbox.com")
        # login
        self.driver.find_element_by_id("uid").send_keys("*********@kkbox.com")
        self.driver.find_element_by_id("pwd").send_keys("*********")
        self.driver.find_element_by_id("login-btn").send_keys(Keys.ENTER)
        time.sleep(2)

    """def test_search_artist(self):
        driver = self.driver
        driver.find_element_by_tag_name("input").send_keys(u"韋禮安")
        time.sleep(1)
        driver.find_element_by_tag_name("input").send_keys(Keys.ENTER)
        time.sleep(2)
        search_result = driver.find_elements_by_css_selector("ul.cards.artists")
        time.sleep(1)
        for string in search_result:
            assert u"韋禮安+郭靜 (Weibird Wei+Claire Kuo)" in string.text"""


    def test_search_song(self):
        driver = self.driver
        driver.find_element_by_tag_name("input").send_keys(u"因為愛")
        time.sleep(1)
        driver.find_element_by_tag_name("input").send_keys(Keys.ENTER)
        time.sleep(3)
        # 取得歌曲 table
        song_table = self.driver.find_element_by_tag_name('table')
        # 取得每一列（橫向）
        rows = song_table.find_elements_by_tag_name('tr')
        # 第一列是項目名稱，我們不需要，所以只取第二列到最後一列 [1:] （list 教學 http://www.runoob.com/python/python-lists.html）
        for row in rows[1:]:
            # 取得第二欄（直向），歌曲名稱
            col = row.find_elements_by_tag_name('td')[1]
            print col.text
            assert u"因為愛" in col.text


    '''def test_search_song_list(self):
        driver = self.driver
        driver.find_element_by_tag_name("input").send_keys(u"韋禮安 (William Wei) 歷年精選")
        time.sleep(1)
        driver.find_element_by_tag_name("input").send_keys(Keys.ENTER)
        time.sleep(2)
        search_result = driver.find_elements_by_css_selector("ol.cards")
        time.sleep(1)
        for string in search_result:
            print string.text
            assert u"韋禮安 (William Wei) 歷年精選" in string.text'''


if __name__ == "__main__":
    unittest.main()