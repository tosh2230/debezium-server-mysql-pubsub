import json
import os

from google.cloud import pubsub_v1

project_id = os.environ.get("GOOGLE_CLOUD_PROJECT")
subscription_id = os.environ.get("PUBSUB_SUBSCRIPTION_ID")
NUM_MESSAGES = 1

subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(project_id, subscription_id)

with subscriber:
    response = subscriber.pull(
        request={"subscription": subscription_path, "max_messages": NUM_MESSAGES},
    )

    if len(response.received_messages) == 0:
        exit

    ack_ids = []
    for received_message in response.received_messages:
        message = json.loads(received_message.message.data.decode("UTF-8"))
        print(json.dumps(message))
    #     ack_ids.append(received_message.ack_id)

    # subscriber.acknowledge(
    #     request={"subscription": subscription_path, "ack_ids": ack_ids}
    # )

    # print(
    #     f"Received and acknowledged {len(response.received_messages)} messages from {subscription_path}."
    # )
