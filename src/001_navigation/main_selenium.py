import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():
    # Chromeドライバーを初期化
    driver = webdriver.Chrome()
    try:
        # example.comにアクセスする
        driver.get("https://example.com")
        # テキストをクリックする
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "More information..."))
        ).click()
        # ページ遷移を待機する
        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://www.iana.org/help/example-domains")
        )
        # ページの情報を表示する
        print(driver.title)
        print(driver.current_url)
        # アサーション(ページタイトルが指定のテキストと一致するか確認する)
        assert driver.title == "Example Domains", "タイトルが一致しません"
        # 1秒待機する
        time.sleep(1)
    finally:
        # ブラウザを閉じる
        driver.quit()


if __name__ == "__main__":
    main()
