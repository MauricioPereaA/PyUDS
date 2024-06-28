class DiagnosticSession:
    def __new__(self, subfunction, *args, **kwargs):
        if not hasattr(self, subfunction):
            raise AttributeError('function %s not supported.'%subfunction)
        req = getattr(self, subfunction)

        return req()

    @staticmethod
    def default_session_control(*args, **kwargs):
        return ( '10 01' )
    
    @staticmethod
    def extended_session_control(*args, **kwargs):
        return ( '10 03' )
    
    @staticmethod
    def programming_session_control(*args, **kwargs):
        return ( '10 02' )
    
    @staticmethod
    def safety_session_control(*args, **kwargs):
        return ( '10 04' )