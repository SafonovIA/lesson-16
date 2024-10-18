from datetime import datetime, timedelta

from atf.api.base_api_ui import BaseApiUI
from atf.api.helpers import *


class WDT(BaseApiUI):
    """WTD.List"""
    def list(self, search):
        """Список планов
        :param search:
        :return:
        """

        params = generate_record_list(
            ФильтрДатаП=(None, 'Строка'),
            ФильтрДатаС=(None, 'Строка'),
            ФильтрПоиска=search,
        )

        return self.client.call_rrecordset(method='WTD.List', **params)


