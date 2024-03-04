from entity.User import User
class Courier(User):
    def __init__(self):
        super().__init__()
        self.courierID = 0
        self.senderName = ' '
        self.senderAddress = ' '
        self.receiverName = ' '
        self.receiverAddress = ' '
        self.weight = 0.0
        self.status = ' '
        self.trackingNumber = 0
        self.deliveryDate = ' '
        self.userID = 0

    #Setters

    def set_courierID(self,value):
        self.courierID = value

    def set_senderName(self,value):
        self.senderName = value

    def set_senderAddress(self,value):
        self.senderAddress = value

    def set_receiverName(self,value):
        self.receiverName = value

    def set_receiverAddress(self,value):
        self.receiverAddress = value

    def set_weight(self,value):
        self.weight = value

    def set_status(self,value):
        self.status = value

    def set_trackingNumber(self,value):
        self.trackingNumber = value

    def set_deliveryDate(self,value):
        self.deliveryDate = value

    def set_userID(self,value):
        self.userID = value

    #Getters

    def get_courierID(self):
        return self.courierID

    def get_senderName(self):
        return self.senderName

    def get_senderAddress(self):
        return self.senderAddress

    def get_receiverName(self):
        return self.receiverName

    def get_receiverAddress(self):
        return self.receiverAddress

    def get_weight(self):
        return self.weight

    def get_status(self):
        return self.status

    def get_trackingNumber(self):
        return self.trackingNumber

    def get_deliveryDate(self):
        return self.deliveryDate

    def get_userID(self):
        return self.userID

    def __str__(self):
        return f'courierID : {self.courierID}\n' \
               f'senderName: {self.senderName} senderAddress : {self.senderAddress}\n' \
               f'receiverName : {self.receiverName} receiverAddress : {self.receiverAddress}\n' \
               f'weight : {self.weight} kg status : {self.status}\n' \
               f'trackingNumber : {self.trackingNumber} deliveryDate : {self.deliveryDate} userId : {self.userID}'


