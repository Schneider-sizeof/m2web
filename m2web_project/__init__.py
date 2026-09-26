"""
M2web Maroc Project Initialization
Includes compatibility patches for Python 3.14+ and Django 5.1+
"""
from copy import copy
import django.template.context

# Python 3.14 + Django 5.1 compatibility patch:
# In Python 3.14, copy(context) via __new__ doesn't inherit instance attributes set in __init__,
# which causes AttributeError on context.template, context._processors, etc. in admin inclusion tags.
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
