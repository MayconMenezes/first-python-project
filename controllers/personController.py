import pickle

class PersonController(object):
  def __init__(self):
    self._people = []

  def addPerson(self, person):
    self._people.append(person)

  def removePerson(self, index):
    return self._people.pop(index)

  def save(self, filename):
    output = open(filename, 'wb')
    pickle.dump(self._people, output)

  def load(self, filename):
    file = open(filename, 'rb')
    self._people = pickle.load(file)