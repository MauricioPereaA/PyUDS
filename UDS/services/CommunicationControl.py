class CommunicationControl:
    def __new__(self, function, *args, **kwargs):
        if not hasattr(self, function):
            raise AttributeError('function %s not supported.'%function)
        req = getattr(self, function)
        return req(*args)
    
    @classmethod
    def communication_control(cls, enabled=False):
        status = { True  : '00', False : '03' }
        return( '28 '+ status[enabled] +' 01' )