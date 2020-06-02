from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options


opts = Options()
opts.set_headless()
assert opts.headless  # Operating in headless mode
browser = Firefox(options=opts)
browser.get('https://asawarijoshi2501.github.io/selenium-test/')

print("Test case 1 : find if element by id 'about' exists")
search_form = browser.find_element_by_id('about')
assert(search_form):


print("Test case 1 : find if element by id 'image' exists")
search_form = browser.find_element_by_id('image')
assert(search_form):







