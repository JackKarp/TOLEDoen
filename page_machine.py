# PageMachine should start with an initializing state that initializes the GPIO pins
class PageMachine():
    
    def __init__(self, page_list) -> None:
        self.states = page_list
        self.on_init()
        self.current_index = 0
        self.current_state = self.states[0]
        return
    def on_init():
        "Write pins and set up GPIO"
        pass
    
    def cycle(self):
        self.current_index += 1
        self.current_index = self.current_index % len(self.states)
        self.current_state = self.states[self.current_index]
        self.current_state.on_enter_func()
        pass
