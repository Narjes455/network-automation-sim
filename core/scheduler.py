import schedule
import time

def run_scheduler(task_function):

    schedule.every(1).minutes.do(task_function)

    print("⏰ Scheduler started...")
    print("Waiting for scheduled jobs...")

    while True:
        schedule.run_pending()
        time.sleep(1)