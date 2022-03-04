# FLiP-PY-FakeDataPulsar
Generate Fake Data


## Setup

pip3 install Faker

## Generate fake data utilizing Python Fake library

* https://github.com/joke2k/faker

````
from faker import Faker
from faker.providers import internet

fake = Faker()
fake.add_provider(internet)

print(fake.ipv4_private())

````


## References

* https://faker.readthedocs.io/en/stable/providers.html
