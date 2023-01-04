prod_conf_pass = {
    'host': 'localhost',
    'ssl_port': '9092',
    'security_protocol': 'SSL',
    'ssl_cafile': './src/certifications/ca.pem',
    'ssl_certfile': './src/certifications/service.cert',
    'ssl_keyfile': './src/certifications/service.key'
}

prod_conf_fail = {
    'host': 'wrong_host_name',
    'ssl_port': '9092',
    'security_protocol': 'SSL',
    'ssl_cafile': './src/certifications/ca.pem',
    'ssl_certfile': './src/certifications/service.cert',
    'ssl_keyfile': './src/certifications/service.key'
}

cons_conf_pass = {
    'topic_name': 'website_metrics',
    'host': 'localhost',
    'ssl_port': '9092',
    'consumer_timeout_ms': '10000',
    'client_id': 'CONSUMER_CLIENT_ID',
    'group_id': 'CONSUMER_GROUP_ID',
    'security_protocol': 'SSL',
    'ssl_cafile': './src/certifications/ca.pem',
    'ssl_certfile': './src/certifications/service.cert',
    'ssl_keyfile': './src/certifications/service.key',
    'auto_offset_reset': 'earliest'
}

cons_conf_fail = {
    'topic_name': 'website_metrics',
    'host': 'wrong_host_name',
    'ssl_port': '9092',
    'consumer_timeout_ms': '10000',
    'client_id': 'CONSUMER_CLIENT_ID',
    'group_id': 'CONSUMER_GROUP_ID',
    'security_protocol': 'SSL',
    'ssl_cafile': './src/certifications/ca.pem',
    'ssl_certfile': './src/certifications/service.cert',
    'ssl_keyfile': './src/certifications/service.key',
    'auto_offset_reset': 'earliest'
}

target_websites =  [
    'http://youtube.com',
    'http://google.com',
    'http://yahoo.fr'
]
