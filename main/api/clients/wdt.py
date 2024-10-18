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
            flServerRendering=False,
            iterative_list=True,
            new_navigation=True,
            translit_search=False,
            УчитыватьИерархиюНО=True,
            ФильтрДатаП=(str(datetime.today().date() + timedelta(days=30)), 'Дата'),
            ФильтрДатаПериод='Период',
            ФильтрДатаС=(str(datetime.today().date()), 'Дата'),
            ФильтрДокументНашаОрганизация='-2',
            ФильтрМоиДокументы='Все',
            ФильтрПодтипДокумента=(None, 'Строка'),
            ФильтрПоиска='Регламентные События',
            ФильтрСостояние='-1'
        )

        return self.client.call_rrecordset(method='WTD.List', **params)


