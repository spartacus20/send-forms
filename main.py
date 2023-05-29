import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

url = 'https://docs.google.com/forms/d/e/1FAIpQLSf0t2Mducl6BfPnpOznfHUAhlejLFhrEbtDXp5Pm18PDzdWRQ/viewform'
driver = uc.Chrome(use_chrome=True)
wait = WebDriverWait(driver, 15)
driver.get(url)

def login_google(email, password):
    wait.until(EC.visibility_of_element_located((By.NAME, 'identifier'))).send_keys(email + '\n')
    time.sleep(10)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input.whsOnd.zHQkBf'))).send_keys(password)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="passwordNext"]/div/button'))).click()
    time.sleep(15)

def page1():
    try:
        campo_email = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input.whsOnd.zHQkBf')))
        valor_email = campo_email.get_attribute('value')
        if valor_email:
            print("O campo de email já está preenchido:", valor_email)
        else:
            campo_email.send_keys('efoxmundial@gmail.com')
        time.sleep(1)
        botao_seguinte = driver.find_element(By.CLASS_NAME, 'NPEfkd')
        botao_seguinte.click()
    except Exception as e:
        print("Erro ao preencher campo de email na página 1:", str(e))

email = 'ALMOST@gmail.com'  # substitua pelo seu email
password = 'AS'  # substitua pela sua senha
login_google(email, password)  # realizar login

# inquery = "https://docs.google.com/forms/d/e/1FAIpQLSf0t2Mducl6BfPnpOznfHUAhlejLFhrEbtDXp5Pm18PDzdWRQ/viewform"
# driver.get(inquery)
time.sleep(3)

# Page 1
page1()

# Array of inputs page 2
def obter_inputs_por_xpath(path, value):
    elemento1 = wait.until(EC.visibility_of_element_located((By.XPATH, path)))
    elemento1.click()
    elemento1.clear()
    elemento1.send_keys(value)

def click_option(path): 
    elemento1 = wait.until(EC.visibility_of_element_located((By.XPATH, path)))
    driver.execute_script("arguments[0].scrollIntoView();", elemento1)
    elemento1.click()

def page2():
    obter_inputs_por_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input', "Ana Santos") #Nome
    obter_inputs_por_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input', "912342843") #Telefone
    obter_inputs_por_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div[2]/textarea', "Rua das Flores") #Rua
    obter_inputs_por_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div/div[1]/input', "1000001") #Codigo Postal
    obter_inputs_por_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div[1]/div/div[1]/input', "Lisboa") #Localidade
    num_option = random.randint(1,4) 
    path_option = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/div/span/div/div[' + str(num_option) + ']'
    click_option(path_option)
    path_option1 = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[15]/div/div/div[2]/div/div/span/div/div[' + str(num_option) + ']'
    click_option(path_option1)
    
    
   
 



page2()

time.sleep(130)
