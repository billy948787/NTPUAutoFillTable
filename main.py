from selenium import webdriver
from selenium.webdriver import  ActionChains
from selenium.webdriver.common.keys import  Keys
import time
import os




driver = webdriver.Edge('./msedgedriver')
def main() :
    driver.get(r"https://ohs02.ntpu.edu.tw/student_new.htm");

    # account = input()
    # password = input()
    account = '411285040'
    password = 'H70471215'

    accountInput = driver.find_element_by_xpath("/html/body/table/tbody/tr/td[1]/table[3]/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/input")
    passwordInput = driver.find_element_by_xpath("/html/body/table/tbody/tr/td[1]/table[3]/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr[3]/td/input")
    loginButton = driver.find_element_by_xpath('''//*[@id="loginBtn1"]''')

    ActionChains(driver)\
        .send_keys_to_element(accountInput, account)\
        .send_keys_to_element(passwordInput, password)\
        .click(loginButton)\
        .perform()

    driver.get(r"https://ohs02.ntpu.edu.tw/pls/univer/g0002.eval_form.sel_course?date1=2024012165850")

    startLoop()
    
def startLoop():
    classList = driver.find_element_by_css_selector("body > center > table:nth-child(4)")

    rows = classList.find_elements_by_tag_name(name='tr')
    for row in rows :
        col = row.find_elements_by_tag_name(name='td')
        for element in col:
            try : 
                print('Can click',element.text)
                link = element.find_element_by_tag_name(name='a')
                href = link.get_attribute("href")
                driver.get(href)
                print(href)
                time.sleep(2)
            except : 
                continue
            fillSheet()
            sentSheet()
            startLoop()

def fillSheet():

    driver.find_element_by_xpath('/html/body/center/form/center[1]/table[1]/tbody/tr[4]/th[2]/input').click()
    # driver.find_element_by_xpath('/html/body/center/form/center[1]/table[1]/tbody/tr[4]/th[2]/input').send_keys(Keys.space)
    driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[4]/th[2]/input').click()
    # driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[4]/th[2]/input').send_keys(Keys.space)
    driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[5]/th[2]/input').click()
    # driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[5]/th[2]/input').send_keys(Keys.space)
    driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[6]/th[2]/input').click()
    # driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[6]/th[2]/input').send_keys(Keys.space)
    driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[7]/th[6]/input').click()
    # driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[7]/th[6]/input').send_keys(Keys.space)
    driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[8]/th[2]/input').click()
    # driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[8]/th[2]/input').send_keys(Keys.space)
    driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[9]/th[2]/input').click()
    # driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[9]/th[2]/input').send_keys(Keys.space)
    driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[10]/th[2]/input').click()
    # driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[10]/th[2]/input').send_keys(Keys.space)
    driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[11]/th[2]/input').click()
    # driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[11]/th[2]/input').send_keys(Keys.space)
    driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[12]/th[2]/input').click()
    # driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[12]/th[2]/input').send_keys(Keys.space)
    driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[13]/th[2]/input').click()
    # driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[13]/th[2]/input').send_keys(Keys.space)
    driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[14]/th[6]/input').click()
    # driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[14]/th[6]/input').send_keys(Keys.space)
    driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[15]/th[2]/input').click()
    # driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[15]/th[2]/input').send_keys(Keys.space)
    driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[16]/th[2]/input').click()
    # driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[16]/th[2]/input').send_keys(Keys.space)
    driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[17]/th[2]/input').click()
    # driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[17]/th[2]/input').send_keys(Keys.space)
    driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[22]/th[2]/input').click()
    # driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[22]/th[2]/input').send_keys(Keys.space)
    driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[23]/th[2]/input').click()
    # driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[23]/th[2]/input').send_keys(Keys.space)
    driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[24]/th[2]/input').click()
    # driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[24]/th[2]/input').send_keys(Keys.space)
    driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[26]/th[2]/input').click()
    # driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[26]/th[2]/input').send_keys(Keys.space)
    driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[27]/th[2]/input').click()
    # driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[27]/th[2]/input').send_keys(Keys.space)
    driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[28]/th[1]/div/input[2]').click()
    # driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[28]/th[1]/div/input[2]').send_keys(Keys.space)
    driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[29]/th[1]/div/input[1]').click()
    # driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[29]/th[1]/div/input[1]').send_keys(Keys.space)
    driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[30]/th[1]/div/input[2]').click()
    # driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[30]/th[1]/div/input[2]').send_keys(Keys.space)
    driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[31]/th[1]/div/input[3]').click()
    # driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[31]/th[1]/div/input[3]').send_keys(Keys.space)
        


def sentSheet():
    driver.find_element_by_xpath('/html/body/center/form/center[2]/input[5]').click()
    alert = driver.switch_to_alert()
    alert_text = alert.text
    alert.accept()
    




if __name__ == '__main__':
    main()
    time.sleep(5)
    driver.close()