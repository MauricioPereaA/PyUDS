class ControlDTCSettings:
    def __new__(self, function, *args, **kwargs):
        if not hasattr(self, function):
            raise AttributeError('function %s not supported.'%function)
        req = getattr(self, function)
        return req(*args)

    @classmethod
    def dtc_settings(cls, enabled=False, *args):
        status = { True  : '01', False : '02' }
        if not isinstance(enabled, bool):
            enabled = True if enabled == 'on' else False
        
        return('85 ' + status[enabled])
