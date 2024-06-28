class ReadDataByPeriodicIdentifier:
    def __new__(self, function, *args, **kwargs):
        if not hasattr(self, function):
            raise AttributeError('function %s not supported.'%function)
        req = getattr(self, function)

        return req(*args)
        
    @classmethod
    def read_periodic_data_id(cls, DDDID, rate, *args):
        return ( '2A {0} {1} {2}'.format(rate, DDDID, ''.join(args)) )

    @classmethod
    def stop_periodic_data(cls, *args):
        params = '' if True in args else ''.join(args)
        return ( '2A 04 %s'%params )


