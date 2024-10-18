from atf import *
from main.api.wrappers.profile_api_wrapper import ProfileApiWrapper


class Test(TestCase):
    """Тест персональных данных"""

    @classmethod
    def setUpClass(cls):
        cls.client = JsonRpcClient(url=cls.config.get('SITE'), verbose_log=2)
        cls.client.auth(login=cls.config.get("LOGIN"), password=cls.config.get("PASSWORD"))
        cls.profile_api = ProfileApiWrapper(cls.client)

    def test(self):
        """Тест персчональных данных"""

        e_data = {
            "position": "Бухгалтер",
            "birthday": None,
            "date_begin": "2019-01-01",
            "email": 'new@mail.ru',
            "phone_num": '+7 (989) 876-34-57',
            "user_id": "7d68445b-1720-44d5-82f1-258b03934726"
        }
        self.profile_api.get_data('Регламентные События')
        self.profile_api.chech_items(**e_data)
