from statemachine import StateMachine, State

class PageMachine(StateMachine):
    "A machine that switches between pages (states)"
    home = State(initial=True)
    canvas = State()
    weather = State()

    cycle = (
    home.to(canvas)
    | canvas.to(weather)
    | weather.to(home)
    )

    def before_cycle(self, event: str, source: State, target: State, message: str = ""):
        message = ". " + message if message else ""
        return f"Running {event} from {source.id} to {target.id}{message}"