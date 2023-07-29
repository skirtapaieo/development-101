

def generate_string(string, frequency):
    for char in string:
        for _ in range(frequency):
            yield char


class GenerateString:
    def __init__(self, string, frequency):
        self.string = string
        self.frequency = frequency
        self.char_index = 0
        self.freq_count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.char_index >= len(self.string):
            raise StopIteration

        result = self.string[self.char_index]
        self.freq_count += 1

        if self.freq_count >= self.frequency:
            self.freq_count = 0
            self.char_index += 1

        return result

