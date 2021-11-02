import smtplib
import pandas
import random
import datetime as dt

my_email = "testforcode12@gmail.com"
password = "testforcode12@#"
# Password for Yahoo: testingforcode12@
PLACEHOLDER = "[NAME]"

today = dt.datetime.now()
data = pandas.read_csv("birthdays.csv")
data = data.to_dict(orient='records')
for i in range(len(data)):
    if today.day == data[i]["day"] and today.month == data[i]["month"]:
        file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
        with open(file_path) as file:
            content = file.read()
            new_letter = content.replace(PLACEHOLDER, data[i]["name"])
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email, to_addrs=data[i]["email"],
                                    msg=f"Subject: Happy Birthday!\n\n {new_letter}")


# ------ ASSIGNMENT: SEND RANDOM QUOTES ON A MONDAY --------#

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="testforcode12@yahoo.com",
#                         msg="Subject: Testing\n\n Hey, how you doin'?")
#
# with open('quotes.txt') as lines_list:
#     lists = lines_list.readlines()
#     current = dt.datetime.now()
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         if current.day == 2:
#             connection.starttls()
#             connection.login(user=my_email, password=password)
#             connection.sendmail(from_addr=my_email, to_addrs="testforcode12@yahoo.com",
#                              msg=f"Subject: Quote of the Day!\n\n {random.choice(lists)}")

