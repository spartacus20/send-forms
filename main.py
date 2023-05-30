import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from selenium.webdriver.common.keys import Keys
import pandas as pd





url = 'https://docs.google.com/forms/d/e/1FAIpQLSf0t2Mducl6BfPnpOznfHUAhlejLFhrEbtDXp5Pm18PDzdWRQ/viewform'
driver = uc.Chrome(use_chrome=True)
wait = WebDriverWait(driver, 15)
driver.get(url)

data = pd.read_excel(r'C:/Users/veget/OneDrive/Desktop/nu/joca/formulario.xlsx')
df = pd.DataFrame(data, columns=['Nome', 'Telefone', 'Morada', 'Código Postal', 'Localidade'])
print(df["Código Postal"])

def login_google(email, password):
    wait.until(EC.visibility_of_element_located((By.NAME, 'identifier'))).send_keys(email + '\n')
    time.sleep(10)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input.whsOnd.zHQkBf'))).send_keys(password)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="passwordNext"]/div/button'))).click()
    time.sleep(15)

def page1():
    try:
        campo_email = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input.whsOnd.zHQkBf')))
        campo_email.click()
        campo_email.clear()
        campo_email.send_keys('efoxmundial@gmail.com')
        valor_email = campo_email.get_attribute('value')            
        time.sleep(1)
        botao_seguinte = driver.find_element(By.CLASS_NAME, 'NPEfkd')
        botao_seguinte.click()
    except Exception as e:
        print("Erro ao preencher campo de email na página 1:", str(e))

email = 'emai@gmail.com'  # substitua pelo seu email
password = 'as'  # substitua pela sua senha
login_google(email, password)  # realizar login
time.sleep(1)


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

def change_input_data(year, month, day): 
   
    path_date1 = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input'
    # elemento_data = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')
    elemento_data = wait.until(EC.element_to_be_clickable((By.XPATH, path_date1)))
    driver.execute_script("arguments[0].scrollIntoView();", elemento_data)
    elemento_data.click()
    elemento_data.clear()
    elemento_data.send_keys(year)
    time.sleep(5)
    elemento_data.send_keys(Keys.ARROW_LEFT)
    time.sleep(1)
    elemento_data.send_keys(month)
    elemento_data.send_keys(Keys.ARROW_LEFT)
    time.sleep(1)
    elemento_data.send_keys(Keys.ARROW_LEFT)
    elemento_data.send_keys(day)
    time.sleep(1)
    
def page2(name, phone, address, zipcode,city):
    obter_inputs_por_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input', name) #Nome
    time.sleep(1)
    obter_inputs_por_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input', phone) #Telefone
    time.sleep(1)
    obter_inputs_por_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div[2]/textarea', address) #Rua
    time.sleep(1)
    obter_inputs_por_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div/div[1]/input', zipcode) #Codigo Postal
    time.sleep(1)
    obter_inputs_por_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div[1]/div/div[1]/input', city) #Localidade
    time.sleep(1)
    num_option = random.randint(1,4) 
    path_option = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/div/span/div/div[' + str(num_option) + ']'
    click_option(path_option)
    
    year = random.randint(2024,2025) 
    month = random.randint(3,12) 
    day = random.randint(1,30) 
    change_input_data(year, month, day)
    time.sleep(2)
    path_option_nao = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div/div/span/div/div[2]'
    click_option(path_option_nao)
  
    time.sleep(1)
    path_option2 = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[15]/div/div/div[2]/div/div/span/div/div[' + str(num_option) + ']'
    click_option(path_option2)
    time.sleep(1)
    
    obter_inputs_por_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[17]/div/div/div[2]/div/div[1]/div[2]/textarea', "Nada")
    time.sleep(1)
    obter_inputs_por_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[19]/div/div/div[2]/div/div[1]/div[2]/textarea', "Satisfeito")
    time.sleep(2)
    btn_next = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span')
    btn_next.click()
      
def page3(): 
    
    obter_inputs_por_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input', "Jorge Lucas") #Nome
    time.sleep(2)
    click_option('//span[contains(text(),"Tiago Martins - Peixe")]')
    click_option('//*[@id="i29"]')
    time.sleep(5)
    click_option('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[3]/div[1]/div[2]/span')
    time.sleep(2)
    click_option('/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    

for i in range(len(df)): 
    page1()
    time.sleep(5)
    try:
        page2(df['Nome'][i], str(df['Telefone'][i]), df['Morada'][i], str(df['Código Postal'][i]), df['Localidade'][i])
    except Exception as e:
        page2(df['Nome'][i], str(df['Telefone'][i]), df['Morada'][i], str(df['Código Postal'][i]), df['Localidade'][i])
    
    try:
        page3()
    except Exception as e:
        page3()
        
    print("Acabei o processo do: ", i)
    
# page1()
# time.sleep(5)
# try: 
#     page2("André Pereira","923847343", "Rua dos Lírios", "4000004", "Porto")
# except Exception as e: 
#     page2("André Pereira","923847343", "Rua dos Lírios", "4000004", "Porto")
# time.sleep(1)
# try: 
#     page3()
# except Exception as e: 
#     page3()

# time.sleep(130)
