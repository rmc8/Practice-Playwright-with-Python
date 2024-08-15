from playwright.sync_api import sync_playwright, expect


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        # example.comにアクセスする
        page.goto("https://example.com")
        # テキストをクリックする
        page.get_by_text("More information...").click()
        # ページ遷移を待機する
        page.wait_for_url("https://www.iana.org/help/example-domains")
        # ページの情報を表示する
        print(page.title())
        print(page.url)
        # アサーション(ページタイトルが指定のテキストと一致するか確認する)
        expect(page).to_have_title("Example Domains")
        # 1秒待機する
        page.wait_for_timeout(1000.0)
        # ブラウザを閉じる
        browser.close()


if __name__ == "__main__":
    main()
