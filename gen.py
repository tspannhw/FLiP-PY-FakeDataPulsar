from time import sleep
from math import isnan
import time
import sys
import datetime
import subprocess
import sys
import os
from subprocess import PIPE, Popen
import traceback
import math
import base64
import json
from time import gmtime, strftime
import random, string
import psutil
import base64
import uuid
import socket 
import time
import logging
import pulsar
from pulsar.schema import *
from faker import Faker
from faker.providers import internet, address, automotive, barcode, company, date_time, geo, job, misc, person
from faker.providers import phone_number, user_agent

fake = Faker()
fake.add_provider(internet)
fake.add_provider(address)
fake.add_provider(automotive)
fake.add_provider(barcode)
fake.add_provider(company)
fake.add_provider(date_time)
fake.add_provider(geo)
fake.add_provider(job)
fake.add_provider(misc)
fake.add_provider(person)
fake.add_provider(phone_number)
fake.add_provider(user_agent)

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
    email_me = Boolean()
    secret_code = String()
    password = String()
    first_name = String()
    last_name = String()
    phone_number = String()
    user_agent = String()


# Create New Topic
# bin/pulsar-admin topics delete persistent://public/default/fakeuser
# bin/pulsar-admin topics create persistent://public/default/fakeuser

# TODO:  create parameters for URL, Login, Topic, producer name, producer id, fields, options, schema - maybe class?, # of rows or continuous, max count

client = pulsar.Client('pulsar://pulsar1:6650')
producer = client.create_producer(topic='persistent://public/default/fakeuser' ,schema=JsonSchema(PulsarUser),properties={"producer-name": "fake-py-sensor","producer-id": "fake-user" })

MAX_COUNT = int(5000)
counter = int(0)

while (counter < MAX_COUNT):

    userRecord = PulsarUser()
    uuid_key = '{0}_{1}'.format(strftime("%Y%m%d%H%M%S",gmtime()),uuid.uuid4())
    userRecord.created_dt = fake.date() 
    userRecord.user_id = uuid_key
    userRecord.ipv4_public = fake.ipv4_public()
    userRecord.email = fake.ascii_email()
    userRecord.user_name = fake.user_name()
    userRecord.cluster_name = fake.slug()
    userRecord.city = fake.city() 
    userRecord.country = fake.country()
    userRecord.postcode = fake.postcode()
    userRecord.street_address = fake.street_address()
    userRecord.license_plate = fake.license_plate()
    userRecord.ean13 = fake.ean13()
    userRecord.response = fake.catch_phrase() 
    userRecord.comment = fake.bs() 
    userRecord.company = fake.company()
    userRecord.latitude = float(fake.latitude())
    userRecord.longitude = float(fake.longitude())
    userRecord.job = fake.job()
    userRecord.email_me = fake.boolean()
    userRecord.secret_code = fake.md5()
    userRecord.password = fake.password()
    userRecord.first_name = fake.first_name()
    userRecord.last_name = fake.last_name()
    userRecord.phone_number = fake.phone_number()
    userRecord.user_agent = fake.user_agent()
    print(userRecord)
    producer.send(userRecord,partition_key=str(uuid_key))
    counter += 1
