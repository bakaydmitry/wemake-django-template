from django.contrib import admin

# todo: replace _MODELNAME_
from server.apps.{{cookiecutter.project_main_app_name}}.models import _MODELNAME_


@admin.register(_MODELNAME_)
class _MODELNAME_Admin(admin.ModelAdmin[_MODELNAME_]):
    """Admin panel example for ``_MODELNAME_`` model."""
