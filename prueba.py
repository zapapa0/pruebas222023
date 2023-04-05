import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Definir lista de URLs de las páginas web a hacer scraping
urls = ['https://www.betsson.com',
        'https://sports.bwin.com',
        'https://www.codere.com',
        'https://sports.yajuego.co/',
        'https://www.pinnacle.com/es',
        'https://www.betway.com/',
        'https://www.unibet.com/',
        'https://www.williamhill.co/']

# Definir lista de categorías de eventos deportivos
categories = ['Football', 'Basketball', 'Baseball', 'Tennis', 'Hockey']

# Configurar el driver de Selenium
options = Options()
options.add_argument("--disable-extensions")
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--incognito")
options.add_argument("--disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--disable-popup-blocking")
options.add_argument("--disable-default-apps")
options.add_argument("--disable-plugins-discovery")
options.add_argument("--start-maximized")
options.add_argument("--remote-debugging-port=9222")
driver = webdriver.Chrome(options=options)

# Función para hacer scraping de una página web
def scrape_page(url, category):
    events = []
    try:
        # Cargar la página
        driver.get(url)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        time.sleep(5)

        # Cerrar cualquier ventana emergente o anuncio que aparezca
        try:
            popup = driver.find_element(By.CSS_SELECTOR, 'div.modal__close')
            popup.click()
        except:
            pass

        # Buscar los elementos de eventos deportivos
        event_elems = driver.find_elements(By.CLASS_NAME, 'EventGrid__item')
        for event_elem in event_elems:
            event = {}
            event['category'] = category
            event['name'] = event_elem.find_element(By.CLASS_NAME, 'EventGrid__eventName').text
            event['league'] = event_elem.find_element(By.CLASS_NAME, 'EventGrid__eventName--sub').text
            event['odds'] = []
            odds_elems = event_elem.find_elements(By.CLASS_NAME, 'OddsButton__odds')
            for odds_elem in odds_elems:
                event['odds'].append(odds_elem.text)
            event['url'] = event_elem.find_element(By.CLASS_NAME, 'EventGrid__eventName').get_attribute('href')
            events.append(event)
    except Exception as e:
        print(f'Error al hacer scraping de la página {url}: {e}')
    return events

# Función para guardar la información en un archivo JSON
def save_json(data, file):
    with open(file, 'w') as json_file:
        json.dump(data, json_file, indent=4)

# Loop principal para hacer scraping en todas las páginas y categorías
while True:
    for url in urls:
        for category in categories:
            events = scrape_page(url, category)
            file = f'{category.lower()}_{url.split("//")[1].replace("/", "_")}.json'
            save_json(events, file)
            print(f'Inform
                        event['url'] = event_elem.find_element(By.CLASS_NAME, 'event-card__link').get_attribute('href')
                        events.append(event)
            except Exception as e:
                print(f'Error al hacer scraping de la página {url}: {e}')
        return events

    # Función para guardar la información en un archivo JSON
    def save_json(data, file):
        with open(file, 'w') as json_file:
            json.dump(data, json_file, indent=4)

    # Configurar el driver de Selenium
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-blink-features=AutomationControlledForTesting")
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--disable-extensions')
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    while True:
        driver = webdriver.Chrome(options=options, executable_path="C:/ruta/al/chromedriver.exe")
        driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"})
        try:
            driver.get(url)
            driver.implicitly_wait(30)
            time.sleep(5)

            event_elems = driver.find_elements(By.CLASS_NAME, 'event-card')
            for event_elem in event_elems:
                event = {}
                event['category'] = category
                event['name'] = event_elem.find_element(By.CLASS_NAME, 'event-card__name').text
                event['league'] = event_elem.find_element(By.CLASS_NAME, 'event-card__league').text
                event['odds'] = []
                odds_elems = event_elem.find_elements(By.CLASS_NAME, 'odd-value')
                for odds_elem in odds_elems:
                    event['odds'].append(odds_elem.text)
                event['url'] = event_elem.find_element(By.CLASS_NAME, 'event-card__link').get_attribute('href')
                events.append(event)
        except Exception as e:
            print(f'Error al hacer scraping de la página {url}: {e}')
        finally:
            driver.quit()
            save_json(events, file)
            print(f'Información ha sido guardada en el archivo {file}')

        time.sleep(5)
