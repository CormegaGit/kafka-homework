#!/usr/bin/python3
#
#
#=== import ===
from datetime import datetime
from kafka import KafkaProducer

#=== variables ===#
KAFKA_BOOTSTRAP_SERVERS = "localhost:9092"
HEALTH_CHECK_TOPIC = "health_checks_topic"

#=== function ===#
def send_health_check(service_name, status):
  producer = KafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS)
  data = {
    "service_name": service_name,
    "status": status,
    "timestamp": datetime.utcnow().isoformat()
  }
  producer.send(HEALTH_CHECK_TOPIC, json.dumps(data).encode())
  producer.flush()

#=== start ===#
send_health_check("kafka", "OK")

#=== end ===#

