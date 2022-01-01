from django.contrib import messages


class UserObservable:
    def __init__(self):
        self.observers = []
        self.state = None

    def add_observer(self, observer):
        self.observers.append(observer)

    def set_state(self, new_state):
        self.state = new_state

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.state)


class UserObserver:
    def __init__(self, observer):
        self.observer = observer

    def update(self, state):
        messages.success(self.observer, state)
