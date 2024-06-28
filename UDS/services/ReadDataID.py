class ReadDataID:
    def __new__(self, function, *args, **kwargs):
        if not hasattr(self, function):
            raise RuntimeError('function %s not supported.'%function)
        req = getattr(self, function)
        return req(*args)
        
    @classmethod
    def read_data_ID(cls, data_ID, *args):
        return ( '22 ' + data_ID + ''.join(args) )
