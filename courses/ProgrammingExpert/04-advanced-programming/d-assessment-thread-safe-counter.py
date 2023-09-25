# Copyright © 2022 AlgoExpert LLC. All rights reserved.

import threading


class WordCounter:
    def __init__(self):
        self.lock = threading.Lock()
        self.word_counts = {}

    def process_text(self, text):
        words = text.split(" ")
        for word in words:
            self._increment_word_count(word)

    def get_word_count(self, word):
        self.lock.acquire()
        count = self.word_counts.get(word, 0)
        self.lock.release()
        return count

    def _increment_word_count(self, word):
        self.lock.acquire()
        self.word_counts[word] = self.word_counts.get(word, 0) + 1
        self.lock.release()
