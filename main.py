import smtplib
import datetime as dt
import random

now = dt.datetime.now()
week_day = now.weekday()
with open("quotes.txt", "r") as file:
    quotes = file.readlines()
    random_quote = random.choice(quotes)
    # print(random_quote)
    # print(random_quote.strip())
    # new_list = [i.strip() for i in quotes]
    # print(new_list)


my_email = "manishsut50@outlook.com"
password = "Abcd54321"
if week_day == 2:
    with smtplib.SMTP("smtp-mail.outlook.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="manishsutradhar@yahoo.com",
                            msg=f"Subject:Motivation\n\n{random_quote}")
# import datetime as dt
#
# now = dt.datetime.now()
# dob=dt.datetime(year=1998, month=4, day=8, hour=5)
# week_day = now.weekday()
# print(week_day)
# print(dob)