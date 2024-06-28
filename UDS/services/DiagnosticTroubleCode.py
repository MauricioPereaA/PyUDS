class DiagnosticTroubleCode:
    def __new__(self, function, *args, **kwargs):
        if not hasattr(self, function):
            raise RuntimeError('function %s not supported.'%function)
        req = getattr(self, function)
        return req(*args)

    @classmethod
    def rqst_dtc_number_status_mask(cls, status_mask, *args):
        return ( '19 01 %s'%status_mask )
    
    @classmethod
    def rqst_dtc_by_status_mask(cls, status_mask, *args):
        return ( '19 02 %s'%status_mask )
    
    @classmethod
    def rqst_dtc_snapshot(cls, *args):
        raise NotImplementedError('This function has not been implemented yet.')
    
    @classmethod
    def rqst_snapshot_by_dtc(cls, *args):
        raise NotImplementedError('This function has not been implemented yet.')
    
   # Future Implementation.    'PLACE HOLDER'
   #@classmethod
    #def rqst_dtc_read_extended_data(cls, DTC, data_record, *args):
    #    return ( '19 06 {} {}'.format(DTC, data_record) )

    # Future Implementation.    'PLACE HOLDER'
    # @classmethod
    #def rqst_supported_dtcs(cls, *args):
    #    return ( '19 0A '+''.join(args))
    
    @classmethod
    def rqst_dtc_fault_detection_counter(cls, *args):
        raise NotImplementedError('This function has not been implemented yet.')


