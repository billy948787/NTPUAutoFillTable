from selenium import webdriver
from selenium.webdriver import  ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
import pyperclip as pc
import time
from os import _exit


print('請選擇系統使用的瀏覽器(請輸入整數!),1:Chrome 2:Edge 3:Firefox')

try :
    browerType = eval(input())
except :
    print('輸入為非整數,程式將停止')
    time.sleep(1)
    _exit(0)

if browerType == 1:
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browerType == 2:
    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
elif browerType == 3:
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
else:
    print('輸入為未支援瀏覽器，程式將停止')
    time.sleep(1)
    _exit(0)



def main() :

    driver.get(r"https://ohs02.ntpu.edu.tw/student_new.htm");

    print('請輸入帳號:')
    account = input()
    print('請輸入密碼:')
    password = input()

    accountInput = driver.find_element_by_xpath("/html/body/table/tbody/tr/td[1]/table[3]/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/input")
    passwordInput = driver.find_element_by_xpath("/html/body/table/tbody/tr/td[1]/table[3]/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr[3]/td/input")
    loginButton = driver.find_element_by_xpath('''//*[@id="loginBtn1"]''')

    pc.copy(account)
    accountInput.send_keys(Keys.CONTROL, 'v')    
    pc.copy(password)
    passwordInput.send_keys(Keys.CONTROL, 'v')    

    loginButton.click()


    driver.get(r"https://ohs02.ntpu.edu.tw/pls/univer/g0002.eval_form.sel_course?date1=2024012165850")

    startLoop()
    
def startLoop():
    classList = driver.find_element_by_css_selector("body > center > table:nth-child(4)")

    rows = classList.find_elements_by_tag_name(name='tr')
    for row in rows :
        col = row.find_elements_by_tag_name(name='td')
        for element in col:
            try : 
                link = element.find_element_by_tag_name(name='a')
                href = link.get_attribute("href")
                driver.get(href)
                time.sleep(2)
            except : 
                continue
            fillSheet()
            sentSheet()
            startLoop()

def fillSheet():

    driver.find_element_by_xpath('/html/body/center/form/center[1]/table[1]/tbody/tr[4]/th[2]/input').click()
    driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[4]/th[2]/input').click()
    driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[5]/th[2]/input').click()
    driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[6]/th[2]/input').click()
    driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[7]/th[6]/input').click()
    driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[8]/th[2]/input').click()
    driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[9]/th[2]/input').click()
    driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[10]/th[2]/input').click()
    driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[11]/th[2]/input').click()
    driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[12]/th[2]/input').click()
    driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[13]/th[2]/input').click()
    driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[14]/th[6]/input').click()
    driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[15]/th[2]/input').click()
    driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[16]/th[2]/input').click()
    driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[17]/th[2]/input').click()
    driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[22]/th[2]/input').click()
    driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[23]/th[2]/input').click()
    driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[24]/th[2]/input').click()
    driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[26]/th[2]/input').click()
    driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[27]/th[2]/input').click()
    driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[28]/th[1]/div/input[2]').click()
    # drive
    driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[29]/th[1]/div/input[1]').click()
    # drive
    driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[30]/th[1]/div/input[2]').click()
    # drive
    driver.find_element_by_xpath('/html/body/center/form/center[1]/table[2]/tbody/tr[31]/th[1]/div/input[3]').click()
    # drive
        


def sentSheet():
    driver.find_element_by_xpath('/html/body/center/form/center[2]/input[5]').click()
    alert = driver.switch_to_alert()
    alert_text = alert.text
    alert.accept()
    


if __name__ == '__main__':
    main()
    print("已成功填寫!")
    driver.close()
    _exit(0)