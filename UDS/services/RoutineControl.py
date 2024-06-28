class RoutineControl:
    def __new__(self, function, *args, **kwargs):
        if not hasattr(self, function):
            raise RuntimeError('function %s not supported.'%function)
        req = getattr(self, function)
        return req(*args)

    @classmethod
    def start_routine(cls, data, *args, **kwargs):
        # Data must be an array val
        data = ''.join(data)
        return ( '31 01 ' + data + ''.join(args) )

    @classmethod
    def request_routine_result(cls, data, *args, **kwargs):
        data = ''.join(data)
        return ( '31 02 ' + data + ''.join(args) )
