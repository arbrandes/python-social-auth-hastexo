from social.backends.oauth import BaseOAuth2
import re

class HastexoOAuth2(BaseOAuth2):
    """Hastexo OAuth2 authentication backend"""

    name = 'hastexo'
    BASE_URL = 'http://hastexo-store.lxc:8000'
    ACCESS_TOKEN_METHOD = 'POST'
    SCOPE_SEPARATOR = ' '

    def __init__(self, *args, **kwargs):
        """
        Construct URLs dynamically.
        """
        self.AUTHORIZATION_URL = '{0}/o/authorize/'.format(self.BASE_URL)
        self.ACCESS_TOKEN_URL = '{0}/o/token/'.format(self.BASE_URL)
        super(HastexoOAuth2, self).__init__(*args, **kwargs)

    def get_user_details(self, response):
        """Return user details from hastexo account"""

        # Check if username is an email, and if so, remove the domain.  Also,
        # if we didn't get an email and the username looks like one, set the
        # email explicitly.
        username = response.get('username', '')
        email = response.get('email', '')
        if username:
            matches = re.match(r'([^@]+)@[^@]+\.[^@]+', username)
            if matches:
                email = email or username
                username = matches.group(1)

        # Parse names
        fullname, first_name, last_name = self.get_user_names(
            first_name = response.get('first_name'),
            last_name = response.get('last_name'),
        )

        return {
            'username': username,
            'email': email,
            'fullname': fullname,
            'first_name': first_name,
            'last_name': last_name
        }

    def user_data(self, access_token, *args, **kwargs):
        """Loads user data from service"""
        return self.get_json('{0}/api/login/'.format(self.BASE_URL),
            headers={'Authorization': 'Bearer {0}'.format(access_token)}
        )
