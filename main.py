import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url = 'https://accounts.google.com/ServiceLogin'
driver = uc.Chrome(use_chrome=True)
wait = WebDriverWait(driver, 10)
driver.get(url)
 
def login_google(email, password):
    wait.until(EC.visibility_of_element_located((By.NAME, 'identifier'))).send_keys(email + '\n')
    time.sleep(10)
    #class="whsOnd zHQkBf"
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input.whsOnd.zHQkBf'))).send_keys(password)
    time.sleep(15)
    
def pagina1(): 
    try:
        campo_email = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input.whsOnd.zHQkBf')))  # substitua pelo seletor correto do campo de email na página 1
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

    
email = 'nomasclips@gmail.com' # replace email
password = 'jorgetomas12'
login_google(email, password) # login
inquery = "https://docs.google.com/forms/d/e/1FAIpQLSf0t2Mducl6BfPnpOznfHUAhlejLFhrEbtDXp5Pm18PDzdWRQ/viewform"
driver.get(inquery)
time.sleep(10)

#Page 1
pagina1()

#Array of inputs  page 2     
inputs = driver.find_elements(By.CSS_SELECTOR, 'input[type="hidden"][name^="entry."]')
for index, input_element in enumerate(inputs):
    nome_campo = input_element.get_attribute('name')
    valor_atual = input_element.get_attribute('value')
    print("Indice:", index)
    print("Nome do campo<:", nome_campo)
    print("-------------------------")

time.sleep(130)


# wait.until(EC.)




#Page 2 


#Page 3 