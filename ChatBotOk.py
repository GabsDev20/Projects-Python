from selenium import webdriver
import time
from datetime import datetime
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

hora = 16
minuto =3
segundo = 10

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(20)

while True:

    if datetime.today().weekday() !=7 and datetime.today().weekday() !=7:

        if time.localtime().tm_hour == int(hora) and time.localtime().tm_min == int(minuto) and time.localtime().tm_sec == int(segundo) or time.localtime().tm_hour == int(00) and time.localtime().tm_min == int(1) and time.localtime().tm_sec == int(00): 

            contatos = ['teste whatsappbot']
            mensagem = 'Testando 1.2.3...'

            #campo de pesquisa copyable-text selectable-text
            def busca_contato(contato):
                campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
                time.sleep(3)
                campo_pesquisa.click()
                campo_pesquisa.send_keys(contato)
                campo_pesquisa.send_keys(Keys.ENTER)

            #campo de mensagem copyable-text selectable-text
            def enviar_mensagem(mensagem):
                campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
                campo_mensagem[1].click()
                time.sleep(3)
                campo_mensagem[1].send_keys(mensagem)
                campo_mensagem[1].send_keys(Keys.ENTER)

            for contato in contatos:
                busca_contato(contato)
                enviar_mensagem(mensagem)