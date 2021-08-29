from views.person.list import PersonListView
from pyforms.basewidget import BaseWidget
from pyforms.controls import ControlButton
from views.person.list import PersonListView

class WelcomeView(BaseWidget):
  def __init__(self):
    super().__init__('Welcome Window')
    self._runButton = ControlButton('Run')
    self._runButton.value = self.__runEvent

    self._formset = [
      ('_runButton')
    ]

  def __runEvent(self):
    personListView = PersonListView()
    personListView.parent = self
    personListView.show()