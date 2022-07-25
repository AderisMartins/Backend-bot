from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from asyncio import run


def automacaoWeb(rede_social: str, perfil: str):
    options = webdriver.ChromeOptions()
    options.add_argument('lang=pt-br')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    print("chegou aqui")
    if(rede_social == 'Instagram'):
        driver.get('https://www.instagram.com/')
        print("insta")
        time.sleep(10)
        driver.quit()
    elif(rede_social == 'Facebook'):
        driver.get('https://www.facebook.com/')
        print("face")
        time.sleep(10)
        driver.quit()
    #botao_face = driver.find_element_by_xpath(f"//span[@class='KPnG0']")
    #botao_face.click()
    #time.sleep(2)
    #botao = driver.find_element_by_xpath(f"'//input[@class=inputtext _55r1 inputtext _1kbt inputtext _1kbt']")
    #botao.click()


#if __name__ == '__main__':
 #   run(ScriptBot())
