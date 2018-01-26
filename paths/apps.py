# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class PathsConfig(AppConfig):
    name = 'paths'

    def ready(self):
        import paths.signals