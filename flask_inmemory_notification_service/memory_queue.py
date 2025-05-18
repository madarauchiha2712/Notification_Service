import queue

# Create in-memory queues to simulate Kafka topics
notifications_queue = queue.Queue()  # Queue for notifications (email, sms, etc.)
failed_notifications_queue = queue.Queue()  # Queue for failed notifications

# In-memory database to store user notifications
user_notifications = {}
