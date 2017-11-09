import time

from selenium import webdriver
from lxml import html

def get_html():
    # driver = webdriver.Chrome()
    driver = webdriver.PhantomJS()
    driver.get('https://888.qq.com/v1.0/award/index.html?bc_tag=40094.3.37')
    time.sleep(10)

    try:
        response = html.fromstring(driver.page_source)
        return response
    except:
        return None
    finally:
        driver.close()