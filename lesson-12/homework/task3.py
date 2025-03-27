# import requests
import json
import time
# from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from pathlib import Path



current_dir = Path(__file__).resolve().parent
json_name=current_dir / 'laptops.json'
url="https://www.demoblaze.com/"

def extract_laptops():
    global url
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Run browser in headless mode
    # chrome_options.add_argument("--disable-popup-blocking")
    # chrome_options.add_argument("--window-position=-1700,-200")
    driver = webdriver.Chrome(options=chrome_options)
    # Browser will remain open after the script ends
    chrome_options.add_experimental_option("detach", True)

    driver.get(url)
    buttons=driver.find_elements(By.TAG_NAME,"a")
    laptop_button=driver.find_element(By.LINK_TEXT,"Laptops")
    # print(type(laptop_button))
    time.sleep(2)
    laptop_button.click()
    next_button=driver.find_element(By.ID,"next2")
    # print('dkkd')
    # print(next_button)
    next_button.click()
    # print("Next button clicked")
    time.sleep(2)
    laptops=driver.find_elements(By.CLASS_NAME,"card-block")
    laptops_list=list()
    for laptop in laptops:
        name=laptop.find_element(By.CLASS_NAME,"card-title").text
        price=laptop.find_element(By.TAG_NAME,"h5").text
        description=laptop.find_element(By.CLASS_NAME,"card-text").text
        laptops_list.append({"name":name,"price":price,"description":description})
#         print(name,price,description)
    
    # print(laptops_list)
    write_to_json(laptops_list)
    # return laptops_list
    time.sleep(2)
    driver.quit()

def write_to_json(laptops_list):

    global json_name
    with open(json_name, 'w') as file:
        # for laptop in laptops_list:
        #     json.dump(laptop, file, indent=4)
        json.dump(laptops_list, file, indent=4)


def main():
    extract_laptops()
    # write_to_json(laptops_list)
    # print(laptops_list)
    print('DONE')
if(__name__=="__main__"):
    main()

