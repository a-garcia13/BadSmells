class legs:
  def __init__(self, fnumber):
    self.number = fnumber

  def printnumber(self):
    print(self.number)


class animals(legs):

    def __init__(self, lbiped, pspicie):
        legs.__init__(self, 4)
        self.biped = lbiped
        self.spicie = pspicie

    def dog_kind(self):
        self.kind()


class chairs(legs):

    def __init__(self):
        legs.__init__(self, 4)

