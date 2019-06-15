from lib.frontend.WinAppManager import WinAppManager


class WindowsExplorerActions:

    def __init__(self):
        pass


if __name__ == '__main__':
    app = WinAppManager(WinAppManager.WIN32)
    main_dlg = app.open_app('explorer.exe', 'FileExplorer')
    main_dlg.draw_outline()
    quick_search = main_dlg.child_window(class_name="Search Box")
    quick_search_textfield = main_dlg.child_window(auto_id="SearchEditBox")
    quick_edit_search = main_dlg.child_window(class_name="SearchEditBoxWrapperClass")
    quick_search_button = main_dlg.child_window(auto_id="SearchBoxSearchButton")

    search_toolbar = main_dlg.child_window(title="Address: Quick access", class_name="ToolbarWindow32")
    search_field = main_dlg.child_window(title="Quick access", class_name="Edit")

    # search_dropdown = main_dlg.child_window(title="Quick access", class_name="ComboBoxEx32")
    search_goto_button = main_dlg.child_window(title="Address band toolbar", class_name="ToolbarWindow32")
