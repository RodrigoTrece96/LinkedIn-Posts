from rdkit import Chem
from rdkit.Chem import Descriptors, Draw, rdMolDescriptors
from os import system


def main():
    print(avaliar_molecula())


def avaliar_molecula():
    while True:
        molecula = Chem.MolFromSmiles(input("Digite uma molécula na forma SMILES: "))

        try:
            molecula_img = Draw.MolToImage(molecula)
            molecula_img.save("imagem_molecula.png")
        except ValueError:
            system("cls")
            print("A molécula deve ser inserida de forma simplificada.\nExemplo: Etanol --> (CCO)")
        else:
            molecula_formula = rdMolDescriptors.CalcMolFormula(molecula)
            return f"A massa de {molecula_formula} é: {round(Descriptors.MolWt(molecula), 2)}"


if __name__ == "__main__":
    main()
