from atf.api.base_api_ui import BaseApiUI
from api.clients.work_plan_list import WorkPlanList
from api.clients.documents.delete_doc import DeleteDoc


class PlanApiWrapper(BaseApiUI):
    """ПланРабот.СписокПланов"""

    def __init__(self, client):
        super().__init__(client)
        self.plan_api = WorkPlanList(client)
        self.delete_doc = DeleteDoc(client)

    def delete_document(self, person, couse):
        """Удаление документа
        :param person: Сотрудник
        :param couse: Причина
        """

        assert couse, 'Параметр couse не может быть пустым'
        response = self.plan_api.list(person).result
        for i in response:
            if couse in i['Пункты']:
                self.delete_doc.delete_doc(i['@Документ'])