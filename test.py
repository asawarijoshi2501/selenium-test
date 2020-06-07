from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options


opts = Options()
opts.set_headless()
opts.add_argument("--headless")
assert opts.headless  # Operating in headless mode
browser = Firefox(options=opts)
browser.get('https://asawarijoshi2501.github.io/selenium-test/')

print("Test case 1 : find if element by id 'about' exists")
search_form = browser.find_element_by_id('about')
heading1 = driver.find_element_by_tag_name('h1')
assert((search_form) or heading1 == "about")


#print("Test case 1 : find if element by id 'image' exists")
#search_form = browser.find_element_by_id('image')
#assert(search_form)
