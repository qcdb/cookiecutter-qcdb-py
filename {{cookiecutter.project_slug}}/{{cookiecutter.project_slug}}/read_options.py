from qcdb.moptions.read_options2 import RottenOption

def load_defaults(options):

    options.add('{{ cookiecutter.project_slug|lower }}', RottenOption(
            keyword='kw1',
            default='',
            validator=lambda x: x.upper(),
            glossary='Explanation of kw1.'))

