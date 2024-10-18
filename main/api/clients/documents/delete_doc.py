from api.clients.wdt import WDT
from atf.api.base_api_ui import BaseApiUI


class DeleteDoc(BaseApiUI):
    """Документ.УдалитьДокументы"""

    def delete_doc(self, idd):
        """
        Удаление документа
        :param idd:
        """

        self.client.call_rvalue(method='Документ.УдалитьДокументы', ИдО=idd)