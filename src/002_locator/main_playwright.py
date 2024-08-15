import re

from playwright.sync_api import sync_playwright


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://quotes.toscrape.com/")
        # quoteクラスの要素をすべて取得し、リストに変換
        quote_elements = page.locator(".quote").all()
        for i, quote_element in enumerate(quote_elements, 1):
            # 名言を抽出する
            text_element = quote_element.locator(".text")
            text = text_element.inner_text().strip('"')
            # 発言者を抽出する
            author_regex = re.compile(r"(?<=by\s)(.+)(?=\s+\(about\))")
            author_raw = quote_element.get_by_text(author_regex).inner_text()
            author = author_regex.search(author_raw).group(1)
            # タグを取得する
            tag_elms = quote_element.get_by_role("link").all()
            tags = ", ".join(
                [tag for elm in tag_elms if (tag := elm.inner_text()) != "(about)"]
            )
            record = {
                "id": i,
                "text": text,
                "author": author,
                "tags": tags,
            }
            print(record)
        browser.close()


if __name__ == "__main__":
    main()
