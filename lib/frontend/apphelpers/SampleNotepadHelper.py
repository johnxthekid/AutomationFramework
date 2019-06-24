from pywinauto.findwindows import ElementNotFoundError

from lib.frontend.appmanagers.WinAppManager import WinAppManager
from lib.frontend.appmanagers.WinElementActions import WinElementActions


class SampleNotepadHelper:
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

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

    def close_notepad(self, notepad_instance):
        self.app_auto.close_app_instance(notepad_instance)

    def user_exit_notepad(self, notepad_instance):
        self.open_submenu(notepad_instance, 'File', 'Exit')
        '''New window open with name Notepad'''
        file_window_dlg = self.app_auto.get_new_window_dialog()
        print(f"now on file window: {file_window_dlg.window_text()}")
        file_window_dlg.DontSave.click()

    def get_dialog_title(self, dialog=None):
        return self.app_auto.get_window_title(dialog)

    def open_submenu(self, notepad_instance, top_menu, submenu):
        notepad_instance.menu_select(f"{top_menu} -> {submenu}")
        return self.app_auto.get_new_window_dialog()

    def open_replace_menu(self, notepad_instance):
        self.open_submenu(notepad_instance, 'Edit', 'Replace')
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

    def type_values(self, notepad_instance, value, with_spaces=True):
        edit_win = WinElementActions(notepad_instance.Edit)
        edit_win.type_element_text(value, with_spaces)
        # self._notepad.Edit.type_keys(f'{value}', with_spaces=with_spaces)

    def get_editor_value(self, notepad_instance):
        # self._notepad.Edit.texts()
        edit_win = WinElementActions(notepad_instance.Edit)
        return edit_win.get_element_text()

    def get_notepad_menus(self, notepad_instance):
        menu_list = self.app_auto.list_dialog_menu(notepad_instance)
        clean_list = self.app_auto.get_clean_menus(menu_list)
        return clean_list


if __name__ == "__main__":
    note = SampleNotepadHelper()
    n_dlg = note.open_notepad()
    new_dlg = note.open_submenu(n_dlg, "Edit", "Replace")
    print(f"New dialog: {note.get_dialog_title(new_dlg)}")
    note.close_replace_menu()
    note.open_replace_menu(n_dlg)
    note.close_replace_menu()
    note.type_values(n_dlg, f"{dir()}")
    print(f"values typed in editor: \n{note.get_editor_value(n_dlg)}")
    note.user_exit_notepad(n_dlg)
