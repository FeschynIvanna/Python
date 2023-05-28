from pen_manager import PenManager


class SetPenManager:
    def __init__(self, manager: PenManager):
        self.manager = manager
        self.current_index = -1

    def __iter__(self):
        for pen in self.manager:
            for set_item in pen.pattern:
                yield set_item

    def __next__(self):
        self.current_index += 1
        if self.current_index >= len(self.manager):
            raise StopIteration
        return self.manager[self.current_index].pattern

    def __len__(self):
        length = 0
        for pens in self.manager:
            length += len(pens.pattern)
        return length

    def __getitem__(self, index):
        for pens in self.manager:
            item = pens[index].pattern
        return item
