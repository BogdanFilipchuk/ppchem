# import py3Dmol
from rdkit import Chem
from rdkit.Chem import AllChem
# Helpful function from a blog (https://rdkit.blogspot.com/2016/07/a-recent-post-on-in-pipeline-talked.html)
def drawit(m,p=None,confId=-1):
        mb = Chem.MolToMolBlock(m,confId=confId) # Returns SDF file as a string
        if p is None:
            p = py3Dmol.view(width=400,height=400)
        p.removeAllModels()
        p.addModel(mb,'sdf') 
        p.setStyle({'stick':{}})
        p.setBackgroundColor('white')
        p.zoomTo()
        return p.show()


import numpy as np
from rdkit.Chem import AllChem
clavulanic_acid_smiles = "O=C2N1[C@H](C(/O[C@@H]1C2)=C/CO)C(=O)O"
# Your code here
clavacid:Chem.Mol = Chem.MolFromSmiles(clavulanic_acid_smiles)
clavacid3d = Chem.AddHs(clavacid)
AllChem.EmbedMolecule(clavacid3d)

###DRAWS 3D
# drawit(clavacid3d)

### PRINTS ALL COORDINATES
# print(Chem.MolToMolBlock(clavacid3d))

### PRINTING ALL THE ATOMS
# print([atom.GetSymbol() for atom in (clavacid3d.GetAtoms())])

def printallatoms(molecule:Chem.Mol):
    allatoms=[atom.GetSymbol() for atom in molecule.GetAtoms()]
    print(f"Atoms in {str(molecule)}: ",allatoms)
printallatoms(clavacid)
