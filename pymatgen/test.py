from dotenv import load_dotenv
import os
from pymatgen.ext.matproj import MPRester

load_dotenv()

with MPRester(os.getenv("MATPRO_API_KEY")) as m:
    material_ids = m.get_material_ids("MoS2")
    print(material_ids)

first_entry = m.get_entry_by_material_id(material_ids[0])
print(first_entry)