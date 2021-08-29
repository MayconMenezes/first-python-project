import sys
from pyforms import start_app
from views.welcome.index import WelcomeView

sys.path.append('./')
if __name__ == "__main__":
  start_app(WelcomeView)