# -*- coding: utf-8 -*-

__title__ = 'py-statsd'
__version__ = '0.0.1'
__build__ = 0x000001
__author__ = 'Siavash Ghorbani'
__license__ = 'MIT'
__copyright__ = 'Copyright 2012 Siavash Ghorbani <siavash@tictail.com>'

import sys
import random
import socket
import logging
from pprint import pformat

class Statsd(object):

    def __init__(self, host='localhost', port=8125):
        self.host = host
        self.port = port
        self.addr = (host, port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def timing(self, stat, time, sample_rate=1):
        """
        Log timing information
        """
        stats = {}
        stats[stat] = "%d|ms" % time
        return self.send(stats, sample_rate)

    def increment(self, stats, sample_rate=1):
        """
        Increments one or more stats counters
        """
        return self.update_stats(stats, 1, sample_rate)

    def decrement(self, stats, sample_rate=1):
        """
        Decrements one or more stats counters
        """
        return self.update_stats(stats, -1, sample_rate)

    def update_stats(self, stats, delta=1, sampleRate=1):
        """
        Updates one or more stats counters by arbitrary amounts
        """
        if (type(stats) is not list):
            stats = [stats]
        data = {}
        for stat in stats:
            data[stat] = "%s|c" % delta

        return self.send(data, sampleRate)

    def send(self, data, sample_rate=1):
        """
        Send the metrics
        """
        sampled_data = {}

        if(sample_rate < 1):
            if random.random() <= sample_rate:
                for stat in data.keys():
                    value = data[stat]
                    sampled_data[stat] = "%s|@%s" %(value, sample_rate)
        else:
            sampled_data=data

        try:
            for stat in sampled_data.keys():
                value = data[stat]
                send_data = "%s:%s" % (stat, value)
                return self.sock.sendto(send_data, self.addr)
        except:
            logging.error("Unexpected error:", pformat(sys.exc_info()))
            pass
