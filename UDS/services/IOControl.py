class IOControl:
    def __new__(self, function, *args, **kwargs):
        if not hasattr(self, function):
            raise AttributeError('function %s not supported.'%function)
        req = getattr(self, function)

        return req(*args)
    
    @classmethod
    def io_return_control(cls, did, *args):
        return ( '2F {} 00'.format(did) + ''.join(args) )

    # Future Implementation.    'PLACE HOLDER'
    #@classmethod
    #def io_reset_to_default(cls, did, control_mask, *args):
        #return ( '2F {} 01 {}'.format(did, control_mask) + ''.join(args) )

    # Future Implementation.    'PLACE HOLDER'
    #@classmethod
    #def io_freeze_current_state(cls, did, control_mask, *args):
        #return ( '2F {} 02 {}'.format(did, control_mask) + ''.join(args) )    
    
    # Future Implementation.    'PLACE HOLDER'
    #@classmethod
    #def io_short_term_adjustment(cls, did, control_mask, *args):
        #return ( '2F {} 03 {}'.format(did, control_mask) + ''.join(args) )

