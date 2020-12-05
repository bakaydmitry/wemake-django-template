from django.contrib import admin

from server.apps.{{cookiecutter.project_main_app_name}}.models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin[BlogPost]):
    """Admin panel example for ``BlogPost`` model."""
