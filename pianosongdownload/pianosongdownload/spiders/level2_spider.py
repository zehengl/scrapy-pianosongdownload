from urllib.parse import urljoin

import scrapy

from .pre_staff_spider import PreStaffSpider


class Level2Spider(PreStaffSpider):
    name = "level2"

    def start_requests(self):
        urls = [
            "https://pianosongdownload.com/level2.html",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def get_pieces(self, response):
        pieces = [
            urljoin(response.url, href)
            for href in response.css(".C-3").xpath("./@href").getall()
        ]

        return pieces
