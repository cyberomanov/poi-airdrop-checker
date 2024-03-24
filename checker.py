import requests
from loguru import logger

from datatypes.response import PoiResponse
from tools.add_logger import add_logger
from tools.other import read_file


def get_claimable_balance(session: requests.Session, address: str):
    url = f"https://orcmarket.xyz/api/orc-20/address/{address}/1?data_type=claim"
    try:
        response = session.get(url=url)
        return PoiResponse.parse_obj(response.json()).data.claimable_balance
    except Exception as e:
        logger.exception(e)
        return 0


if __name__ == '__main__':
    add_logger()
    try:
        addresses = read_file(path='data/address.txt')

        poi_total = 0
        with requests.session() as session:
            for address in addresses:
                claimable_balance = get_claimable_balance(session=session, address=address)
                if claimable_balance:
                    poi_total += claimable_balance
                    logger.success(f"{address}: {claimable_balance} $POI.")
                else:
                    logger.info(f"{address}: 0 $POI.")

        logger.info(f"total: {poi_total} $POI.")
    except Exception as e:
        logger.exception(e)
