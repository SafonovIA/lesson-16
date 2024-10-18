from atf.api.base_api_ui import BaseApiUI
from api.clients.wdt import WDT
from api.clients.documents.delete_doc import DeleteDoc


class TimeoffApiWrapper(BaseApiUI):
    """wrapper WTD.List"""

    def __init__(self, client):
        super().__init__(client)
        self.timeoff_api = WDT(client)
        self.delete_doc = DeleteDoc(client)

    def delete_document(self, person, filter_del):
        """
        Удаление документа
        :param filter_del: фильтр для удаления
        :param person: Поиск по имени
        """

        assert filter_del, 'Параметр timeoff_mask не может быть пустым'
        response = self.timeoff_api.list(person).result
        for i in response:
            if filter_del in i['NoteText']:
                self.delete_doc.delete_doc(i['DocID'])