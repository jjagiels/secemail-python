class packet():
   command = 0
   message = 0
   user = "null"
   salt = "null"
   password = "null"
   key = "null"
   recipient = "null"
   date = "null"
   subject = "null"
   body = "null"

   def prepNewUser(self, user, salt,  password, key):
       self.user = user
       self.salt = salt
       self.password = password
       self.key = key

   def prepLogin(self, user, password):
       self.user = user
       self.password = password

   def sendReceive(self, user, recipient, subject, body, date):
       self.user = user
       self.recipient = recipient
       self.subject = subject
       self.body = body
       self.date = date
