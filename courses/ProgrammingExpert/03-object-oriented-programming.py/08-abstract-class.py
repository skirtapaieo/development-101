class AbstractGame:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def start(self):
        raise NotImplementedError("Start method not implemented")

    @staticmethod
    def stop(self):
        raise NotImplementedError("Stop method not implemented")

    def play(self):
        self.start()
        self.stop()

    def __repr__(self):
        return self.name

