__version__ = '{{ cookiecutter.current_tag }}'
__version_long = '{{ cookiecutter.current_tag }}+{{ cookiecutter.current_tag_githash7 }}'
__version_upcoming_annotated_v_tag = '{{ cookiecutter.upcoming_tag }}'

def version_formatter(dummy):
    return '(inplace)'
