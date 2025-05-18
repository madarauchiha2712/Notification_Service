import time
from memory_queue import notifications_queue, failed_notifications_queue
from services.notification_service import push_to_queue


def send_email(user_id, message):
    try:
        print(f"Sending email to user {user_id}: {message}")
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

def send_sms(user_id, message):
    try:
        print(f"Sending SMS to user {user_id}: {message}")
        return True
    except Exception as e:
        print(f"Error sending SMS: {e}")
        return False

def process_notification(data):
    notification_type = data.get('type')
    user_id = data.get('user_id')
    message = data.get('message')

    if notification_type == 'email':
        if not send_email(user_id, message):
            failed_notifications_queue.put(data)
    elif notification_type == 'sms':
        if not send_sms(user_id, message):
            failed_notifications_queue.put(data)
    elif notification_type == 'in-app':
        print(f"Sending in-app notification to user {user_id}: {message}")
    else:
        print("Unknown notification type")

# Mimicking behaviour of kafka publisher
def populate_queue():
    push_to_queue("sms", "Aradhya", "Welcome to pepSales")
    push_to_queue("email", "Aradhya", "PepSales monthly report")

def consume_notifications():
    populate_queue()

    while True:
        if not notifications_queue.empty():
            data = notifications_queue.get()
            process_notification(data)
        time.sleep(1)  # To prevent the thread from hogging CPU


if __name__ == "__main__":
    consume_notifications()