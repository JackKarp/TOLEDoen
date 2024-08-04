# PageMachine should start with an initializing state that initializes the GPIO pins
from page import Page
class PageMachine():
    
    def __init__(self, page_list, device) -> None:
        for i in page_list:
            assert type(i) is Page
        self.states = page_list
        self.current_index = 0
        self.current_state = self.states[0]
        self.device = device
        return
    
    def cycle(self) -> None:
        if self.current_state.is_flaggable:
            self.current_state.flag[0] = False

        self.current_index += 1
        self.current_index = self.current_index % len(self.states)
        self.current_state = self.states[self.current_index]
        print(self.current_state.name)

        # Checks for a flag object in the current page and runs it into the enter_func if there is one
        if self.current_state.is_flaggable:
            self.current_state.flag[0] = True
            self.current_state.on_enter_func(self.device, self.current_state)
        else:
            self.current_state.on_enter_func(self.device)
