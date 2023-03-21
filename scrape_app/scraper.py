from time import sleep
from random import randint
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import json

def scrape_walmart(url):       
   
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')    
    driver = WebDriver(options=options)
    
    # get al sitio

    print(url)
    driver.get(url)
    sleep(randint(2,3))
  
    


    try:    
        # verificación click & hold
        element = driver.find_element(By.XPATH, "//div[@id='px-captcha']")
        action = ActionChains(driver)
        action.move_to_element_with_offset(element, 0, 0).click_and_hold().perform()
        sleep(10)
        action.release(element)
        action.perform()
        sleep(0.2)
        action.release(element)
        # verificación click & hold
        sleep(1)
        print('Click & hold verificado')
        sleep(5)
    except:
        # no hay hold&click
        print('no hay click and hold')

    categorias = []
    #data_item_ids_guardados = {}
    contador = 0
    for div_categoria in driver.find_elements(By.CSS_SELECTOR, 'div[class="mv3 mv4-xl ml3 ml0-l bb b--near-white"]'):
        contador+=1
        texts = div_categoria.text.splitlines()
        uno = texts[0]
        print(uno)
        
        try:
            texts = div_categoria.text.splitlines()
            uno = texts[0]
            print(uno)
        
            categoria = {
                'nombre': driver.find_element(By.XPATH, "//h2[text()='" + uno + "']").text,
                'productos': []
            }

    
            for li_producto in div_categoria.find_elements(By.CSS_SELECTOR, 'li[class="flex flex-column items-center pa1 pr2 pb2"]'):
                aux_producto = li_producto.find_element(By.CSS_SELECTOR, 'div[class="sans-serif mid-gray relative flex flex-column w-100 h-100 hide-child-opacity"]').get_attribute("data-item-id")
                #if  aux_producto not in data_item_ids_guardados:

                producto = {
                    'nombre_producto': li_producto.find_element(By.CSS_SELECTOR, 'span[class="normal dark-gray mb0 mt1 lh-title f6 f5-l"]').text,
                    'img_uri': li_producto.find_element(By.CSS_SELECTOR, 'div[class="relative"]').find_element(By.TAG_NAME, 'img').get_attribute('src')
                }

        
                precios_div = li_producto.find_element(By.CSS_SELECTOR, 'div[class="flex flex-wrap justify-start items-center lh-title mb2 mb1-m"]')
                
                try:            
                    precio_descuento_div = precios_div.find_element(By.CSS_SELECTOR, 'div[class="mr1 mr2-xl lh-copy b black f5 f4-l"]')
                    producto['precio_actual'] = precio_descuento_div.text if precio_descuento_div.text else 'null'
                except:
                    producto['precio_actual'] = None


                try:            
                    precio_anterior_div = precios_div.find_element(By.CSS_SELECTOR, 'div[class="gray mr1 strike f7 f6-l"]')
                    producto['precio_anterior'] = precio_anterior_div.text if precio_anterior_div.text else 'null'
                except:
                    producto['precio_anterior'] = None

                categoria['productos'].append(producto)
                #data_item_ids_guardados.append(aux_producto)


            categorias.append(categoria)
            contador+=1
        except:
            print('categoria no válida')

    result = {
        'URL': url,
        'categorias': categorias
    }

    

    if contador == 0:
        result = {
            'URL': url,
            'categorias': categorias,
            'resultado': 'Walmart bloqueó al driver el acceso a los productos, el archivo ejecutable está en el repo: https://github.com/elJamesSnz/walmart-webscraping-apps'
        }

        print(driver.page_source)

        with open('pagina.txt', 'w', encoding='utf-8') as file:
            file.write(driver.page_source)

    

    # Convertimos el diccionario a un objeto JSON y lo regresamos
    return result

    