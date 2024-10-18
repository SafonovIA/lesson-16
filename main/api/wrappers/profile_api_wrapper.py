from atf.api.base_api_ui import BaseApiUI
from main.api.clients.Staff import Staff
from main.api.clients.Person import Person


class ProfileApiWrapper(BaseApiUI):
    """Проверка персональных данных"""

    def get_data(self, name):
        """
        Получение данных сотрудника
        :param name: Имя сотрудника
        """
        self.staff = Staff(self.client)
        self.person = Person(self.client)

        self.public_data = self.staff.wasaby_list(name)
        person_id = self.public_data[1]['Employee']['PrivatePerson']
        self.personal_data = self.person.read_card(person_id)



    def chech_items(self, **kwargs):
        """Проверка персональных данных
        :param kwargs: эталонные параметры
        """

        if "position" in kwargs.keys():
            assert self.personal_data['Header']['WorkData']['Position'] == kwargs['position']

        if "birthday" in kwargs.keys():
            assert self.personal_data['Header']['PrivatePersonData']['BirthDate'] == kwargs['birthday']

        if "date_begin" in kwargs.keys():
            assert self.personal_data['Header']['WorkData']['ManagementWorkData']['HireDate'] == kwargs['date_begin']

        if "user_id" in kwargs.keys():
            assert self.personal_data['Ids']['Person'] == kwargs['user_id']

        if "phone_num" in kwargs.keys():
            assert self.public_data[1]['Employee']['Contacts']['MobilePhone'][0]['Value'] == kwargs['phone_num']

        if "email" in kwargs.keys():
            assert self.public_data[1]['Employee']['Contacts']['Email'][0]['Value'] == kwargs['email']


