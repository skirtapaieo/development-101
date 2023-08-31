class RunCodeInterface:
    def execute_code(self, code):
        return exec(code)

    def compile_code(self, code):
        return compile(code, '', 'exec')

class Code(RunCodeInterface):
    def __init__(self, code):
        self.code = code

    def execute(self):
        return self.execute_code(self.code)

    def compile(self):
        return self.compile_code(self.code)


