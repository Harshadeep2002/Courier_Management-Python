class TrackingNumberNotFoundException(Exception):
    def __init__(self,tracking_Number):
        super().__init__(f'TrackingNumber {tracking_number} is not found in the system')