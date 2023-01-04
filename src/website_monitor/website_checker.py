"""Module periodically checks websites availability and sends check results to a kafka producer."""
import time
import json
import requests
import yaml
from kafka import KafkaProducer
from kafka.errors import KafkaError, KafkaTimeoutError, KafkaConnectionError, NoBrokersAvailable


def read_configuration_from_file():
    """Function Reading the YAML file configuration."""
    with open('./config.yml', encoding="utf-8") as file:
        config = yaml.safe_load(file)
        producer_config = config['producer_config']
        consumer_config = config['consumer_config']
        database_config = config['database_config']
        target_websites = config['target_websites']
        print("Configuration Successfully loaded")
        file.close()

        return producer_config, consumer_config, database_config, target_websites


def create_producer(prod_conf):
    """Function Creating a Kafka producer object with necessary configuration params."""
    try:
        producer = KafkaProducer(
        bootstrap_servers=f"{prod_conf['host']}:{prod_conf['ssl_port']}",
        security_protocol=prod_conf['security_protocol'],
        ssl_cafile=prod_conf['ssl_cafile'],
        ssl_certfile=prod_conf['ssl_certfile'],
        ssl_keyfile=prod_conf['ssl_keyfile'],
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        result = producer
    except NoBrokersAvailable as error:
        print("KafkaProducer creation error:", error)
        result = None
    return result


def check_websites(producer, websites, topic_name):
    """
    Function checking websites availabilty
    and sending check results to a kafka producer.
    """
    for website in websites:
        print(website)
        try:
            # Make HTTP request to the website and get response_time in milliseconds and status_code
            response = requests.get(website, timeout=5)
            status_code = response.status_code
            response_time = round((response.elapsed.total_seconds() * 1000.0), 3)
            print(status_code)
            print(response_time)

            # Send the website check results to a Kafka topic called 'website_metrics'
            data_dict = {
                    'website': website,
                    'response_time': response_time,
                    'status_code': status_code,
            }
            producer.send(topic_name, data_dict)
            print(f"Data sent: {data_dict}")
            time.sleep(1)

        except (requests.exceptions.RequestException,
                NoBrokersAvailable,
                KafkaTimeoutError,
                KafkaConnectionError,
                KafkaError) as error:
            print("Error:", error)
