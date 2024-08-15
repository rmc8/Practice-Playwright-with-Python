from playwright.sync_api import sync_playwright, expect


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://quotes.toscrape.com/")
        page.get_by_text("Login").click()
        # ログインページ
        page.wait_for_url("https://quotes.toscrape.com/login")
        ## ユーザー名
        user = page.get_by_label("Username")
        user.fill("username")
        ## パスワード
        pwd = page.get_by_label("Password")
        pwd.fill("password")
        ## ボタンを押す
        page.get_by_role("button", name="Login").click()
        # ログインの成功を確認する
        expect(page.get_by_text("Logout")).to_be_visible(timeout=5000)
        # 5秒待機する
        page.wait_for_timeout(5000.0)
        print("Success!")
        browser.close()


if __name__ == "__main__":
    main()
