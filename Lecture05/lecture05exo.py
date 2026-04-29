import rdkit
from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem.Draw import IPythonConsole
IPythonConsole.ipython_useSVG=True

# ethanol = Chem.MolFromSmiles("CCO")
# ethylene = Chem.MolFromSmiles("C#C")
# print(ethanol)
# print(ethylene)
# img_ethanol = Draw.MolToImage(ethanol)
# img_ethanol.show()  # opens in your image viewer
# img_ethylene = Draw.MolToImage(ethylene)
# img_ethylene.show()

# butanol = Chem.MolFromSmiles("CCCO")
# tertbutanol = Chem.MolFromSmiles("CC(CO)C")
# vanillin = Chem.MolFromSmiles("c1(O)c(OC)cc(C=O)cc1")
# img_tertbutanol = Draw.MolToImage(tertbutanol)
# img_tertbutanol.show()
# img_vanillin = Draw.MolToImage(vanillin)
# img_vanillin.show()

smiles_list = ["CC(=O)OC1=CC=CC=C1C(=O)O", "c1c(OC(=O)C)c(C(=O)O)ccc1", "CC(=O)Oc1ccccc1C(=O)O"] 
# Convert mol from smiles, then mol to smiles
mol_list:list=[Chem.MolFromSmiles(s) for s in smiles_list]
backtosmiles_list:list = [Chem.MolToSmiles(s) for s in mol_list]
# Count unique smiles
print("Number of unique canonical smiles:",backtosmiles_list)
# Fill in here
