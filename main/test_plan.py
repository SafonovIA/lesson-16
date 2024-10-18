from atf import JsonRpcClient
from atf.ui import *
from main.pages.Libraries.AuthControls.authForm import MainWithSteps
from main.pages.plans import Plans
from random import randint
from api.wrappers.plan_api_wrapper import PlanApiWrapper


class Test(TestCaseUI):
    plan_data = {
        'Сотрудник': 'Регламентные События',
        'Объекты планирования': 'Регламентные События',
        'Комментарий': f'Коментарий {randint(10000, 100000)}',
    }

    @classmethod
    def setUpClass(cls):
        cls.client = JsonRpcClient(url=cls.config.get('SITE'), verbose_log=2)
        cls.client.auth(login=cls.config.get("LOGIN"), password=cls.config.get("PASSWORD"))
        cls.plan_api = PlanApiWrapper(cls.client)
        cls.browser.open(cls.config.get('SITE'))
        MainWithSteps(cls.driver).auth(cls.config.get('LOGIN'), cls.config.get('PASSWORD'))
        cls.plan_api.delete_document(cls.plan_data['Сотрудник'], cls.plan_data['Комментарий'])

    def setUp(self):
        self.browser.open('https://fix-online.sbis.ru/page/plans')
        self.plans_page = Plans(self.driver)
        self.plans_card = self.plans_page.create_doc('План работ')

    def tearDown(self):
        self.plan_api.delete_document(self.plan_data['Сотрудник'], self.plan_data['Комментарий'].split()[0])

    def test_01(self):
        """Создание плана работ"""

        self.plans_card.fill_document(**self.plan_data)
        self.plans_card.run_task()
        self.plans_page.exist_plan(self.plan_data['Комментарий'])
        self.plans_page.open_plan(self.plan_data['Комментарий'])
        self.plans_card.check_plan(**self.plan_data)
        self.plans_page.delete_plan(self.plan_data['Комментарий'])
        self.plans_page.exist_plan(self.plan_data['Комментарий'], exist=False)

