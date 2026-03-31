import datetime

def get_days(date_str):
  """Calculates days between today and the deadline"""
  try:
    target=datetime.datetime.strptime(date_str,"%Y-%m-%d").date()
    today=datetime.date.today()
    days_left=(target-today).days
    return days_left
  except:
    return 999

def run_planner():
  tasks=[]
  print("My Study Planner")

  while True:
    todo=input("\nEnter Assignment/Subject Name (or 'done' to finish):")
    if todo.lower()=='done':
      break

    due_date=input("Whwn is it due? (YYYY-MM_DD):")
    days_left=get_days(due_date)

    tasks.append({
      "name":todo,
      "days":days_left, 
      "date":due_date
      })
    
  tasks.sort(key=lambda x: x['days'])

  print("\nTOP PRIORITIES:")
  if not tasks:
    print("No tasks added. Enjoy your free time!")
  else:
    for t in tasks:
        if t['days']<0:
          tag="!!! OVERDUE !!!"
        elif t['days']<=2:
          tag="DO THIS NOW"
        else:
          tag="Relax"
        print(f"-{t['name']} (Due:{t['date']})-{t['date']} days left[{tag}]")

run_planner()