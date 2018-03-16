import os
import numpy as np

import pprint
pp = pprint.PrettyPrinter(width=120)

import qcdb
from qcdb.driver.driver_helpers import get_active_molecule


def {{ cookiecutter.main_function }}(name, **kwargs):
    """ Example Docstring
        input: 
               molecule: Molecule instance
        output: 
               molecule.esp_charges: dictionary of fitted 
                                     esp charges. Modified
                                     in place
        return: None
        output files: mol_results.dat: fitting results
                      mol_grid.dat: grid points in molecule.units
                      mol_grid_esp.dat: QM esp valuese in a.u. 
    """
    molecule = kwargs.pop('molecule', get_active_molecule())
    molecule.update_geometry()

    qopt = qcdb.get_active_options().scroll['{{ cookiecutter.project_slug|upper }}']



    qcdb.get_active_options().require('PSI4', 'E_CONVERGENCE', 6, accession='wert')
    e, jrec = qcdb.energy(name, molecule=molecule, return_wfn=True)
    pprint.pprint(jrec)

    return jrec

