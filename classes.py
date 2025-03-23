import re 


class Estudante:
    def __init__(self, nome, curso, idade):
        self.nome = nome
        self.curso = curso
        self.idade = idade
    
    def __str__(self):
        return f"Meu nome é {self.nome} e gosto de {self.interesses}"
    
    # Getter para idade
    @property
    def idade(self):
        return self._idade
    
    # Setter para idade
    @idade.setter
    def idade(self, idade):        
        if re.search(r"^(\d+)$", idade):
            self._idade = idade
        else:
            raise ValueError("Idade inválida")            

    # Método que compila as páginas de interesse do estudante
    def paginas_de_interesse(self):
        paginas = []
        while True:
            try:
                interesse = input("Páginas seguidas: ").strip()
            except EOFError:
                self.interesses = ", ".join(paginas)
                return self.interesses
            else:
                paginas.append(interesse)


def main():
    estudante = Estudante("Amauri", "Engenharia Química", "20")
    print(estudante.paginas_de_interesse())
    print(estudante.interesses)


if __name__ == "__main__":
    main()
