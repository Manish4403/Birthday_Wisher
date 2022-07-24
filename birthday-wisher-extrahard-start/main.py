##################### Extra Hard Starting Project ######################
import pandas
import smtplib
import datetime as dt
import random

letters = random.randint(1, 3)
my_email = "manishsutradhar66@gmail.com"
password = "eaxuxultrnisoscv"
# 1. Update the birthdays.csv
data = pandas.read_csv('birthdays.csv')
data_dict = data.to_dict()

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
today = now.day
this_month = now.month
for i in range(len(data_dict["day"])):
    if today == data_dict["day"][i] and this_month == data_dict["month"][i]:
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        with open(f"letter_templates/letter_{letters}.txt") as file:
            file_name = file.read()
            new_letter = file_name.replace("[NAME]", data_dict['name'][i])

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=data_dict['email'][i],
                                msg=f"Subject:Happy Birthday!\n\n{new_letter}")
