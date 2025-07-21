from pymatgen.core import structure
from pymatgen.io.vasp.inputs import Poscar
from pymatgen.io.vasp import sets
from pymatgen.io.vasp.sets import MPRelaxSet, MPStaticSet
from pymatgen.io.vasp.inputs import Kpoints
import os


poscar = Poscar.from_file("outputs/POSCAR")
monolayer_MoS2_struct = poscar.structure
vasp_input_set = MPRelaxSet(monolayer_MoS2_struct)

output_dir = os.path.join(os.path.dirname(__file__), "../outputs")
output_dir = os.path.abspath(output_dir)

vasp_input_set.write_input(
    output_dir=output_dir,
    make_dir_if_not_present=True,
    include_cif=False,
    potcar_spec=True,
    zip_output=False,
)
