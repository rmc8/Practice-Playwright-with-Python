import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():
    driver = webdriver.Chrome()
    try:
        driver.get("https://quotes.toscrape.com/")
        # quoteクラスの要素をすべて取得
        quote_elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "quote"))
        )
        for i, quote_element in enumerate(quote_elements, 1):
            # 名言を抽出する
            text_element = quote_element.find_element(By.CLASS_NAME, "text")
            text = text_element.text.strip('"')
            # 発言者を抽出する
            author_raw = quote_element.find_element(
                By.XPATH, ".//*[contains(text(), 'by')]"
            ).text
            author_regex = re.compile(r"(?<=by\s)(.+)(?=\s+\(about\))")
            author = author_regex.search(author_raw).group(1)
            # タグを取得する
            tag_elms = quote_element.find_elements(By.CLASS_NAME, "tag")
            tags = ", ".join([tag.text for tag in tag_elms])
            record = {
                "id": i,
                "text": text,
                "author": author,
                "tags": tags,
            }
            print(record)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
