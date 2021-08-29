import sys
import pyforms
from pyforms.basewidget import BaseWidget
from pyforms.controls import ControlText
from pyforms.controls import ControlButton
from models.personModel import PersonModel

sys.path.append('../../')
class PersonCreateView(PersonModel, BaseWidget):
  def __init__(self):
    PersonModel.__init__(self, '', '', '')
    BaseWidget.__init__(self, 'Create Person View')

    self._firstNameField = ControlText('First Name')
    self._middleNameField = ControlText('Middle Name')
    self._lastNameField = ControlText('Last Name')
    self._fullNameField = ControlText('Full Name')
    self._buttonField = ControlButton('Save This Person')

    self._buttonField.value = self.__buttonAction

  def __buttonAction(self):
    self._firstName = self._firstNameField.value
    self._middleName = self._middleNameField.value
    self._lastName = self._lastNameField.value
    self._fullNameField.value = self._fullName

    if self.parent != None: self.parent.addPerson(self)