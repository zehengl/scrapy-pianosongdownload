from urllib.parse import urljoin

import scrapy

from .pre_staff_spider import PreStaffSpider


class Level1Spider(PreStaffSpider):
    name = "level1"

    def start_requests(self):
        urls = [
            "https://pianosongdownload.com/freemusiclevels.html",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def get_pieces(self, response):
        pieces = [
            urljoin(response.url, href)
            for href in response.css(".C-4").xpath("./@href").getall()
        ]

        return pieces
