<div align="center">
    <img src="https://pianosongdownload.com/wpimages/wp2752df2f_06.png" alt="logo" height="64">
</div>

# scrapy-pianosongdownload

![coding_style](https://img.shields.io/badge/code%20style-black-000000.svg)

A scrapy app to crawl sheet music from [pianosongdownload.com][1]

## Getting Started

    python -m venv .venv
    .\.venv\Scripts\activate
    python -m pip install -U pip
    pip install -r requirements.txt
    cd pianosongdownload
    scrapy crawl pre_staff
    scrapy crawl level1
    scrapy crawl level2
    scrapy crawl level3
    scrapy crawl intermediate

> Use `pip install -r requirements-dev.txt` for development.

## Credits

- [pianosongdownload.com][1]

[1]: https://pianosongdownload.com
