from urllib.parse import urljoin

import scrapy

from ..items import PianosongdownloadItem


class PreStaffSpider(scrapy.Spider):
    name = "pre_staff"

    def start_requests(self):
        urls = [
            "https://pianosongdownload.com/prestaffmusic.html",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def get_pieces(self, response):
        pieces = [
            urljoin(response.url, href)
            for href in response.css(".C-5").xpath("./@href").getall()
        ]

        return pieces

    def parse(self, response):
        pieces = self.get_pieces(response)
        yield from [scrapy.Request(url=url, callback=self.parse) for url in pieces]

        href = response.css(".OBJ-15").xpath("./@href").get()
        if href:
            url = urljoin(response.url, href)
            yield PianosongdownloadItem(
                file_urls=[url],
                name=self.name,
            )

        href = response.css(".OBJ-17").xpath("./@href").get()
        if href:
            url = urljoin(response.url, href)
            yield PianosongdownloadItem(
                file_urls=[url],
                name=self.name,
            )
