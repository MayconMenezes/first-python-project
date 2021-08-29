from pyforms.controls   import ControlText

class TextFieldComponent():
  def __init__(self,  label, hasError, helperText):
    self._control = ControlText(label)
