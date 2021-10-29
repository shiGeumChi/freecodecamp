class Category:
  def __init__(self, name):
        self.total = 0
        self.name = name
        self.ledger = []
        self.withtotal = 0

  def __repr__(self):

    s = f"{self.name:*^30}\n"

    for item in self.ledger:
      amount_str = f"{item['amount']:.2f}"
      s+= f"{item['description'][0:29-len(amount_str)]}"
      s+= " "* ( 29-len(amount_str)  - len(item['description'])) + " "
      s+= amount_str + "\n"
    s+= f"Total: {self.total:.2f}"

    return s

  def deposit(self,amount,description=""):
    self.ledger.append({"amount": amount, "description": description})
    self.total += amount

  def withdraw(self,amount, description=""):
    if(self.check_funds(amount) == True):
      self.ledger.append({"amount": -amount, "description": description})
      self.total -= amount
      self.withtotal += amount
      return True
    return False
    
  def get_balance(self):
    return self.total

  def transfer(self,amount,instance):
    if(self.check_funds(amount) == True):
      self.withdraw(amount, f"Transfer to {instance.name}")
      instance.deposit(amount, f"Transfer from {self.name}")
      return True
    return False

  def check_funds(self,amount):
    if (amount > self.total):
      return False
    return True



def create_spend_chart(categories):
  
  res =""
  # print("Percentage spent by category")
  res += "Percentage spent by category\n"
  total =0
  maxlen = 0
  for item in categories:
    total += item.withtotal
    if( len(item.name) >= maxlen ):
      maxlen = len(item.name) 

  avgs =[]
  for item in categories:
    avgs.append(float(item.withtotal)/total*100)

  
  percent = 100
  for i in range(0,11) :
    s = f'{percent:>3}|'
    for avg in avgs:
      if(avg >= percent):
        s += " o "
      else:
        s += "   "
    # print(s)
    res += s + '\n'
    percent -= 10

  # print("    " + "-"*(len(avgs)*3+1))
  res += "    " + "-"*(len(avgs)*3+1) + '\n'

  for i in range(0,maxlen):
    x = "    "
    for item in categories:
      if( i == 0 ):
        x += f" {item.name[i].upper()} "
      else:
        if(i >= len(item.name)):
          x += "   "
        else:
          x += f" {item.name[i]} "
    
    # print(x)
    if(i==maxlen-1):
      res+=x
    else:
      res+= x + '\n'

  print(res)
  return res

# food = Category("food")
# food.deposit(1000)
# food.withdraw(100)
# food.withdraw(100)
# food.withdraw(100)
# food.withdraw(100)


# enter = Category("entertainment")
# enter.deposit(1000)
# enter.withdraw(100)
# enter.withdraw(100)
# enter.withdraw(100)
# create_spend_chart([food,enter])

