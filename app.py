import sys
from pyforms import start_app
from views.person.list import PersonListView

sys.path.append('./')
if __name__ == "__main__":
  start_app(PersonListView)