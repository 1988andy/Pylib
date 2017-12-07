import sys
sys.path.append("..")

from browser import Firefox, Chrome

d = Firefox('../../selenium-starter/drivers/geckodriver')
#d = Chrome('../../selenium-starter/drivers/chromedriver_mac64')
d.open('https://www.google.com')
d.type('#lst-ib', 'bndy.net')
d.click('.gb_P')
d.screenshot('aaa.png')
d.close()