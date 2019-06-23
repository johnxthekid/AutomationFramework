import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), '..', '..', '..', '..'))
print(sys.path)

from appmanagers.WinAppManager import WinAppManager
from appmanagers.WinElementActions import WinElementActions
from pywinauto.findwindows import ElementNotFoundError


class SampleNotepadHelper:

    def __init__(self):
        self.app_auto = WinAppManager(WinAppManager.WIN32)
        self._notepad = None

    @property
    def notepad(self):
        return self._notepad

    @notepad.setter
    def notepad(self, notepad):
        self._notepad = notepad

    @notepad.deleter
    def notepad(self):
        self._notepad = None

    def open_notepad(self, location='Notepad.exe'):
        self._notepad = self.app_auto.open_app(location)
        return self._notepad

    def close_notepad(self):
        self.app_auto.close_app_instance(self._notepad)

    def user_exit_notepad(self):
        self.open_submenu('File', 'Exit')
        '''New window open with name Notepad'''
        file_window_dlg = self.app_auto.get_new_window_dialog()
        print(f"now on file window: {file_window_dlg.window_text()}")
        file_window_dlg.DontSave.click()

    def get_dialog_title(self, dialog=None):
        return self.app_auto.get_window_title(dialog)

    def open_submenu(self, top_menu, submenu):
        self._notepad.menu_select(f"{top_menu} -> {submenu}")
        return self.app_auto.get_new_window_dialog()

    def open_replace_menu(self):
        self.open_submenu('Edit', 'Replace')
        menu_window_dlg = self.app_auto.get_new_window_dialog()
        print(f"now on Menu window: {menu_window_dlg.window_text()}")
        assert(menu_window_dlg.window_text() == 'Replace'), "Incorrect window display"

    def close_replace_menu(self):
        menu_window_dlg = self.app_auto.get_new_window_dialog()
        try:
            menu_window_dlg.Cancel.click()
        except ElementNotFoundError:
            print("Replace window was already closed")
            return menu_window_dlg

    def type_values(self, value, with_spaces=True):
        edit_win = WinElementActions(self._notepad.Edit)
        edit_win.type_element_text(value, with_spaces)
        # self._notepad.Edit.type_keys(f'{value}', with_spaces=with_spaces)

    def get_editor_value(self):
        # self._notepad.Edit.texts()
        edit_win = WinElementActions(self._notepad.Edit)
        return edit_win.get_element_text()

    def get_notepad_menus(self):
        menu_list = self.app_auto.list_dialog_menu(self._notepad)
        clean_list = self.app_auto.get_clean_menus(menu_list)
        return clean_list


if __name__ == "__main__":
    note = SampleNotepadHelper()
    note.open_notepad()
    new_dlg = note.open_submenu("Edit", "Replace")
    print(f"New dialog: {note.get_dialog_title(new_dlg)}")
    note.close_replace_menu()
    note.open_replace_menu()
    note.close_replace_menu()
    note.type_values(f"{dir()}")
    print(f"values typed in editor: \n{note.get_editor_value()}")
    note.user_exit_notepad()
