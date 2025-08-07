import os
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv

load_dotenv()

URL_TO_SCRAPE = os.getenv("URL") 
RAW_DATA_FILE = os.getenv("RAW_DATA_FILE")

def scrape_qa_data(url: str) -> list[dict]:
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--log-level=3')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    all_qa_pairs = []
    
    try:
        driver.get(url)
        wait = WebDriverWait(driver, 30)
        
        thread_links = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a[class='undefined']")))
        thread_urls = [link.get_attribute('href') for link in thread_links if link.get_attribute('href')]

        for i, thread_url in enumerate(thread_urls, 1):
            try:
                driver.get(thread_url)
                wait = WebDriverWait(driver, 20)
                
                question_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[class='font-bold text-lg']")))
                question = question_element.text

                answer_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "p[class='mt-4']")))
                answer = answer_element.text

                all_qa_pairs.append({'question': question, 'answer': answer})
                print(f"({i}/{len(thread_urls)})")

            except Exception as e:
                print(f"เกิดข้อผิดพลาดในการ Scrape ข้อมูลจาก {thread_url}: {e}")
                continue
        return all_qa_pairs
    finally:
        driver.quit()

def save_to_csv(qa_pairs: list[dict], filename: str):
    if not qa_pairs:
        print("ไม่มีข้อมูลให้บันทึก")
        return
    print(f"กำลังบันทึกข้อมูล {len(qa_pairs)} รายการลงไฟล์ {filename}")
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['question', 'answer'])
            writer.writeheader()
            writer.writerows(qa_pairs)
        print(f"บันทึกข้อมูลสำเร็จ")
    except Exception as e:
        print(f"เกิดข้อผิดพลาดในการบันทึกไฟล์: {e}")

if __name__ == "__main__":
    qa_data = scrape_qa_data(URL_TO_SCRAPE)
    save_to_csv(qa_data, RAW_DATA_FILE)