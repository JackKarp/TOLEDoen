class Page():
    def __init__(self, name, on_enter_func, while_running_func=None) -> None:
        "Necessary Init"
        self.name = name
        self.on_enter_func = on_enter_func
        # The while_running_func should take a device argument
        self.while_running_func = while_running_func if while_running_func else lambda *x: x
        pass
    
    def on_enter_func() -> dict:
        "Should return a dict with information to be rendered"
        pass