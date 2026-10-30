"""
6. Programe um pato.
"""

class Pato:
  def __init__ (self, nome, fase):
    self.nome = nome
    self.fase = fase
    self.fome = 1

  def atividade(self):

    if self.fase == "filhote":
      print(f"O patinho {self.nome} está brincando na água")
      print("QUACK QUACK!")
      print("~"*20)

    else:
      print(f"A pata Sra.{self.nome} está passeando com os seus patinhos")
      print("QUACK QUACK! Vamos lá crianças...")


  def comer(self):

    if self.fome >= 5:
      if self.fase == "filhote":
        print(f"\nO patinho {self.nome} está comendo papinha.")
      else:
        print(f"\nA pata Sra.{self.nome} está comendo e cuidando dos patinhos.")

    elif self.fome < 5:
       if self.fase == "filhote":
          print(f"\nA dona Pata já alimentou o patinho {self.nome}")
       else:
        print(f"\nA pata Sra.{self.nome} já se alimentou e cuidou dos patinhos.")

pato = Pato("Peninha", "filhote")
pato.atividade()
pato.comer()
