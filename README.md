# FLiP-PY-FakeDataPulsar
Generate Fake Data


## Setup

pip3 install Faker

## Generate fake data utilizing Python Fake library

* https://github.com/joke2k/faker

## Schema

````

# Pulsar Message Schema
class PulsarUser (Record):
    created_dt = String()
    user_id = String()
    ipv4_public = String()
    email = String()
    user_name = String()
    cluster_name = String()
    city = String()
    country = String()
    postcode = String()
    street_address = String()
    license_plate = String()
    ean13 = String()
    response  = String()
    comment   = String()
    company = String()
    latitude = Float()
    longitude = Float()
    job = String()
    email_me = String()
    secret_code = String()
    password = String()
    first_name = String()
    last_name = String()
    phone_number = String()
    user_agent = String()

````

## Example JSON Record

````
{'_required_default': False, '_default': None, '_required': False, 'created_dt': '1975-04-17', 'user_id': '20220304192446_cf77fa3c-ac2d-46c1-8be4-d24933011779', 'ipv4_public': '16.39.132.11', 'email': 'tarabaker@thompson.com', 'user_name': 'billycrawford', 'cluster_name': 'half-leader-better', 'city': 'Simmonsburgh', 'country': 'Mali', 'postcode': '37010', 'street_address': '98777 Robert Dale Suite 885', 'license_plate': '7X 10043', 'ean13': '2203406035944', 'response': 'Object-based demand-driven model', 'comment': 'exploit synergistic functionalities', 'company': 'Mcdonald LLC', 'latitude': 56.688108, 'longitude': 118.429998, 'job': 'Psychotherapist', 'email_me': None, 'secret_code': '92778885568782e8b9b26a64dec0aaba', 'password': '##7cb2Tz)M', 'first_name': 'Michael', 'last_name': 'Richardson', 'phone_number': '041-420-1733', 'user_agent': 'Mozilla/5.0 (Windows; U; Windows 98) AppleWebKit/534.16.7 (KHTML, like Gecko) Version/5.0 Safari/534.16.7'}
{'_required_default': False, '_default': None, '_required': False, 'created_dt': '1974-01-07', 'user_id': '20220304192446_045a2724-6f9e-4968-ae19-a5a1a095e57b', 'ipv4_public': '207.116.194.88', 'email': 'hsanchez@chandler.com', 'user_name': 'qpearson', 'cluster_name': 'memory-story-see', 'city': 'Elizabethview', 'country': 'Mauritius', 'postcode': '01045', 'street_address': '352 Rodriguez Rue', 'license_plate': '6-79707I', 'ean13': '3151191404713', 'response': 'Quality-focused logistical conglomeration', 'comment': 'implement value-added relationships', 'company': 'Harper LLC', 'latitude': 88.5392145, 'longitude': -7.466258, 'job': 'Development worker, community', 'email_me': None, 'secret_code': '28b5519f4bb38cd9fc52aa9bb7bca1aa', 'password': '+5u&%TTkHt', 'first_name': 'Johnny', 'last_name': 'Hoffman', 'phone_number': '9669534677', 'user_agent': 'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.2; Trident/3.1)'}
````

## TODO

create parameters for URL, Login, Topic, producer name, producer id, fields, options, schema - maybe class?, # of rows or continuous

## References

* https://faker.readthedocs.io/en/stable/providers.html
* https://faker.readthedocs.io/en/master/
