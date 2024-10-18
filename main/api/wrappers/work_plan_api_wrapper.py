from atf.api.base_api_ui import BaseApiUI
from api.clients.work_plan_list import WorkPlanList
from api.clients.documents.delete_doc import DeleteDoc


class PlanApiWrapper(BaseApiUI):
    """ПланРабот.СписокПланов"""

    def __init__(self, client):
        super().__init__(client)
        self.plan_api = WorkPlanList(client)
        self.delete_doc = DeleteDoc(client)

    def delete_document(self, plan_mask, search):
        """Удаление документа
        :param plan_mask: фильтр
        :param search: фильтр поиска
        """

        assert plan_mask, 'Параметр plan_mask не может быть пустым'
        response = self.plan_api.list(search).result
        for i in response:
            if plan_mask in i['Пункты']:
                self.delete_doc.delete_doc(i['@Документ'])