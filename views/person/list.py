import pyforms
from pyforms.basewidget import BaseWidget
from pyforms.controls import ControlList
from controllers.personController import PersonController
from views.person.create import PersonCreateView
from components.topmenu.topmenu import TopMenuComponent
from pyforms.controls import ControlDockWidget
class PersonListView(TopMenuComponent, PersonController, BaseWidget):
    def __init__(self):
        PersonController.__init__(self)
        BaseWidget.__init__(self, 'List Person View')
        TopMenuComponent.__init__(self)

        self._panel = ControlDockWidget()

        self._personList = ControlList('Registered Person',
            add_function = self.__addPersonBtnAction,
            remove_function = self.__rmPersonBtnAction)

        self._personList.horizontal_headers = ['First Name', 'Middle Name', 'Last Name']

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