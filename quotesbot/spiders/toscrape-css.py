# -*- coding: utf-8 -*-
import scrapy


class ToScrapeCSSSpider(scrapy.Spider):
    name = "toscrape-css"
    start_urls = [
        'http://quotes.toscrape.com/',
    ]

    # def parse(self, response):
    #     for quote in response.css("div.quote"):
    #         yield {
    #             'text': quote.css("span.text::text").extract_first(),
    #             'author': quote.css("small.author::text").extract_first(),
    #             'tags': quote.css("div.tags > a.tag::text").extract()
    #         }

    #     next_page_url = response.css("li.next > a::attr(href)").extract_first()
    #     if next_page_url is not None:
    #         yield scrapy.Request(response.urljoin(next_page_url))

    
    # def parse_top_10_tags(self, response):
    #     for tag in response.css("span.tag-item"):
    #         yield {
    #             'tags': tag.css("a.tag::text").extract_first()
    #         }

    def parse(self, response):
        for tag in response.css("span.tag-item"):
            yield {
                'tags': tag.css("a.tag::text").extract_first()
            }
