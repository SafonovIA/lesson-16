from atf.api.base_api_ui import BaseApiUI
from atf.api.helpers import *


class PlanWorks(BaseApiUI):
    """ПланРабот.СписокПланов"""
    def list_plans(self, search):
        """Список планов
        :param search:
        :return:
        """

        params = generate_record_list(search=search)

        return self.client.call_rrecordset(method='ПланРабот.СписокПланов', **params)

