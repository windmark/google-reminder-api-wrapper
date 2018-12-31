from reminder_api import ReminderApi

api = ReminderApi()
reminders = api.list()
print(reminders)


new_reminder = api.create('Test reminder', '2019-01-10 15:00')
reminders = api.list()
print(reminders)


api.delete(new_reminder)
reminders = api.list()
print(reminders)