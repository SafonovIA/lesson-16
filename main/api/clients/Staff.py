from atf.api.base_api_ui import BaseApiUI
from atf.api.helpers import *


class Staff(BaseApiUI):
    """Staff.WasabyList"""

    def wasaby_list(self, name):
        """Поиск по имени"""
        params = generate_record_list(Access=(None, 'Строка'),
                                      CalcFields=(['Contact'], {'n': 'Массив', 't': 'Строка'}),
                                      SearchString=name,
                                      )

        return self.client.call_rrecordset(method='Staff.WasabyList', **params).result

