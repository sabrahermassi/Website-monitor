"""Module that always runs the website checker and saves the results into a postgres database."""
import time
from src.website_monitor.website_checker import create_producer
from src.website_monitor.website_checker import check_websites
from src.website_monitor.website_checker import read_configuration_from_file
from src.website_monitor.database_writer import create_consumer, database_writer


def main():
    """Main function."""
    # Load config params from yaml config file for KafkaProducer,
    # KafkaConsumer, the database and the list of websites
    producer_config, consumer_config, database_config, target_websites = (
        read_configuration_from_file()
    )

    # Create a KafkaProducer and a KafkaConsumer
    while True:
        producer = create_producer(producer_config)
        if producer is not None:
            break
        time.sleep(2)
    while True:
        consumer = create_consumer(consumer_config)
        if consumer is not None:
            break
        time.sleep(2)

    # Always run the websites checker then write websites check results into a database
    while True:
        check_websites(producer, target_websites, producer_config['topic_name'])
        database_writer(consumer, database_config)


if __name__ == "__main__":
    main()
