import time

from consumers.notification_consumer import populate_queue
from memory_queue import failed_notifications_queue

def retry_failed_notification(message):
    print(f"Retrying failed notification: {message}")

def populate_queue():
    failed_notifications_queue.put({
        "type": "sms",
        "user_id": "Aradhya",
        "message": "Your otp is 4321"
    })
    failed_notifications_queue.put({
        "type": "email",
        "user_id": "Aradhya",
        "message": "Welcome to pepSales"
    })

def consume_failed_notifications():
    populate_queue()
    while True:
        if not failed_notifications_queue.empty():
            data = failed_notifications_queue.get()
            retry_failed_notification(data)
        time.sleep(1)

if __name__ == "__main__":
    consume_failed_notifications()
