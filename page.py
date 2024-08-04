class Page():
    def __init__(self, name, on_enter_func, flag=None) -> None:
        "Necessary Init"
        self.name = name
        self.on_enter_func = on_enter_func
        if flag:
            self.flag = flag
        pass