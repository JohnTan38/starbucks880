from flask import Flask
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import Select
import time

app = Flask(__name__)

@app.route('/')
def home():
    driver = webdriver.Chrome()
    driver.get('https://az3.ondemand.esker.com/ondemand/webaccess/asf/home.aspx')
    driver.maximize_window()
    time.sleep(3)

    
    driver.find_element(By.XPATH, '//*[@id="ctl03_tbUser"]').send_keys("john.tan@sh-cogent.com.sg")
    driver.find_element(By.XPATH, '//*[@id="ctl03_tbPassword"]').send_keys("Esker3838")
    #company_code = driver.find_element(By.XPATH, '//*[@id="tpl_ih_adminList_displayedFilters_ctl00_ctl02_ddl1_tagify"]/span')
    #company_code.send_keys("SG80") #(2) input company code SG77
    time.sleep(0.5)
    actions = ActionChains(driver)
    actions.send_keys(Keys.TAB).perform()
    actions.send_keys(Keys.ENTER).perform()
    time.sleep(2)
    
    
    return "Login_Success"

if __name__ == "__main__":
    app.run(debug=True)
