import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url = 'https://accounts.google.com/ServiceLogin'
driver = uc.Chrome(use_chrome=True)
wait = WebDriverWait(driver, 20)
driver.get(url)
 
def login_google(email):
    wait.until(EC.visibility_of_element_located((By.NAME, 'identifier'))).send_keys(email + '\n')
    time.sleep(15)
    
def pagina1(): 
    try:
        campo_email = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input.whsOnd.zHQkBf')))  # substitua pelo seletor correto do campo de email na página 1
        valor_email = campo_email.get_attribute('value')
        if valor_email: 
            print("O campo de email já está preenchido:", valor_email)
        else:
            campo_email.send_keys('efoxmundial@gmail.com')
        time.sleep(5)
        botao_seguinte = driver.find_element(By.CLASS_NAME, 'NPEfkd')
        botao_seguinte.click()
    except Exception as e:
        print("Erro ao preencher campo de email na página 1:", str(e))

    
email = 'nomasclips@gmail.com' # replace email
login_google(email) # login
inquery = "https://docs.google.com/forms/d/e/1FAIpQLSf0t2Mducl6BfPnpOznfHUAhlejLFhrEbtDXp5Pm18PDzdWRQ/viewform"
driver.get(inquery)
time.sleep(10)

#Page 1
pagina1()
wait.until()
    
time.sleep(130)


# wait.until(EC.)




#Page 2 


#Page 3 