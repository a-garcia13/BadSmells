class animal_legs:
  def __init__(self, fnumber, lbiped, pspicie):
    self.number = fnumber
    self.biped = lbiped
    self.spicie = pspicie

  def kind(self):
    print(self.biped+" "+self.kind)

  def printnumber(self):
    print(self.number)


class dog_legs(animal_legs):

    def __init__(self):
        animal_legs.__init__(self, 4, "no", "dog")

    def dog_kinf(self):
        self.kind()


class chair_legs(animal_legs):

    def __init__(self):
        animal_legs.__init__(self, 4, "no", "chair")

    def number(self):
        self.printnumber()
