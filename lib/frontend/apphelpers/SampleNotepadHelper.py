from os import path
import sys
sys.path.append(path.join(path.dirname(__file__), "..", "..", ".."))
print(sys.path)

from pywinauto.findwindows import ElementNotFoundError

from lib.frontend.appmanagers.WinAppManager import WinAppManager
from lib.frontend.appmanagers.WinElementActions import WinElementActions


class SampleNotepadHelper:
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    _notepad = None
    _menu_dlg = None

    def __init__(self):
        self.app_mgr = WinAppManager(WinAppManager.WIN32)

    @property
    def notepad(self):
        return self.app_mgr.get_app_instance(self._notepad)

    @notepad.setter
    def notepad(self, notepad):
        self._notepad = notepad

    @notepad.deleter
    def notepad(self):
        self.app_mgr.delete_app_instance(self.notepad)
        self._notepad = None

    def open_notepad(self, location='Notepad.exe'):
        notepad_id, self._notepad = self.app_mgr.open_app(location)
        return notepad_id

    def close_notepad(self, notepad_id):
        self.app_mgr.close_app_instance(notepad_id)

    def user_exit_notepad(self, notepad_id):
        self.open_submenu(notepad_id, 'File', 'Exit')
        '''New window open with name Notepad'''
        file_window_dlg = self.app_mgr.get_new_window_dialog()
        print(f"now on file window: {file_window_dlg.window_text()}")
        file_window_dlg.DontSave.click()

    def get_dialog_title(self, notepad_id):
        notepad_app = self.app_mgr.get_app_instance(notepad_id)
        return self.app_mgr.get_window_title(notepad_app)

    def open_submenu(self, notepad_id, top_menu, submenu):
        notepad_app = self.app_mgr.get_app_instance(notepad_id)
        notepad_app.menu_select(f"{top_menu} -> {submenu}")
        self._menu_dlg = self.app_mgr.get_new_window_dialog()

    def close_submenu(self):
        try:
            self._menu_dlg.Cancel.click()
        except ElementNotFoundError:
            print("Submenu window was already closed")

    def open_replace_menu(self, notepad_id):
        self.open_submenu(notepad_id, 'Edit', 'Replace')
        print(f"now on Menu window: {self._menu_dlg.window_text()}")
        assert(self._menu_dlg.window_text() == 'Replace'), "Incorrect window display"

    def type_values(self, notepad_id, value, with_spaces=True):
        notepad_app = self.app_mgr.get_app_instance(notepad_id)
        edit_win = WinElementActions(notepad_app.Edit)
        edit_win.type_element_text(value, with_spaces)

    def get_editor_value(self, notepad_id):
        notepad_app = self.app_mgr.get_app_instance(notepad_id)
        edit_win = WinElementActions(notepad_app.Edit)
        return edit_win.get_element_text()

    def get_notepad_menus(self, notepad_id):
        notepad_app = self.app_mgr.get_app_instance(notepad_id)
        menu_list = self.app_mgr.list_dialog_menu(notepad_app)
        clean_list = self.app_mgr.get_clean_menus(menu_list)
        return clean_list


if __name__ == "__main__":
    note = SampleNotepadHelper()
    note.open_notepad()
    note.open_submenu("Edit", "Replace")
    print(f"New dialog: {note.get_dialog_title()}")
    note.close_replace_menu()
    note.open_replace_menu()
    note.close_replace_menu()
    note.type_values(f"{dir()}")
    print(f"values typed in editor: \n{note.get_editor_value()}")
    note.user_exit_notepad()
