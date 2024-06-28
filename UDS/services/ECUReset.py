class ECUReset:
    def __new__(self, function, *args, **kwargs):
        if not hasattr(self, function):
            raise AttributeError('function %s not supported.'%function)
        req = getattr(self, function)

        return req(*args)
        
    @classmethod
    def ecu_reset(cls, *args):
        data = '01' if True in filter(lambda x: isinstance(x, bool), args) else ''.join(args)
        return ( '11 ' + data  )
