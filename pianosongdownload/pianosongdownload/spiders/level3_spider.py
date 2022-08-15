from urllib.parse import urljoin

import scrapy

from .level2_spider import PreStaffSpider


class Level3Spider(PreStaffSpider):
    name = "level3"

    def start_requests(self):
        urls = [
            "https://pianosongdownload.com/level3.html",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def get_pieces(self, response):
        pieces = [
            urljoin(response.url, href)
            for href in response.css(".C-6").xpath("./@href").getall()
        ]

        return pieces
