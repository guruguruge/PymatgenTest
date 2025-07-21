from ase.io import read
from ase.calculators.espresso import Espresso, EspressoProfile
import os


cif_file_path = "outputs/MoS2.cif"
pseudo_dir = "/home/gu/projects/PymatgenTest/outputs/"

output_base_dir = "qe_scf_ase"
calculation_name = "relax"
output_full_dir = os.path.join(output_base_dir, calculation_name)
os.makedirs(output_full_dir, exist_ok=True)

atoms = read(cif_file_path)
pseudos = {"Mo": "Mo.upf", "S": "S.upf"}
profile = EspressoProfile(
    command="/home/gu/Downloads/qe-7.4.1/bin/pw.x ", pseudo_dir=pseudo_dir
)

# "calculation": "vc-relax",  # Type of calculation: 'vc-relax' for variable-cell relaxation [5]
# "restart_mode": "from_scratch",  # Start a new calculation [5]

input_data = {
    "control": {
        "calculation" : 'bands',      
        "restart_mode" : 'restart', 
        "prefix": "MoS2_single",  # Prefix for output files [5]
        "outdir": "/tmp",  # Directory for output files [5]
        "pseudo_dir": pseudo_dir,  # Directory where pseudopotential files are located [5]
        "tprnfor": True,  # Print forces [5]
        "tstress": True,  # Print stress [5]
    },
    "system": {
        "ibrav": 4,  # Bravais lattice index: 0 for direct lattice vector specification [5]
        "nat": 3,  # Number of atoms in the system (e.g., Mo: 25, S: 50) [5]
        "ntyp": 2,  # Number of atom types (e.g., Mo, S) [5]
        "ecutwfc": 60,  # Plane-wave cutoff energy in Rydberg [5].
        "ecutrho": 480,  # Charge density cutoff energy, often 4 times ecutwfc [8].
        "input_dft": "PBE",  # DFT exchange-correlation functional [8].
        "occupations": "fixed",  # How to handle Fermi level occupations [8].
    },
    "electrons": {
        "conv_thr": 1.0e-8,  # Self-consistent calculation convergence threshold [8].
        "mixing_mode": "plain",  # Charge density mixing mode [8].
        "mixing_beta": 0.7,  # Charge density mixing parameter [8].
    },
    "ions": {
        "ion_dynamics": "bfgs",  # Ionic dynamics algorithm (BFGS for geometry optimization) [8].
    },
}

esp_calc = Espresso(
    profile=profile,
    directory=output_full_dir,
    input_data=input_data,
    pseudopotentials=pseudos,
    tstress=True,
    tprnfor=True,
    kpts=(8, 8, 1),
    calculation="vc-relax",
)

atoms.calc = esp_calc

atoms.get_potential_energy()

print(f"Quantum ESPRESSO calculation initiated in: {output_full_dir}")
print("Check the .pwo and .err files for output and potential errors.")
