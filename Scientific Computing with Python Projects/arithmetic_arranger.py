def arithmetic_arranger(problems,val=False):
  line1 = ""
  line2 = ""
  line3 = ""
  line4 = ""

  if len(problems) > 5:
    return "Error: Too many problems."

  for problem in problems:
    x = problem.split()

    a = x[0]
    operand = x[1]
    b = x[2]

    if (operand != "+" and operand != "-"):
      return "Error: Operator must be '+' or '-'."

    if not a.isnumeric() or not b.isnumeric():
      return "Error: Numbers must only contain digits."

    if (len(a) > 4 or len(b) >4):
      return "Error: Numbers cannot be more than four digits."

    if(operand =="+"):
      c = int(a) + int(b)
    else:
      c = int(a)-int(b)

    c = str(c)

    maxlen = max(len(a),len(b))

    first = "  " + " "*(maxlen-len(a)) + a
    second = operand + " " + " "*(maxlen-len(b)) + b
    forth = " " * (maxlen+2-len(c)) + c


    third = (maxlen+2) * "-"

    line1 += first + "    "
    line2 += second + "    "
    line3 += third + "    "
    line4 += forth + "    "


  line1 = line1.rstrip()
  line2 = line2.rstrip()
  line3 = line3.rstrip()
  line4 = line4.rstrip()

  if(val==True):
    arranged_problems = line1 + '\n' + line2 + '\n' + line3 + '\n' + line4
    print(arranged_problems)
  else:
    arranged_problems = line1 + '\n' + line2 + '\n' + line3
    print(arranged_problems)

  

  return arranged_problems