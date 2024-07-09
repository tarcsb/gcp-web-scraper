from google.cloud import pubsub_v1
import logging

logger = logging.getLogger("gcp_web_scraper")

def publish_message(topic_name, message):
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(os.getenv('GCP_PROJECT_ID'), topic_name)
    future = publisher.publish(topic_path, message.encode("utf-8"))
    future.result()
    logger.info(f"Message published to {topic_name}")
