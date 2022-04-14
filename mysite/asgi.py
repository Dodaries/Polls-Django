# 현재 프로젝트를 서비스하기 위한 ASGI-호환 웹 서버의 진입점입니다. 자세한 내용은 ASGI를 사용하여 배포하는 방법 를 참조하십시오.
"""
ASGI config for mysite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_asgi_application()
