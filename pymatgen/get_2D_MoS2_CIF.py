from mp_api.client import MPRester

# For direct slab generation, it's more common to use SlabGenerator
from pymatgen.core.surface import SlabGenerator  # [2]

import os
from dotenv import load_dotenv

load_dotenv()

with MPRester() as m:
    # 1. Retrieve the bulk MoS2 structure
    MoS2_bulk_structure = m.get_structure_by_material_id("mp-2815", True, True)
    # print(MoS2_bulk_structure)
    # print(f"Successfully retrieved bulk MoS2 structure (MP ID: mp-1027525).")

    # 2. Define parameters for slab generation
    miller_index = (0, 0, 1)

    # min_slab_size: Thickness of a single MoS2 layer is 0.65 nm (6.5 Å) [11]
    min_slab_thickness_angstroms = 6.5  # Å [11]

    # min_vacuum_size: A vacuum of at least 20 Å is widely accepted to minimize spurious interactions [2, 12]
    min_vacuum_thickness_angstroms = 20.0  # Å [2, 12]

    # 3. Generate the 2D slab using SlabGenerator
    # It takes the initial bulk structure, Miller index, minimum slab size, and minimum vacuum size [2]
    slab_generator = SlabGenerator(
        initial_structure=MoS2_bulk_structure,
        miller_index=miller_index,
        min_slab_size=min_slab_thickness_angstroms,
        min_vacuum_size=min_vacuum_thickness_angstroms,
        center_slab=True,  # Centers the slab in the non-periodic direction [2]
    )

    # The get_slabs() method returns a list of symmetrically distinct slabs [2]
    # For MoS2 (001), there is typically one non-polar termination relevant for a simple monolayer.
    MoS2_2D_slabs = slab_generator.get_slabs()

    # Assuming the first slab in the list is your desired monolayer [2]
    MoS2_monolayer_structure = MoS2_2D_slabs[2]
    # print(MoS2_2D_slabs)
    MoS2_monolayer_structure.to(filename="MoS2_monolayer.cif")
    MoS2_bulk_structure.to(filename="MoS2_bulk.cif")
    # You can now save this structure to a file (e.g., POSCAR, CIF) for DFT calculations:
    # MoS2_monolayer_structure.to(filename="MoS2_monolayer.poscar") [13]
