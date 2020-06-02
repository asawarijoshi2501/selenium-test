from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options


opts = Options()
opts.set_headless()
assert opts.headless  # Operating in headless mode
browser = Firefox(options=opts)
browser.get('https://asawarijoshi2501.github.io/selenium-test/')
search_form = browser.find_element_by_id('about')
assert(search_form)


