class Category:
  

  def __init__(self, category):
    self.category = category
    self.ledger = list()
    self.balance = 0

  def check_funds(self, amount):
    if amount > self.balance:
      return False
    else:
      return True

  def deposit(self, amount, description=""):
    self.balance += amount
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description=""):
    if self.check_funds(amount) == False:
      return False
    else:
      self.balance -= amount
      self.ledger.append({"amount": -amount, "description": description})
      return True

  def get_balance(self):
    return self.balance

  def transfer(self, amount, category):
    if self.check_funds(amount) == False:
      return False
    else:
      self.withdraw(amount, "Transfer to {}".format(category.category))
      category.deposit(amount, "Transfer from {}".format(self.category))
      return True

  def __repr__(self):
    output = self.category.center(30, '*')
    total = 0
    for tx in self.ledger:
      print(tx)
      total += tx['amount']
      output += '\n' + str(tx['description'][:23]).ljust(23, ' ') + "{:.2f}".format(tx['amount']).rjust(7, ' ')
    output += '\nTotal: ' + str(total)
    return output
 
def create_spend_chart(categories):
  final = list()
  cats = list()
  n = 100
  total = 0
  str = 'Percentage spent by category\n'
  
  for category in categories:
    
    wit = 0
    for tx in category.ledger:
      if tx['amount'] < 0:
        total += tx['amount']
        wit += tx['amount']
    cats.append(wit)
    
  for cat in cats:
    final.append(int(cat/total * 10) * 10)

  print(final)
  while n >= 0:
    str += "{}".format(n).rjust(3, ' ') + '|' + " "
    for per in final:
      if per == n:
        str += "o  "
        final[final.index(per)] -= 10
      else:
        str += "   "
    str += "\n"
    n -= 10

  str += '    -'
  for cat in categories:
    str += '---'
  str += '\n'

  catnames = list()
  for cat in categories:
    catnames.append(cat.category)

  long = 0
  for name in catnames:
    if len(name) > long:
      long = len(name)

  n = 0
  
  while n < long:
    str += "     "
    for name in catnames:
      if n < len(name):
        str += name[n] + "  "
      else:
        str += "   "
    if n < long - 1:
      str += "\n"
    n += 1

  return str