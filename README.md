# A simple statsd python client
Almost identical to the [client](https://github.com/etsy/statsd/blob/master/examples/python_example.py) included in the [statsd](https://github.com/etsy/statsd) examples, but slightly cleaner and with some minor optimizations such as not initating a new socket on each send and not requiring any local_settings.py file.
## Usage
    import statsd
    client = statsd.Client(host='localhost', port=8125)
    client.increment('my.value')
    client.timing('my.timed.value', 25)
  
