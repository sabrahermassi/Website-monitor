"""Module that reads websites check results from a kafka topic and saves them into a database."""
import json
import psycopg2
from kafka import KafkaConsumer
from kafka.errors import NoBrokersAvailable


def create_consumer(cons_conf):
    """Function Creating a Kafka consumer object with necessary configuration params."""
    try:
        consumer = KafkaConsumer(
            cons_conf['topic_name'],
            bootstrap_servers=f"{cons_conf['host']}:{cons_conf['ssl_port']}",
            consumer_timeout_ms=cons_conf['consumer_timeout_ms'],
            client_id=cons_conf['client_id'],
            group_id=cons_conf['group_id'],
            security_protocol=cons_conf['security_protocol'],
            ssl_cafile=cons_conf['ssl_cafile'],
            ssl_certfile=cons_conf['ssl_certfile'],
            ssl_keyfile=cons_conf['ssl_keyfile'],
            auto_offset_reset=cons_conf['auto_offset_reset'],
            value_deserializer=lambda v: json.loads(v.decode('utf-8')),
        )
        result = consumer
    except NoBrokersAvailable as error:
        print("KafkaConsumer creation error:", error)
        result = None
    return result


def database_writer(consumer, db_conf):
    """
    Function reading websites check results from a
    kafka topic and saving them into a postgres database.
    """
    try:
        # Connect to the postgreSQL database
        connection = psycopg2.connect(
            (f"{db_conf['database_type']}://{db_conf['user']}:"
             f"{db_conf['password']}@{db_conf['host']}:{db_conf['port']}/"
             f"{db_conf['database_name']}?{db_conf['sslmode']}")
        )

        # Create a cursor to perform database operations
        cursor = connection.cursor()

        # Executing a SQL query to select the database version and commit changes in the database
        query_sql = 'SELECT VERSION()'
        cursor.execute(query_sql)
        version = cursor.fetchone()[0]
        print(version)
        connection.commit()

        # SQL query to create a new table check_results_table
        create_table_query = """ CREATE TABLE IF NOT EXISTS check_results_table
                                (WEBSITE TEXT   NOT NULL,
                                RESPONSE_TIME       FLOAT,
                                STATUS_CODE     INT);
                            """
        cursor.execute(create_table_query)
        connection.commit()
        print("Table created successfully in PostgreSQL ")

        # Executing a SQL query to insert data into table
        for message in consumer:
            print ("%d:%d: v=%s" % (message.partition,
                                    message.offset,
                                    message.value))
            check_results = message.value
            website = check_results['website']
            response_time = check_results['response_time']
            status_code = check_results['status_code']

            insert_query = """ INSERT INTO check_results_table
                            (WEBSITE, RESPONSE_TIME, STATUS_CODE)
                            VALUES (%s,%s,%s)
                        """
            cursor.execute(insert_query, (website, response_time, status_code))
            connection.commit()
            print("website_check_results inserted successfully")

            cursor.execute("SELECT * from check_results_table")
            website_check_results = cursor.fetchall()
            print("website_check_results ", website_check_results)
        # Close the curson and the connection
        cursor.close()
        connection.close()

    except (psycopg2.InterfaceError,
            psycopg2.ProgrammingError,
            psycopg2.OperationalError
            ) as error:
        print("Error:", error)
