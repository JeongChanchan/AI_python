from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
browser = webdriver.Chrome(options=options)

browser.maximize_window()

url = 'https://flight.naver.com'
browser.get(url)

browser.get_screenshot_as_file('data/flight.png')
browser.quit()