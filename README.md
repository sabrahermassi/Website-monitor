# Website-monitor
Website Availability Checker is a robust Python tool designed to monitor the availability of websites and store the results in a PostgreSQL database. This project ensures continuous monitoring of website statuses, providing insights into their uptime and downtime periods.


Prerequisites
-------------

- Python 3
- PostgreSQL
- Apache Kafka


Installation
------------

1. Clone the repository:


2. Install the dependencies:
pip install -r requirements.txt


Configuration
-------------

Website-monitor can be configured using the config.yaml file in the root directory. The following params are available:

KafkaProducer configurations:
- `topic_name`: The name of the Kafka topic to publish check results to
- `host`: The hostname of the KafkaProducer
- `ssl_port`: The port number of the KafkaProducer
- `security_protocol`: The security protocol to use when connecting to the KafkaProducer
- `ssl_cafile`: The path to the CA certificate
- `ssl_certfile`: The path to the CERT certificate
- `ssl_keyfile`: The path to the KEY certificate

KafkaCondumer configurations:
- `topic_name`: The name of the Kafka topic the check results will be read from
- `host`: The hostname of the KafkaConsumer
- `ssl_port`: The port number of the KafkaConsumer
- `consumer_timeout_ms`: The time the consumer should wait for new messages to arrive before it returns control to the caller
- `client_id`: The consumer client ID
- `group_id`: The consumer group ID
- `security_protocol`: The security protocol to use when connecting to the KafkaConsumer
- `ssl_cafile`: The path to the CA certificate (same as the KafkaProducer)
- `ssl_certfile`: The path to the CERT certificate (same as the KafkaProducer)
- `ssl_keyfile`: The path to the KEY certificate (same as the KafkaProducer)
- `auto_offset_reset`: The consumer automatically resets the offset to the earliest available offset if it is unable to find the current offset

Database configurations:
- `database_type`: In this case it is postgres
- `user`: The username to connect to the PostgreSQL server
- `password`: The password to connect to the PostgreSQL server
- `host`: The hostname of the PostgreSQL server
- `port`: The port of the PostgreSQL server
- `database_name`: The name of the PostgreSQL database to connect to
- `sslmode`: The SSL mode to use when connecting to the PostgreSQL server

List of websites to check
- `target_websites`: The list of websites that the website_monitor should check their availability


Usage
-----

To start Website-checker-Database-writer, run the following command from the root directory "Website-checker-Database-writer":
python .\main.py

Website-checker-Database-writer will start checking websites and publishing check results to the Kafka topic specified in the configuration.
