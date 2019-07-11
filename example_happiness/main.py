import csv
from rdkit.Chem import MolFromSmiles, Draw

labels = []
smiles = []

with open("smiles.csv", "r") as f:
    content = csv.reader(f)
    for row in content:
        name, smile = row
        labels.append(row[0])
        smiles.append(MolFromSmiles(row[1]))

img = Draw.MolsToGridImage(smiles,
                           molsPerRow=2,
                           subImgSize=(300, 300),
                           legends=labels)
img.save("happiness.png")
