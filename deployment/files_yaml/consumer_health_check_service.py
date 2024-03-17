#!/usr/bin/python3
#
#
#=== import ===
from kafka import KafkaConsumer
import json

#=== variables ===#
KAFKA_BOOTSTRAP_SERVERS = "localhost:9092"
HEALTH_CHECK_TOPIC = "health_checks_topic"

#=== function ===#
def get_latest_health_check():
  consumer = KafkaConsumer(HEALTH_CHECK_TOPIC, bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS, 
                           auto_offset_reset="earliest", consumer_timeout_ms=1000)
  for msg in consumer:
    return json.loads(msg.value.decode())
  return None

#=== start ===#
latest_check = get_latest_health_check()
if latest_check:
  print(f"Latest health check: {latest_check}")

#=== end ===#
