class Queue:
    def __init__(self,letter: str, length: int = 1):
        self.length = length
        self.letter = letter

    def queue_lenght(self):
        print(f"{self.letter}{self.length}")

    def add_queue_lenght(self):
        self.length += 1


if __name__ == '__main__':
    # a = Queue('A')
    # a.add_queue_lenght()
    # a.queue_lenght()
    # a.add_queue_lenght()
    # a.queue_lenght()
    # b = Queue('B')
    # b.add_queue_lenght()
    # b.queue_lenght()

