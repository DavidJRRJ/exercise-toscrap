from parsel import Selector
import requests


def scrape(url: str) -> str:
    URL_BASE = "http://books.toscrape.com/catalogue/"

    response = requests.get(url)
    selector = Selector(text=response.text)

    title = selector.css("h1::text").get()
    price = selector.css("p.price_color::text").re_first(r"\d+\.\d{2}")
    description = selector.css("article.product_page > p::text").get()
    cover = URL_BASE + selector.css("img::attr(src)").get()

    # Retira o ...more no final da descrição
    suffix = "...more"
    if description.endswith(suffix):
        description = description[:-len(suffix)]

    # retorna o resultado do crawling
    result = [title, price, description, cover]
    format_result = ",".join(result)
    return format_result
