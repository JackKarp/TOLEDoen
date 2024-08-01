class Page():
    def __init__(self, name, on_enter_func) -> None:
        "Necessary Init"
        self.name = name
        self.on_enter_func = on_enter_func
        pass