from flask import Flask, request, jsonify

from memory_queue import user_notifications
from services.notification_service import push_to_queue
import threading
from consumers.notification_consumer import consume_notifications

app = Flask(__name__)

def write_nitification_to_db(user_id, notification_type, message):
    if user_id not in user_notifications:
        user_notifications[user_id] = []

    user_notifications[user_id].append({
        "type": notification_type,
        "message": message
    })

@app.route('/notifications', methods=['POST'])
def send_notification():
    data = request.get_json()

    notification_type = data.get('type')
    user_id = data.get('user_id')
    message = data.get('message')

    # Print out the received request data for debugging
    print(f"Received notification request: {data}")

    if notification_type not in ['email', 'sms', 'in-app']:
        return jsonify({"error": "Invalid notification type"}), 400

    # Push the notification message to the in-memory queue
    push_to_queue(notification_type, user_id, message)
    write_nitification_to_db(user_id, notification_type, message)

    return jsonify({"status": "Notification sent to in-memory queue"}), 200

@app.route('/users/<int:user_id>/notifications', methods=['GET'])
def get_user_notifications(user_id):
    # Retrieve notifications for the specified user_id
    notifications = user_notifications.get(user_id, [])

    if not notifications:
        return jsonify({"message": "No notifications found for this user"}), 404

    return jsonify({"user_id": user_id, "notifications": notifications}), 200

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
