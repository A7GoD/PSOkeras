class ProgressBar:
    def __init__(self, steps, updates=10):
        self.step = 0
        self.step_size = (steps // updates)
        self.total_steps = steps
        self.updates = updates
        print(self.step_size)
        bar = self._make_bar(0)
        print(bar)

    def update(self, i):
        print('i',i)
        print('step_size', self.step_size)
        if i % self.step_size > 0:
            return

        self.step = i // self.step_size
        bar = self._make_bar(i)

        print(bar)

    def done(self):
        self.step = self.total_steps
        bar = self._make_bar(self.updates)
        print(bar)

    def _make_bar(self, x):
        bar = f"Progress: {x}/{self.updates}"
        print(bar)
        return bar
