from playwright.sync_api import sync_playwright


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://playwright.dev")
        print(page.title())
        print(page.url)
        page.wait_for_timeout(1000.0)
        browser.close()


if __name__ == "__main__":
    main()
