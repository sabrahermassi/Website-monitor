"""Module that tests website_checker and database_writer."""
import unittest
from src.website_monitor.website_checker import create_producer
from src.website_monitor.website_checker import check_websites
from src.website_monitor.database_writer import create_consumer
from helpers import *


class TestCreateProducer(unittest.TestCase):
    """
    Functions testing producer creation.
    """
    def test_create_producer_success(self):
        producer = create_producer(prod_conf_pass)
        self.assertIsNotNone(producer)

    def test_create_producer_failure(self):
        producer = create_producer(prod_conf_fail)
        self.assertIsNone(producer)


class TestCreateConsumer(unittest.TestCase):
    """
    Functions testing consumer creation.
    """
    def test_create_consumer_success(self):
        consumer = create_consumer(cons_conf_pass)
        self.assertIsNotNone(consumer)

    def test_create_consumer_failure(self):
        consumer = create_consumer(cons_conf_fail)
        self.assertIsNone(consumer)


class TestCheckWebsites(unittest.TestCase):
    """
    Function testing website_checker on target websites.
    """
    def test_websites_monitor_success(self):

        producer = create_producer(prod_conf_pass)
        self.assertIsNotNone(producer)

        consumer = create_consumer(cons_conf_pass)
        self.assertIsNotNone(consumer)

        check_websites(producer, target_websites, 'website_metrics')
        # TODO : continue implementing tests


if __name__ == '__main__':
    unittest.main()
