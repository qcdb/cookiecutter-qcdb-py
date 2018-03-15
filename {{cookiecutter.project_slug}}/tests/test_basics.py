import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from utils import *
from addons import *


sys1_pk_rhf =  -76.0266537
sys2_pk_uhf =  -38.925334624580
sys2_pk_rohf = -38.919988755499

@using_psi4
def test_qcdb_energy():

    h2o = qcdb.set_molecule("""
  O 
  H 1 0.96
  H 1 0.96 2 104.5
""")

    qcdb.set_options({'basis': 'cc-pVDZ',
                      'scf_type': 'pk',
                      'memory': '600 mb'})

    qcdb.energy('p4-hf')

    assert compare_values(sys1_pk_rhf, qcdb.get_variable('HF TOTAL ENERGY'), 6, sys._getframe().f_code.co_name)


@using_cfour
def test_qcdb_energy_yaml():

    yamlin = """
molecule: |
  O 
  H 1 0.96
  H 1 0.96 2 104.5

driver: !!python/name:qcdb.energy
method: c4-hf
options:
  memory: 1gb
  basis: 'cc-pvdz'
  reference: rhf
  scf_type: pk
"""

    jrec = qcdb.yaml_run(yamlin)
    #import yaml
    #asdf = yaml.load(yamlin)

    #ene = asdf['driver'](asdf['method'],
    #                     options=asdf['options'],
    #                     molecule=qcdb.Molecule(asdf['molecule']))

    #assert compare_values(-38.9199888, ene, 6, 'calc from yaml str')  # ROHF
    assert compare_values(sys1_pk_rhf, float(jrec['qcvars']['HF TOTAL ENERGY'].data), 6, sys._getframe().f_code.co_name)


def test_{{ cookiecutter.project_slug }}():
    qcdb.set_options({'{{ cookiecutter.project_slug }}_kw1': 'cat'})

    import {{ cookiecutter.project_slug }}
    jrec = {{ cookiecutter.project_slug }}.{{ cookiecutter.main_function }}('hf/cc-pvdz', molecule=mol)

    
    
