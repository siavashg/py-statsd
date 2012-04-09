# -*- coding: utf-8 -*-
import statsd

def main():

    c = statsd.Client()
    for i in range(0, 50):
        c.increment('hello')

    for i in range(0, 50):
        c.timing('timed.hello', i, 0.5)

    for i in range(0, 50):
        c.decrement('hello')

if __name__ == '__main__':
    main()
