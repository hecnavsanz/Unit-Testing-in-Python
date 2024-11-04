class Survey:

    def __init__(self, customer):
        self.customer = customer
        self.status = 'not completed'
        self.answers = []

    def set_customer(self, customer):
        self.customer = customer

    def get_customer(self):
        return self.customer

    def set_status(self, status):
        self.status = status

    def get_status(self):
        return self.status

    def add_answer(self, answer):
        self.answers.append(answer)

    def compute_csat_score(self):
        score = int(sum(self.answers) / len(self.answers) * 10 + 0.5)
        return score
