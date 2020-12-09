class Event(list):
    def __init__(self, *args):
        super().__init__(args)

    def call(self, *args, **kwargs):
        return [ listener(*args, **kwargs) for listener in self ]

class EventDispatcher(dict):
    def call(self, event_name, *args):
        if event_name in self:
            self[event_name].call(*args)

    def subscribe(self, event_name, func):
        if event_name in self:
            self[event_name].append(func)

    def unsubscribe(self, event_name, func):
        if event_name in self:
            self[event_name].remove(func)
