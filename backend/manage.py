#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

# settings.py를 개발용이랑 배포용이랑 다르게 바꾸었기 때문에 mysite.settings.develop로 경로를 지정해준다.
# 개발용 settings.py는 여기서 경로를 설정한다. 배포용은 wsgi.py에서 설정한다.
def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
