import json
from typing import Any, Dict
from kafka import KafkaProducer
from app.core.config import settings
from app.core.constants import RiskIndicator, get_kafka_topic

class KafkaService:
    def __init__(self):
        self.producer = KafkaProducer(
            bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
            value_serializer=lambda v: json.dumps(v).encode('utf-8'),
            key_serializer=lambda v: v.encode('utf-8')
        )

    def send_indicator_data(self, indicator: RiskIndicator, data: Dict[str, Any]):
        """Send indicator data to appropriate Kafka topic"""
        topic = get_kafka_topic(indicator)
        
        # Create message with metadata
        message = {
            "indicator": indicator,
            "country_code": settings.COUNTRY_CODE,
            "data": data,
            "source": "worldbank-api"
        }
        
        # Use indicator as key for message partitioning
        future = self.producer.send(
            topic=topic,
            key=indicator,
            value=message
        )
        
        # Wait for message to be sent
        try:
            future.get(timeout=10)
        except Exception as e:
            print(f"Error sending message to Kafka: {str(e)}")
            raise

    def close(self):
        """Close Kafka producer connection"""
        if self.producer:
            self.producer.close()

# Create singleton instance
kafka_service = KafkaService()
