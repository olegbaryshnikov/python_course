import os

import asyncio
from typing import Any, Dict, List
import requests
import pandas as pd

from bs4 import BeautifulSoup


async def async_scraper(url: str) -> Any:
    headers = {
        "Content-Type": "text",
        "Accept-Language": "ru-RU,ru;q=0.9",
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36",
    }
    response = requests.get(url, headers=headers)
    return response.text


def extract_from_soup(soup_data: Any) -> Any:
    if soup_data is None:
        return None

    test_splits = soup_data.find_all(recursive=False)

    if len(test_splits) > 0:
        return "\n".join(tag.text for tag in test_splits if tag.text)
    return soup_data.get_text()


def parse_single(single_data: Any) -> Dict[str, Any]:
    parsed_data = {}

    parsed_data["imgs"] = [
        img["src"]
        for img in single_data.find("div", {"data-name": "Gallery"}).findAll("img")
    ]
    parsed_data["price"] = extract_from_soup(
        single_data.find("div", {"data-name": "OfferGeneralInfoLayout"}).find("span")
    )
    parsed_data["features"] = extract_from_soup(
        single_data.find("a", {"data-name": "Features"})
    )

    # these fields should be used together
    parsed_data["underground_names"] = [
        extract_from_soup(soup_data)
        for soup_data in single_data.findAll("div", {"data-name": "Underground"})
    ]
    parsed_data["underground_travel_time"] = [
        extract_from_soup(soup_data)
        for soup_data in single_data.findAll("div", {"data-name": "GeoTravelTime"})
    ]

    parsed_data["address"] = extract_from_soup(
        single_data.find("div", {"data-name": "Address"})
    )
    parsed_data["description"] = extract_from_soup(
        single_data.find("div", {"data-name": "OfferDescription"})
    )

    return parsed_data


async def async_parser(data: Any) -> List[Dict[str, Any]]:
    soap = BeautifulSoup(data, "lxml")
    data_containers = soap.findAll("section", {"data-name": "CardContainer"})
    return [parse_single(data) for data in data_containers]


async def extract_page_data(url: str) -> List[Dict[str, Any]]:
    data = await async_scraper(url)
    parsed_data = await async_parser(data)
    return parsed_data


async def main(url_template: str, artifacts_dir: str, pages_num: int):
    pages_data = await asyncio.gather(
        *(extract_page_data(url_template.format(i)) for i in range(1, pages_num + 1))
    )
    concated_pages_data = [d for p_d in pages_data for d in p_d]

    pd.DataFrame(concated_pages_data).to_csv(os.path.join(artifacts_dir, "out.csv"))


if __name__ == "__main__":
    url_template = "https://www.cian.ru/cat.php?deal_type=rent&engine_version=2&offer_type=flat&p={0}&region=1"
    artifacts_dir = os.path.join(os.getcwd(), "hw_5", "artifacts", "5.2")
    asyncio.run(main(url_template, artifacts_dir, 3))
