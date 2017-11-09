# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import Request


class BookSpiderSpider(Spider):
    name = 'book_spider'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        books = response.xpath('//h3/a/@href').extract()
        for book in books:
            book_url =  response.urljoin(book)
            yield Request(book_url,callback = self.parse_book)
        next_page_url =  response.urljoin(response.xpath('//a[text() = "next"]/@href').extract_first())
        yield Request(next_page_url)    

    def parse_book(self,response):
    	rating = response.xpath('//*[contains(@class,"star-rating")]/@class').extract_first()
    	img_url = response.xpath('//img/@src').extract_first()
    	img_url = img_url.replace("../..","http:/books.toscrape.com")
    	title = response.xpath("//div[contains(@class,'product_main')]/h1/text()").extract_first()
    	price = response.xpath("//*[@class = 'price_color']/text()").extract_first()
    	rating = response.xpath("//*[contains(@class,'star-rating')]/@class").extract_first()
    	description = response.xpath("//*[@id = 'product_description']/following-sibling::p/text()").extract_first()
    	yield {
        'rating' : rating,
        'img_url' : img_url,
        'title ': title ,
        'price': price,
        'rating': rating,
        'description': description,
         }
