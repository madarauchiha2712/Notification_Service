# In-Memory Kafka Notification Service

## Description:
This service handles sending notifications to users via Email, SMS, or In-App using in-memory queues. It maintains a pub/sub design using Python's queue.Queue. Failed notifications are retried using a separate consumer.

### **Demo Assumptions and Shortcuts**

For the purpose of this demo, the following shortcuts have been implemented:

1. **In-Memory Notification Storage**:

   * Instead of using a real database, an in-memory dictionary is used to store notifications. All notifications are read from and written to this dictionary.

2. **In-Memory Queue Simulation**:

   * An in-memory queue is used to simulate the behavior of **Kafka** or **RabbitMQ**. All messages are pushed to or consumed from this queue.

3. **Dummy Consumers**:

   * Two consumer processes are created to simulate message consumption. Upon starting, these consumers push dummy messages to the queue, demonstrating the consumption flow.

4. **No Actual Email or SMS Integration**:

   * While the application simulates the sending of emails and SMS, no real connections are made to email or SMS servers. Instead, **print statements** are used to indicate that a message is being sent.

5. **Notification Storage Behavior**:

   * Ideally, notifications should only be written to the database after they have been successfully delivered to the user by the consumer. However, to keep the **GET endpoint lightweight** (i.e., not implement a capability to write from one process(consumers) and read from another process(main function where producer is running)), the notification is written to the in-memory "database" (queue) as soon as the message is pushed, not after successful delivery.

## Setup Instructions:
1. Set up the env:
   ```bash
   cd in-memory-notification-service
   python3 -m venv .venv
   source ./.venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   # Needed only during the fist time and when a new package is added as the virtual env present in repo already has all dependencies installed.
   ```

3. Start Flask application:
   ```bash
   python app.py
   ```

4. Start consumers:
   - Notification consumer:
     ```bash
     python consumers/notification_consumer.py
     ```
   - Failed notification retry consumer:
     ```bash
     python consumers/failed_notifications_consumer.py
     ```
   