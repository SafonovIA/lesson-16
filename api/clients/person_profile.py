from atf.api.base_api_ui import BaseApiUI
from atf.api.helpers import *


class PersonalInfo(BaseApiUI):
    """PersonProfile.PersonalInfo"""

    def personal_info(self):
        """Получение данных сотрудника"""

        params = {'Person': '7d68445b-1720-44d5-82f1-258b03934726'}
        return self.client.call_rrecord(method='PersonProfile.PersonalInfo', **params)
