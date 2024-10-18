from atf.api.base_api_ui import BaseApiUI
from atf.api.helpers import *


class Person(BaseApiUI):
    """Person.ReadCard"""

    def read_card(self, privat_person):
        """Получение карточки сотрудника"""
        params = {'Ids': generate_record(PrivatePerson=privat_person), 'Params': {}}

        return self.client.call_rrecord(method='Person.ReadCard', **params).result
