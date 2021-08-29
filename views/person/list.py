import pyforms
from pyforms.basewidget import BaseWidget
from pyforms.controls import ControlList
from controllers.personController import PersonController
from views.person.create import PersonCreateView
from components.topmenu.topmenu    import TopMenuComponent

class PersonListView(TopMenuComponent, PersonController, BaseWidget):
    def __init__(self):
        PersonController.__init__(self)
        BaseWidget.__init__(self, 'List Person View')

        self._personList = ControlList('Registered Person',
            plusFunction = self.__addPersonBtnAction,
            minusFunction = self.__rmPersonBtnAction)

        self._personList.horizontalHeaders = ['First name', 'Middle name', 'Last name']

    def addPerson(self, personCreateView):
        super(PersonListView, self).addPerson(personCreateView)
        self._personList += [personCreateView._firstName, personCreateView._middleName, personCreateView._lastName]
        personCreateView.close()

    def removePerson(self, index):
        super(PersonListView, self).removePerson(index)
        self._personList -= index

    def __addPersonBtnAction(self):
        personCreateView = PersonCreateView()
        personCreateView.parent = self
        personCreateView.show()

    def __rmPersonBtnAction(self):
        self.removePerson( self._personList.selected_row_index )