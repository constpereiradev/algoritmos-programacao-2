# Módulo 1


class Nota:

  def __init__(self, nome, nota1, nota2):
    self.nome = nome
    self.nota1 = nota1
    self.nota2 = nota2

  def alteraNome(self, nome):
    self.nome = nome


n = Nota("Amanda", 10, 10)
n.alteraNome("Amanda Pereira")
print(n.nome, n.nota1, n.nota2)
