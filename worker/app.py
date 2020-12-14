import schedule
from resources.sqs_queue import receive_messages


def job():
    receive_messages()


schedule.every(10).seconds.do(job)

while True:
    schedule.run_pending()
