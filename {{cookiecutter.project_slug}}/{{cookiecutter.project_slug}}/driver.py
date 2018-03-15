import os
import numpy as np
import qcdb

def {{ cookiecutter.main_function }}(name, **kwargs):
    """ Main resp function
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
    qopt = qcdb.get_active_options().scroll['{{ cookiecutter.project_slug|upper }}']



    qcdb.get_active_options().require('PSI4', 'GRIDDAT', griddat, accession='wert')
    e, jrec = qcdb.energy(name, molecule=molecule, return_wfn=True)
    pprint.pprint(jrec)

    return jrec

