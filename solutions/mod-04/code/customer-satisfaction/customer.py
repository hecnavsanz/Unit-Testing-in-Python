class Customer:

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def send_promo_code(self):
        return 'Promo code sent'
