import os

from django.conf import settings


def configure(nose_args=None):
        # Helper function to extract absolute path
    location = lambda x: os.path.join(
        os.path.dirname(os.path.realpath(__file__)), x)

    settings.configure(
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',
            }
        },
        TEMPLATE_DIRS=(
            location('templates'),
        ),
        NOSE_ARGS=nose_args,
    )
