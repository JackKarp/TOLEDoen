class Page():
    def __init__(self, name, on_enter_func, is_flaggable=False) -> None:
        "Necessary Init"
        self.name = name
        self.on_enter_func = on_enter_func
        self.is_flaggable = is_flaggable
        if is_flaggable:
            self.flag = [True]
        pass