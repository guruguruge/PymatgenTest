from ase.build import mx2
from ase.visualize import view
from ase.io import write

# formula = "MoS2"
# state = "2H"
# a = 3.18
# thickness = 3.19
# size = (1, 1, 1)

# construct 2D-MoS2 supercell ( 3 x 3 )
MoS2_struct = mx2(
    formula="MoS2", kind="2H", a=3.18, thickness=3.19, size=(1, 1, 1), vacuum=20.0
)

# visualize
# view(MoS2_struct)

# make VASP file of struct
# write("POSCAR", MoS2_struct, format="vasp")
# make CIF file of sturct
write("MoS2.cif", MoS2_struct, format="cif")

# view(MoS2_struct)