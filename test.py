"""
A simple selenium test example written by python
"""

import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

class TestTemplate(unittest.TestCase):
    """Include test cases on a given url"""

    def setUp(self):
        """Start web driver"""
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(10)
        
    def tearDown(self):
        """Stop web driver"""
        self.driver.quit()

    def test_case_1(self):
        """TESTCASE 1 : TEST IF 'about' ELEMENT EXISTS"""
        try:
            about=[]
            self.driver.get(url)
            elem_about = self.driver.find_elements_by_css_selector('h1')
            for heading in elem_about:
                about.append(heading.text.lower())
            if "about" not in about:    
                self.fail("No heading found with 'about' text") 
        except NoSuchElementException as ex:
            self.fail(ex.msg)

    def test_case_2(self):
        """TESTCASE 2 : TEST IF 'img' ELEMENT EXISTS"""
        try:
            self.driver.get(url)
            elem_img = self.driver.find_element_by_tag_name('img')        
        except NoSuchElementException as ex:
            self.fail(ex.msg)
    def test_case_3(self):
        """TESTCASE 3 : FIND IF MULTIPLE PARAGRAPHS EXISTS WITH 100 CHARACTERS AT LEAST"""
        try:
            self.driver.get(url)
            elem_paras = self.driver.find_elements_by_css_selector('p') 
            word_count = 0
            para_list = []
            for paragraph in elem_paras:
                para_list = para_list+list(paragraph.text)
            Letter_count = len(para_list)
            assert(Letter_count >= 100000)
        except NoSuchElementException as ex:
            self.fail(ex.msg)
    def test_case_4(self):
        """TESTCASE 4: FIND 2 LINKS TO 2 BLOG POSTS"""
        try:
            self.driver.get(url)
            elems = self.driver.find_elements_by_css_selector('a')
            #for elem in elems:
            #   elem.click() 
            #current_url = self.driver.current_url
            links = [elem.get_attribute('href') for elem in elems]
            if len(links) < 2:
                self.fail("Two blog links are not present.")              
        except NoSuchElementException as ex:
            self.fail(ex.msg)
    def test_case_5(self):
        """TESTCASE 5: BLOG ONE HEADING SHOULD CONTAIN 'this course xxx'"""
        try:
            self.driver.get(url)
            elems = self.driver.find_elements_by_css_selector('a')
            links = [elem.get_attribute('href') for elem in elems]
            self.driver.get(links[0])
            hdrs=[]
            header = self.driver.find_elements_by_css_selector('h1')
            for heading in header:
                hdrs.append(heading.text.lower())
            if "".join(s for s in hdrs if "this course" in s.lower()) == "":
                self.fail("No header element has 'this course' text")
        except NoSuchElementException as ex:
            self.fail(ex.msg)  

    def test_case_6(self):
        """TESTCASE 6: BLOG ONE CONTAINS PARAGRAPHS OR UNORDERED LIST , WORD LIMIT : 250-500"""
        try:
            self.driver.get(url)
            elems = self.driver.find_elements_by_css_selector('a')
            links = [elem.get_attribute('href') for elem in elems]
            self.driver.get(links[0])
            
            elem_paras = self.driver.find_elements_by_css_selector('p') 
            para_list=[]
            for paragraph in elem_paras:
                para_list = para_list + list(paragraph.text)
            Letter_count = len(para_list)


            elem_list= self.driver.find_elements_by_tag_name("li")
            unordered_list=[]
            for li in elem_list:
                unordered_list = unordered_list + list(li.text)
            Letter_count_list = len(unordered_list)

            assert((Letter_count >= 250 and Letter_count <= 500) or (Letter_count_list >= 250 and Letter_count_list <= 500))
        except NoSuchElementException as ex:
            self.fail(ex.msg)  
    
    def test_case_7(self):
        """TESTCASE 8: BLOG TWO HEADING SHOULD CONTAIN 'learned xxx'"""
        try:
            self.driver.get(url)
            elems = self.driver.find_elements_by_css_selector('a')
            links = [elem.get_attribute('href') for elem in elems]
            self.driver.get(links[1])
            hdrs=[]
            header = self.driver.find_elements_by_css_selector('h1')
            for heading in header:
                hdrs.append(heading.text.lower())
            if "".join(s for s in hdrs if "learned" in s.lower()) == "":
                self.fail("No header element has 'learned' text")
        except NoSuchElementException as ex:
            self.fail(ex.msg)  

    def test_case_8(self):
        """TESTCASE 8: BLOG TWO CONTAINS PARAGRAPHS OR UNORDERED LIST , WORD LIMIT : 250-500"""
        try:
            self.driver.get(url)
            elems = self.driver.find_elements_by_css_selector('a')
            links = [elem.get_attribute('href') for elem in elems]
            self.driver.get(links[1])
            elem_paras = self.driver.find_elements_by_css_selector('p') 
            para_list=[]
            for paragraph in elem_paras:
                para_list = para_list + (list(paragraph.text))
            Letter_count = len(para_list)


            elem_list= self.driver.find_elements_by_tag_name("li")
            unordered_list=[]
            for li in elem_list:
                unordered_list = unordered_list + list(li.text)
            Letter_count_list = len(unordered_list)

            assert((Letter_count >= 250 and Letter_count <= 500) or (Letter_count_list >= 250 and Letter_count_list <= 500))

        except NoSuchElementException as ex:
            self.fail(ex.msg) 
      

url="https://asawarijoshi2501.github.io/selenium-test/"
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTemplate)
    unittest.TextTestRunner(verbosity=2).run(suite)
