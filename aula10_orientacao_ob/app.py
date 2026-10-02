from aluno import Aluno
from disciplina import Disciplina

# criar / instanciar 1 aluno
aluno1 = Aluno("joao", "123456", "Ciência da computação")

# criar / instanciar 2 disciplinas
sers = Disciplina( "Soluçoes renovaveis", "tritiack")
model_mat = Disciplina( "Modelagem Matematica", "Roberto")

#matricular o aluno nas duas disciplinas
aluno1.matricular(sers)
aluno1.matricular(model_mat)

#adicionar notas do aluno referente a disciplina

aluno1.adicionar_nota(sers,10)
aluno1.adicionar_nota(model_mat,8)
aluno1.adicionar_nota(model_mat,5)
aluno1.adicionar_nota(model_mat,3)

print(aluno1.calcular_media_d(model_mat))


