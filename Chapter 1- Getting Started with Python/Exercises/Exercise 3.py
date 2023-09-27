from datetime import datetime
# datetime object containing current date and time
now = datetime.now()

print ("now=", now)

# dd/mm/YY H:M:S
dt_string =now.strftime("%d/%m/%Y %H:%M:%S")
print ("Current date and time:", dt_string)