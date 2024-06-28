class TesterPresent:
    def __new__(self, function, *args, **kwargs):
        if not hasattr(self, function):
            raise AttributeError('function %s not supported.'%function)
        req = getattr(self, function)

        return req()

    @classmethod
    def start_tester_present(cls, *args):
        print('Tester present has started!')
        return ( '3E 80' )

    @classmethod
    def stop_tester_present(cls, *args):
        print('Tester present has stopped!')
        return ( '3E 00' )