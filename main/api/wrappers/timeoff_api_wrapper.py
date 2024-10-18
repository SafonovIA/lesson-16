from atf.api.base_api_ui import BaseApiUI
from api.clients.wdt import WDT
from api.clients.documents.delete_doc import Document


class TimeoffApiWrapper(BaseApiUI):
    """wrapper WTD.List"""

    def __init__(self, client):
        super().__init__(client)
        self.timeoff_api = WDT(client)
        self.delete_doc = Document(client)

    def delete_timeoff(self, person, couse):
        """
        Удаление документа
        :param couse: причина отгула
        :param person: Поиск по имени
        """

        assert couse, 'Параметр couse не может быть пустым'
        response = self.timeoff_api.list(person).result
        for i in response:
            if couse in i['NoteText']:
                self.delete_doc.delete_doc(i['DocID'])