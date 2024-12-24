import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def load_actions(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def find_element(driver, selector):
    try:
        return WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, selector))
        )
    except:
        print(f"Elemento não encontrado: {selector}")
        return None

def perform_action(driver, action):
    if action['type'] == 'click':
        element = find_element(driver, action['selector'])
        if element:
            element.click()
    elif action['type'] == 'input':
        element = find_element(driver, action['selector'])
        if element:
            element.send_keys(action['value'])
