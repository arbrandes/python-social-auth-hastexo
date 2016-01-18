from social.backends.oauth import BaseOAuth2


class HastexoOAuth2(BaseOAuth2):
    """Hastexo OAuth2 authentication backend"""

    name = 'hastexo'
    AUTHORIZATION_URL = 'https://store.hastexo.com/o/authorize/'
    ACCESS_TOKEN_URL = 'https://store.hastexo.com/o/token/'
    ACCESS_TOKEN_METHOD = 'POST'
    SCOPE_SEPARATOR = ' '

    def get_user_details(self, response):
        """Return user details from hastexo account"""

        fullname, first_name, last_name = self.get_user_names(
            first_name = response.get('first_name'),
            last_name = response.get('last_name'),
        )

        return {
            'username': response.get('username'),
            'email': response.get('email', ''),
            'fullname': fullname,
            'first_name': first_name,
            'last_name': last_name
        }

    def user_data(self, access_token, *args, **kwargs):
        """Loads user data from service"""
        return self.get_json('https://store.hastexo.com/api/login/',
            headers={'Authorization': 'Bearer {0}'.format(access_token)}
        )
