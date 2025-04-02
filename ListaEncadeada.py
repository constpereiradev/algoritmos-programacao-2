# Estudos da Matéria Algoritmos e Programação II, da UFMS, com o professor Samuel Ferraz.
# Aluna: Amanda da Conceição Pereira
# Módulo 1


class Nota:

  def __init__(self, nome, nota1, nota2):
    self.nome = nome
    self.nota1 = nota1
    self.nota2 = nota2


n = Nota("Amanda", 10, 10)
print(n.nome, n.nota1, n.nota2)
