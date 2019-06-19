from os import environ
from sys import path

from pywinauto.application import Application
from pywinauto import Desktop
from pywinauto.timings import wait_until, TimeoutError
from pywinauto.findwindows import ElementNotFoundError, find_windows, WindowNotFoundError
from retrying import retry
from tempfile import NamedTemporaryFile

import logging
log = logging.getLogger(__name__)


class WinAppManager:
    UIA = "uia"
    WIN32 = "win32"
    EXISTING_APP_PROCESS = []

    def __init__(self, app_type="uia"):
        '''
        Class to initialized the main application for automation
        :param app_type: the backend type for the applicaiton UIA or WIN32
        '''
        self.app = Application(backend=app_type)
        self.desktop_app = Desktop(backend=app_type)

    def open_app(self, app_location, app_name=None, timeout=None, retry_value=None):
        """
        Opens the application to be tested
        :param app_location: Location of the application to automate
        :param app_name: Window text property name of the application
        :param timeout: time out value before retrying to launch the application
        :param retry_value: number of retries to launch the application
        :return: returns the application instance
        """
        log.info("Starting application")
        self.app.start(cmd_line=app_location, timeout=timeout, retry_interval=retry_value)

        log.debug("retrieving the Application dialog")
        try:
            app_dlg = self.app.top_window()
            app_process = self.app.process
        except RuntimeError:
            if app_name is not None:
                log.debug("No windows found through Application. Using Desktop instead")
                app_dlg = self.desktop_app[app_name]
                app_process = app_dlg.element_info.process_id
            else:
                raise RuntimeError("No windows found through Application, Provide an app_name to connect via Desktop backend class")

        app_dlg.wait('visible', timeout)

        for counter in range(5):
            if app_process in self.__class__.EXISTING_APP_PROCESS:
                if counter == 4:
                    raise ElementNotFoundError("Could not get the correct Application Process")
            else:
                log.info(f"New application process started successfully. Process ID {self.app.process}")
                break

        self.__class__.EXISTING_APP_PROCESS.append(app_process)
        return app_dlg

    @retry(stop_max_attempt_number=3)
    def connect_to_app(self, app_location):
        '''
        function that returns the instance of the Application being automated
        :param app_location: location of the application to automate
        :return: instance of the application under test
        '''
        return self.app.connect(path=app_location).top_window()

    def list_desktop_windows(self):
        """
        Displays list of top level windows active on the desktop
        :return: Name of desktop windows
        """
        return [app_window._element_info.name for app_window in self.desktop_app.windows(visible_only=True, enabled_only=True)]

    @staticmethod
    def get_window_dialog(app_type, handle_id):
        """
        returns the window dialog for handle ID provided
        :param app_type: the backend type for the applicaiton UIA or WIN32
        :param handle_id: the handle ID of the application
        :return: returns the dialog object for the window
        """
        return Application(backend=app_type).connect(handle=handle_id).window(handle=handle_id)

    def get_app_display_state(self):
        """
        :return: the display state of the application
        """
        pass

    def list_dialog_children(self):
        """
        :return: list of children from the dialog window
        """
        return [child.window_text() for child in self.app.top_window().children()]

    def list_dialog_child_windows(self, dialog_instance):
        """
        List the child windows as an object
        :return: Object list of child windows
        """
        # todo: Finish this method to return the correct list of child windows
        main_lst = NamedTemporaryFile()
        # main_lst.write()
        main_lst.close()
        main_dlg.print_control_identifiers(filename=main_lst.name)
        child_list2 = []
        final_lst = {}
        with open(main_lst.name, 'r') as main_child:
            child_list = [line for line in main_child if 'child_window' in line]
            child_level = child_list.count('|')
            for n_window in child_list:
                child_list2.append(n_window[n_window.find('(') + 1: n_window.find(')') - 1])
            for index, n_window2 in enumerate(child_list2):
                _a = n_window2.split(',')
                for _b in _a:
                    _c = _b.split('=')
                    final_lst.update({f'child{index}': {_c[0]: _c[1]}})

        return final_lst

    @staticmethod
    def list_dialog_menu(dialog_instance):
        """
        List the top level menus for the current window dialog
        :param dialog_instance: dialog instance for the current window
        :return:
        """
        return [menu['text'] for menu in dialog_instance.menu_items()]

    def list_dialog_menu_submenu(self, dialog_instance, menu_name):
        """
        List the sub menus for the current window dialog
        :param dialog_instance: dialog instance for the current window
        :param menu_name: Top level menu name
        :return:
        """
        top_menus = self.__class__.list_dialog_menu(dialog_instance)
        if menu_name in top_menus:
            return [subs['text'] for subs in dialog_instance.menu_items()[top_menus.index(menu_name)]['menu_items']['menu_items']]
        else:
            raise ElementNotFoundError(f"{menu_name} does not exist in the current list of menus below:\n{top_menus}")

    def get_clean_menus(self, menu_list):
        """
        removes the special characters from the menu name
        :param dialog_instance: dialog instance for the current window
        :param menu_list:   List of menus
        :return:
        """

        temp_m = [m_clean.replace("&", "") for m_clean in menu_list]
        sub_menu_clean = [sub_value.split("\t")[0] for sub_value in temp_m]

        return sub_menu_clean

    def remove_app_process(self, app_process_id):
        """
        Removes the specified application instance
        :param app_process_id: process id of the application instance to be removed
        :return:
        """
        pass

    def get_new_window_dialog(self):
        """
        Returns the dialog of the application being automated
        :return: Dialog object of the new page in the application
        """
        # todo: add a new method that provides the name of the new dialog
        return self.app[self.app.top_window().window_text()]

    @staticmethod
    def get_app_handle(app_instance):
        """
        returns the handle id for the application instance being automated
        :param app_instance: the instance that is being automated
        :return: handle_id of the application
        """
        return app_instance.wrapper_object().handle

    @staticmethod
    def get_app_process(dialog_instance):
        """
        returns the process id for the application instance being automated
        :param dialog_instance: the instance of the dialog for the application
        :return: process_id of the application
        """
        log.info("Retrieving the application process id")
        return dialog_instance.wrapper_object().process_id()

    @classmethod
    def get_app_handle_list(cls, app_instance=None, process_id=None):
        """
        returns the list of handles found for the application instance
        :param app_instance: the instance of the application running
        :param process_id: the process id of the application
        :return: the list of handles found
        """
        if app_instance is not None:
            handles = find_windows(process=cls.get_app_process(app_instance))
        elif process_id is not None:
            handles = find_windows(process=process_id)
        else:
            return AttributeError("application instance or process requires to retrieve the correct handles list")

        return handles

    def close_app_instance(self, app_instance=None):
        """draw_outline("red")
        closes the instance of the application provided
        :param app_instance: the instance of the application running
        :return: True if the application was closed successfully
        """
        if app_instance is None:
            app_window = self.app.top_window()

        try:
            if app_window.is_visible():
                app_window.close()
            else:
                log.debug("Application Window was not found. Already closed")
        except ElementNotFoundError:
            log.debug("Application Window was not found. Already closed")

        return True


if __name__ == '__main__':
    app_auto = WinAppManager(WinAppManager.WIN32)
    main_dlg = app_auto.open_app('Notepad.exe')
    '''Each menu in Notepad is a different window'''
    main_window_name = main_dlg.window_text()
    print(f"now on main window: {main_window_name}")
    main_dlg.menu_select("Edit -> Replace")
    # main_dlg.menu_select("Format -> Font")
    '''New window open with name Replace'''
    # menu_window_name = app_obj.top_window().window_text()
    menu_window_dlg = app_auto.get_new_window_dialog()
    # app_obj[menu_window_name].Cancel.click()
    print(f"now on Menu window: {menu_window_dlg.window_text()}")
    menu_window_dlg.Cancel.click()
    main_dlg.Edit.type_keys(f"Hi from Python interactive prompt {dir()}", with_spaces=True)

    '''Get list of menu options for the application'''
    # menu_names = [menu['text'] for menu in main_dlg.menu_items()]
    menu_names = app_auto.list_dialog_menu(main_dlg)
    print(f'Menu names: \n{menu_names}')
    print(f'clean Menu: \n{app_auto.get_clean_menus(menu_names)}')
    sub_menu = app_auto.list_dialog_menu_submenu(main_dlg, menu_names[0])
    print(f'Submenu for {menu_names[0]}:\n{sub_menu}')
    print(f'Clean Submenu: \n{app_auto.get_clean_menus(sub_menu)}')
    main_dlg.menu_select("File -> Exit")
    '''New window open with name Notepad'''
    # file_window_name = app_obj.top_window().window_text()
    file_window_dlg = app_auto.get_new_window_dialog()
    print(f"now on file window: {file_window_dlg.window_text()}")
    # app_obj[file_window_name].DontSave.click()
    file_window_dlg.DontSave.click()