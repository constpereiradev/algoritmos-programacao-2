# Módulo 1


class Nota:

  def __init__(self, nome, nota1, nota2):
    self.nome = nome
    self.nota1 = nota1
    self.nota2 = nota2


n = Nota("SeuNomeAqui", 10, 10)
print(n.nome, n.nota1, n.nota2)