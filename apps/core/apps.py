from django.apps import AppConfig
from copy import copy
import django.template.context

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.core'
    verbose_name = 'Configuration & Entreprise'

    def ready(self):
        # Python 3.14 + Django 5.1 compatibility patch for context copying
        def _patched_context_copy(self):
            duplicate = self.__class__.__new__(self.__class__)
            duplicate.__dict__.update(self.__dict__)
            duplicate.dicts = self.dicts[:]
            duplicate.render_context = copy(self.render_context)
            return duplicate

        django.template.context.Context.__copy__ = _patched_context_copy
        django.template.context.RequestContext.__copy__ = _patched_context_copy
        django.template.context.BaseContext.template = None
        django.template.context.Context.template = None
        django.template.context.RequestContext.template = None
