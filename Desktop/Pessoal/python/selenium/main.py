from selenium import webdriver
from time import sleep

navegador = webdriver.Chrome()

while(True):
    navegador.get('https://www.google.com/search?q=pre%C3%A7o+do+dolar&rlz=1C1GCEU_pt-BRBR973BR973&oq=&aqs=chrome.1.69i59i450l8.140867423j0j15&sourceid=chrome&ie=UTF-8')
    
    valor =  navegador.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').text
    print('=====================')
    print("Preço do dólar convertido em Real brasileiro: " + valor)
    print('=====================')
    

    sleep(10)


