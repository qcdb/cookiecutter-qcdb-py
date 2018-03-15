
# -*- coding: utf-8 -*-

"""Top-level package for {{ cookiecutter.project_name }}."""

__author__ = """{{ cookiecutter.full_name }}"""
__email__ = '{{ cookiecutter.email }}'


from .metadata import __version__, version_formatter
from .driver import {{ cookiecutter.main_function }}

