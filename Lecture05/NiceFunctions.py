# import py3Dmol
from rdkit import Chem
from rdkit.Chem import AllChem
import numpy as np

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

### PRINTING ALL ATOMS FORM A MOL
def printallatoms(molecule:Chem.Mol):
    allatoms=[atom.GetSymbol() for atom in molecule.GetAtoms()]
    print(allatoms)

### CHECKING IF THE PASSED STRING IS A VALID ATOMIC SYMBOL
def is_valid_atom(symbol: str) -> bool:
    try:
        atom = Chem.Atom(symbol)
        return atom
    except Exception:
        return False

###CREATING AN ARRAY OF ATOM INDEXES OF A CERTAIN TYPE FROM A MOL
def all_indexes_of_atom(molecule:Chem.Mol,Atom:str):
    if(is_valid_atom(Atom)):
         all_atoms=[]
         for my_atom in molecule.GetAtoms():
              if my_atom.GetSymbol()==Atom:
                   all_atoms.append(my_atom.GetIdx())
    return all_atoms
   