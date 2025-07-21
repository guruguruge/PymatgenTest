from lxml import etree

tree = etree.parse("/home/gu/projects/PymatgenTest/MoS2_single.xml")
root = tree.getroot()

ns = {"qes": "http://www.quantum-espresso.org/ns/qes/qes-1.0"}

# 重要なエネルギー関連のタグをリストで用意しておく
energy_tags = ["fermi_energy", "total_energy", "etot"]

for tag in energy_tags:
    elem = root.find(f".//qes:{tag}", namespaces=ns)
    if elem is not None:
        print(f"{tag}: {elem.text}")
    else:
        print(f"{tag}: 見つからず")

# 格子ベクトルの取得（cellのa1, a2, a3）
cell_vectors = root.findall(
    ".//qes:cell/qes:a1 | .//qes:cell/qes:a2 | .//qes:cell/qes:a3", namespaces=ns
)
print("格子ベクトル:")
for vec in cell_vectors:
    print(" ", vec.text)

# 原子位置の取得
atoms = root.findall(".//qes:atomic_positions/qes:atom", namespaces=ns)
print("原子位置:")
for a in atoms:
    print(f"  {a.attrib.get('name', '?')}: {a.text}")

# 電荷密度とポテンシャルの有無
rho = root.find(".//qes:charge_density", namespaces=ns)
vpot = root.find(".//qes:local_potential", namespaces=ns)
print("電荷密度:", "あり" if rho is not None else "なし")
print("ポテンシャル:", "あり" if vpot is not None else "なし")
