from atf.api.base_api_ui import BaseApiUI


class Document(BaseApiUI):
    """Документ.УдалитьДокументы"""

    def delete_document(self, id):
        """
        Удаление документа
        :param id:
        """

        self.client.call_rvalue(method='Документ.УдалитьДокументы', ИдО=id)