class Disciplina:
    def __int__(self, nome, professor):
        self.nome = nome
        self.professor = professor

    def exibir_infos(self):
        print(f"Disciplina: {self.nome} | prof.: {self.professor}")


#temporario
#cs = Disciplina("computer science","mauamau")
#print(cs.professor)