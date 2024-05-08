class Feedback:
    def __init__(self, _id, userId, chatty_score, safety_score, punctuality_score, friendliness_score, comfortibility_score, UTT):
        self._id = _id
        self.userId = userId
        self.chatty_score = chatty_score
        self.safety_score = safety_score
        self.punctuality_score = punctuality_score
        self.friendliness_score = friendliness_score
        self.comfortibility_score = comfortibility_score
        self.UTT = UTT

    def __str__(self):
        return f"ID: {self._id}, User ID: {self.userId}, Chatty Score: {self.chatty_score}, Safety Score: {self.safety_score}, Punctuality Score: {self.punctuality_score}, Friendliness Score: {self.friendliness_score}, Comfortibility Score: {self.comfortibility_score}, UTT: {self.UTT}"
