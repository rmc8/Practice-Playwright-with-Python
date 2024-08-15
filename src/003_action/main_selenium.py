import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():
    driver = webdriver.Chrome()
    try:
        driver.get("https://quotes.toscrape.com/")
        driver.find_element(By.LINK_TEXT, "Login").click()
        # ログインページに遷移したことを確認
        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://quotes.toscrape.com/login")
        )
        # ユーザー名を入力
        username_field = driver.find_element(By.ID, "username")
        username_field.send_keys("username")
        # パスワードを入力
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("password")
        # ログインボタンをクリック
        driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        # ログイン成功を確認（Logoutリンクが表示されるまで待機）
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Logout"))
        )
        # 5秒待機
        time.sleep(5)
        print("Success!")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
