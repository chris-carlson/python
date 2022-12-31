import locale


class Currency:

    @staticmethod
    def format(num: int, include_decimals: bool = True, include_commas: bool = False) -> str:
        locale.setlocale(locale.LC_ALL, '')
        formatted_currency: str = locale.currency(num, grouping=include_commas)
        if not include_decimals:
            return formatted_currency[:-3]
        return formatted_currency
