class WriteDataID:
    def __new__(self, function, *args, **kwargs):
        if not hasattr(self, function):
            raise AttributeError('function %s not supported.'%function)
        req = getattr(self, function)

        return req(*args)
        
    @classmethod
    def write_data_ID(cls, data, *args):
        data = ''.join(data)
        return ( '2E ' + data + ''.join(args) )
