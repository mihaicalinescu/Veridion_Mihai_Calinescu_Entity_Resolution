import scrapy

class QoutesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
            }

            # cautam urmatoarea pagina si continuam scrapping-ul
            next_page = response.css('li.next a ::attr(href)').get()
            if next_page is not None:
                yield response.follow(next_page, se)