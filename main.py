from time import sleep

from queue import Queue

a = Queue('A')
b = Queue('B')
c = Queue('C')


def letter_selection():
    letter = input('Dzień dobry, proszę wybrac literę A, B lub C w zależnosci od sprawy do załatwienia: \n'
                   'A - Rejestracja pojazdu \n'
                   'B - Prawo jazdy \n'
                   'C - Dowody osobiste \n'
                   ': '
                   ).lower()
    if letter == 'a':
        a.queue_lenght()
        sleep(10)
        a.add_queue_lenght()
        letter_selection()
    if letter == 'b':
        b.queue_lenght()
        sleep(10)
        b.add_queue_lenght()
        letter_selection()
    if letter == 'c':
        c.queue_lenght()
        sleep(10)
        c.add_queue_lenght()
        letter_selection()


if __name__ == '__main__':
    letter_selection()
