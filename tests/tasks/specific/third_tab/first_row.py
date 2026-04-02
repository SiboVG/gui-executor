from gui_executor.exec import exec_ui

UI_MODULE_DISPLAY_NAME = "First Row of Tasks"


@exec_ui(immediate_run=True, use_script_app=True)
def immediate_run_script():
    print("[blue]The task has run successfully as a script[/]")


@exec_ui(immediate_run=True, use_kernel=True)
def immediate_run_kernel():
    print("[blue]The task has run successfully in kernel[/]")


@exec_ui(immediate_run=True, allow_kernel_interrupt=True)
def emergency_stop():
    print("[red]EMERGENCY STOP PRESSED[/red] (kernel possibly interrupted)")
