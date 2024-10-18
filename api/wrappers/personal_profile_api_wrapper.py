from atf.api.base_api_ui import BaseApiUI
from api.clients.person_profile import PersonalInfo


class ProfileApiWrapper(BaseApiUI):
    """PersonProfile.PersonalInfo"""

    def __init__(self, client):
        super().__init__(client)
        self.person_api = PersonalInfo(client)

    @property
    def get_items(self):
        """Получение персональных данных"""

        return self.person_api.personal_info().result

    def chech_items(self, **kwargs):
        """Проверка персональных данных"""

        if "position" in kwargs.keys():
            assert self.get_items['Workplaces'][0]['Post'] == kwargs['position']

        if "birthday" in kwargs.keys():
            assert self.get_items['PrivatePersonData']['BirthDate'] == kwargs['birthday']

        if "date_begin" in kwargs.keys():
            assert self.get_items['WorkExperiences']["Verified"][0]["DateBegin"] == kwargs['date_begin']

        if "phone_num" in kwargs.keys():
            for contact in self.get_items['Contacts']:
                if "mobile_phone" in contact.values():
                    assert contact['Value'] == kwargs['phone_num']

        if "email" in kwargs.keys():
            for contact in self.get_items['Contacts']:
                if "email" in contact.values():
                    assert contact['Value'] == kwargs['email']

        if "user_id" in kwargs.keys():
            assert self.get_items['Person'] == kwargs['user_id']


