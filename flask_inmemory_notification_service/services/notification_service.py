from memory_queue import notifications_queue

def push_to_queue(notification_type, user_id, message):
    notification_message = {
        "type": notification_type,
        "user_id": user_id,
        "message": message
    }

    notifications_queue.put(notification_message)
    print(f"Notification message pushed to in-memory queue for {notification_type}: {message}")
