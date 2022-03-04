# FLiP-PY-FakeDataPulsar
Generate Fake Data


## Setup

pip3 install Faker

## Generate fake data utilizing Python Fake library

* https://github.com/joke2k/faker

## Build a Topic

````
bin/pulsar-admin topics delete persistent://public/default/fakeuser

bin/pulsar-admin topics create persistent://public/default/fakeuser
````

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
    email_me = Boolean()
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

## Testing

````
bin/pulsar-admin schemas get persistent://public/default/fakeuser

bin/pulsar-client consume "persistent://public/default/fakeuser" -s fakeuser-consumer -n 0

----- got message -----
key:[20220304193720_c66b0c26-3bb5-4183-8c32-ee3fe78cce7c], properties:[], content:{
 "created_dt": "2004-11-27",
 "user_id": "20220304193720_c66b0c26-3bb5-4183-8c32-ee3fe78cce7c",
 "ipv4_public": "194.151.189.253",
 "email": "marywood@davis.info",
 "user_name": "santiagogregory",
 "cluster_name": "history-threat",
 "city": "Birdmouth",
 "country": "Norway",
 "postcode": "91306",
 "street_address": "6971 Dana Wall Apt. 594",
 "license_plate": "83M\u2022390",
 "ean13": "8230532486542",
 "response": "Configurable modular parallelism",
 "comment": "reinvent one-to-one eyeballs",
 "company": "Cantrell, Ochoa and Willis",
 "latitude": 14.1899475,
 "longitude": -162.604588,
 "job": "Ambulance person",
 "email_me": false,
 "secret_code": "f048d2d55b7be1689f9c9846e31ba9de",
 "password": "+8WWoLcV4t",
 "first_name": "Jennifer",
 "last_name": "Diaz",
 "phone_number": "001-797-009-5002x04500",
 "user_agent": "Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 5.01; Trident/3.0)"
}

````

## Validate with Trino/Presto SQL/Pulsar SQL

````
select * from pulsar."public/default"."fakeuser";
````

## Example Pulsar SQL Run

````
resto> select * from pulsar."public/default"."fakeuser";
 created_dt |                       user_id                       |   ipv4_public   |                  email                   |       user_name       |    cluster_name     |           city           |                    
------------+-----------------------------------------------------+-----------------+------------------------------------------+-----------------------+---------------------+--------------------------+--------------------
 2007-04-10 | 20220304193708_1cd7012e-c0ee-4911-b511-ace7e190e1b2 | 201.35.109.250  | bennettnicole@rivera.com                 | thomasbrown           | mean-major          | Jonesville               | Saint Pierre and Mi
 1975-11-22 | 20220304193708_c840eaa2-faab-4be7-91a0-e81d38a058b3 | 215.130.224.134 | rfoster@gmail.com                        | rallen                | every-five-leader   | East Lawrenceshire       | Sierra Leone       
 2005-10-17 | 20220304193708_b8ba6454-3be9-41f0-8345-5d0cac9f95a6 | 205.42.194.21   | michellesmith@gmail.com                  | ashley71              | traditional-able    | Floresville              | Faroe Islands      
 2018-05-04 | 20220304193708_53a7a714-f9e4-4bee-9dd3-100c37a15a1f | 39.236.134.6    | david22@gmail.com                        | wilsonkevin           | action-similar-fact | Palmerside               | Hungary            
 1971-12-26 | 20220304193708_7b410fec-9e54-46e0-8ca7-7585f2d1f9bf | 37.64.27.159    | perkinsnicole@edwards.net                | danieledwards         | local-identify      | West Deborah             | Ethiopia           
 1992-06-04 | 20220304193708_3f38dfb0-f445-4044-9e2d-c654390fedec | 193.105.205.92  | edwardgillespie@valdez.com               | michael98             | great-agree         | Port Danielle            | Netherlands Antille
 1987-05-06 | 20220304193708_f65f2f50-ae1f-49b6-9ba1-391a31a5ba62 | 163.48.165.226  | lauren83@hotmail.com                     | juliafoster           | heart-describe-onto | East Susanside           | Kiribati           
 2009-07-18 | 20220304193708_c58d67d4-cf48-42b8-aae1-e0b8a24e9fbe | 199.56.240.50   | fbrown@gmail.com                         | jamesblankenship      | south-must-language | Zacharymouth             | Brunei Darussalam  
 2012-01-24 | 20220304193708_b9501e5c-003b-48aa-9ca8-35f98121f9a8 | 19.140.90.84    | markdavies@gmail.com                     | ibrown                | can-example-subject | East Jacob               | Germany            
 2004-10-17 | 20220304193708_c24549a5-71bf-478c-965c-14c009b4ee7a | 60.226.144.142  | darlene58@hotmail.com                    | brownmelissa          | speech-report-light | South Brenda             | Tajikistan         
 1990-08-23 | 20220304193708_2bb30889-12ff-4700-b568-32ada4166068 | 110.237.54.65   | qlester@powell.com                       | katiegarcia           | voice-account-mrs   | East Marioshire          | Taiwan             
 1991-03-11 | 20220304193708_8cfcf3d0-b176-464f-8c4d-19aecbe2da2e | 71.136.161.117  | mooneyernest@stewart.com                 | cgreen                | human-crime         | Stephenhaven             | French Southern Ter
 1987-09-13 | 20220304193708_7c7b2a3b-da74-40ed-9fd0-09a7d67a1587 | 69.41.44.240    | christina45@gmail.com                    | darrellwhite          | including-play      | West Rickyshire          | Montenegro         
 1991-11-23 | 20220304193708_1c3d7978-03d4-4b9c-88fb-ff2fe75345c1 | 157.236.159.234 | jamesestrada@gmail.com                   | cynthiasmith          | would-pretty-add    | Alexandramouth           | Montenegro         
 1982-04-16 | 20220304193708_11e37713-057c-4d70-b3f6-fbe01e57ae58 | 140.217.89.170  | wballard@gmail.com                       | hdavis                | information-policy  | Hicksfort                | Senegal            
 1999-02-08 | 20220304193708_5074a732-05a9-46b5-a37d-9c20de2a0ae0 | 137.2.171.31    | stephen02@molina.info                    | edwingriffin          | old-author-ability  | North Seanshire          | Jordan             
 1990-03-01 | 20220304193708_7ecd6eb9-8f87-4fa4-a38d-7d56df917709 | 60.4.236.185    | nchristensen@hotmail.com                 | wandacarson           | could-alone-green   | East Veronicamouth       | Mozambique         
 1981-04-06 | 20220304193708_58770f4f-f934-4d9f-b0df-36da7a1d7865 | 8.3.253.29      | jeffreylee@hotmail.com                   | karenstanley          | pull-matter-bill-us | Richardton               | Papua New Guinea   
 1998-07-06 | 20220304193708_bd3f5159-b000-4e37-9787-82daa4de4338 | 187.46.71.75    | jesusmartin@johnson-jensen.com           | zharrison             | anything-term       | South Olivialand         | China              
 1991-07-09 | 20220304193708_e257cef2-2b04-4b31-8f5c-e73028fbf3d8 | 214.97.18.168   | chasemartin@holmes.info                  | xcannon               | space-him-fire-her  | Kimberlybury             | Guam               
 1984-08-03 | 20220304193708_9064c299-c580-4c62-9b04-b49acf18f184 | 215.41.52.206   | jasminealvarez@adams.info                | griffithscott         | only-east-price     | South Markstad           | Malta              
 2005-01-18 | 20220304193708_c7c49007-a5b7-41ce-a9b4-116631a43b78 | 98.121.141.5    | josephgonzalez@dillon.com                | fowlerdenise          | room-consumer-tell  | East Caitlyn             | Congo              
 1999-07-16 | 20220304193708_285d041b-c24f-4ec6-aed2-844826d89ae6 | 172.3.66.176    | seth28@burke.biz                         | amendez               | about-eye-gun       | Lisamouth                | Belgium            
 2018-06-30 | 20220304193708_58e4593f-e929-4d10-880e-97e6a1eec6f0 | 3.17.22.107     | lisabeck@yahoo.com                       | cervantesbarbara      | cut-mouth-outside   | South Stephentown        | Congo              
 1982-11-21 | 20220304193708_bc3fcbbb-67ef-4c3d-aa90-7ddefb210163 | 217.62.63.208   | amandaodom@macdonald.info                | laurie77              | money-raise-tell    | New Ruben                | Maldives           
 1970-08-14 | 20220304193708_cd1586dc-efbd-4594-bfee-ec7533d76235 | 205.82.255.209  | patrick75@gmail.com                      | christiewilliams      | evidence-area-all   | New Johnton              | Mayotte            
 1971-11-21 | 20220304193708_24284192-912e-4d51-b8a2-7e574a2c6011 | 19.152.140.203  | ocollins@wilson-perez.net                | martinezdanielle      | tree-major-personal | New Michael              | French Polynesia   
 1977-07-03 | 20220304193708_3fc04a3f-916d-4192-964d-73768aee571c | 161.44.9.32     | karina58@patrick-johnson.com             | jwillis               | arrive-ever-instead | Ortizshire               | Saint Vincent and t
 1984-07-07 | 20220304193708_a3d0c8e3-5363-4798-b473-f20a26da1769 | 148.182.134.243 | harrisjames@hotmail.com                  | acowan                | shoulder-fall-bar   | Milesshire               | Faroe Islands      
 1986-07-01 | 20220304193708_9ddb9223-fb15-4622-9fb5-7dcff5d62fe2 | 199.42.193.185  | reginald07@yahoo.com                     | bakerjohn             | usually-suggest     | Port Sylviamouth         | Greece             
 1980-09-17 | 20220304193708_876d48ed-7f8c-455b-a48e-6e08686cb7d4 | 220.0.184.116   | katherinehodge@yahoo.com                 | hparker               | argue-ready-paper   | Lake David               | Bahamas            
 2005-06-01 | 20220304193709_abb45275-c506-4242-aac0-e0dd31b17f45 | 102.252.7.70    | johnsonrobert@wilson.com                 | vpatel                | three-the-heavy     | South Jennifershire      | Antarctica (the ter
 2010-06-14 | 20220304193709_1e8344f5-b178-4020-8550-4e37a98ef7af | 45.94.232.107   | boyerjared@hotmail.com                   | johnsonallison        | possible-church     | Port Stephanie           | Tonga              
 1991-01-09 | 20220304193709_75dc6625-1413-45d6-b251-18f3b427fff6 | 129.241.214.7   | carrollallison@hotmail.com               | morganrichard         | available-week      | South Steven             | British Indian Ocea
 1979-10-08 | 20220304193709_9d78191c-c382-4891-add4-55a203a1d39d | 165.143.78.56   | kyleweaver@robbins.info                  | danielskelly          | page-culture-deep   | Lake Kelsey              | Lesotho            
 1981-09-11 | 20220304193709_9bb3a446-81a8-45b7-b580-4ed96cd9d0bd | 140.129.48.223  | danielbennett@hotmail.com                | miguel28              | go-all-catch        | Port Laura               | Mayotte            
 2008-08-29 | 20220304193709_a3973c55-3c7c-4624-af67-492b8b9de760 | 222.14.203.52   | rodgersrandall@hotmail.com               | bradleyjennifer       | need-while          | Amandaton                | Barbados           
 1986-08-28 | 20220304193709_1f0fca4e-2675-4092-a8c7-3488be8a8573 | 157.122.212.132 | emily97@hotmail.com                      | amberbarber           | enough-inside       | Andersonburgh            | Armenia            
 2000-03-07 | 20220304193709_542377ed-7653-47b5-a433-c6155fa4f3b2 | 11.232.64.92    | milleralexander@gmail.com                | manndonald            | condition-however   | Susanbury                | Belize             
 2006-12-11 | 20220304193709_3840bb14-6994-4f33-9d25-6f7354024038 | 188.19.33.204   | cathygardner@brown-martin.com            | tammyharris           | could-onto-push-see | West Mistymouth          | Romania            
 1979-05-26 | 20220304193709_c4a1674a-f183-41c9-8953-6681c704458b | 192.134.220.140 | amanda95@gill.info                       | kristennolan          | market-interesting  | Barnesbury               | Central African Rep
 2001-10-28 | 20220304193709_f9d1f6c6-bdf8-4ea6-bd18-6f6a4996399f | 5.246.85.209    | christopher79@hotmail.com                | bhale                 | heart-road-prepare  | North Johnland           | Uruguay            
 2014-01-19 | 20220304193709_a6dd0223-cea3-4e43-8919-505594050f69 | 41.168.248.81   | ltaylor@yahoo.com                        | tpatel                | myself-price-result | South Matthew            | Guernsey           
 2013-11-12 | 20220304193709_d6e8926b-7598-4a2f-94b2-54d76be0d74a | 67.80.32.202    | twhite@walters.com                       | markmorris            | rather-indicate     | East Morganmouth         | Lao People's Democr
 2021-04-16 | 20220304193709_3fd27b39-b169-4d6a-9af7-1f7ac6b11bd2 | 115.90.230.144  | sarah05@johnson-rogers.net               | fosterbrittany        | billion-modern-now  | Shelbyview               | Greece             
 1989-09-04 | 20220304193709_6f625e50-a215-4101-93fa-a4b1132332e9 | 216.25.22.75    | wwood@wilson.org                         | crystalmiller         | create-feel         | Ericmouth                | Madagascar         
 1970-07-10 | 20220304193709_c8a798af-2c4c-4155-a260-74bd64826e61 | 203.126.95.18   | matthew29@maxwell-west.com               | wnolan                | right-scientist     | Whiteshire               | Zambia             
 1995-08-28 | 20220304193709_2697cb47-2f4e-4e35-943e-6ab0b1ea33e6 | 205.179.105.127 | christopher42@jones.com                  | christina26           | authority-point     | Port Elizabethport       | Northern Mariana Is
 1970-09-29 | 20220304193709_0ab1f14d-9a8a-44fb-be15-78e6bea5274a | 142.154.227.73  | davidmeyer@lyons-kelly.org               | shale                 | happen-result       | North Ericastad          | Guam               
 2019-09-29 | 20220304193709_5caf8396-0ac3-47fc-b252-ebed158c9f3c | 129.154.253.13  | elliottanna@hotmail.com                  | kevinryan             | certain-quality     | Angelabury               | Lao People's Democr
 2013-11-01 | 20220304193709_475f391f-4088-498a-9c98-0d195e928a58 | 156.232.148.30  | rebeccashelton@yahoo.com                 | campossteven          | event-appear-hear   | Donnaview                | Gambia             
 1981-01-16 | 20220304193709_9ff0e1ab-376e-4467-9f8a-8864bd07282e | 218.184.213.23  | johnmcdaniel@yahoo.com                   | conniegould           | you-check-they-box  | New Natasha              | India              
 2008-12-16 | 20220304193709_190888dd-e8b3-49a7-bfb8-333ebf717a71 | 181.113.118.211 | mhernandez@yahoo.com                     | kendra51              | effect-participant  | Hudsonfort               | Philippines        
 2010-03-11 | 20220304193709_87cd9267-8137-453e-862a-c5b9375c3c6a | 102.234.67.59   | madison06@brown.com                      | myersrebecca          | wish-attorney-third | North Amandaberg         | Bhutan             
 1998-07-26 | 20220304193709_bf1cd82e-bd44-4de4-a233-c4841f61843e | 113.177.110.191 | sbaker@henson.net                        | sophia78              | kind-he-message     | Lake Helen               | Nauru              
 1983-09-29 | 20220304193709_bf824a00-2e33-4e17-a7c3-4f0b429894a9 | 9.93.163.89     | mhughes@smith.info                       | roger25               | great-we-check      | Jessicaview              | Australia          
 2017-10-11 | 20220304193709_8878b1d1-ba88-4078-a831-fd9965329cd5 | 108.99.79.19    | andrewmann@hotmail.com                   | downsbarbara          | against-break-out   | Port Molly               | Hungary            
 1991-12-02 | 20220304193709_061af0f7-23a8-4cc5-b2e0-e883251033ad | 179.236.218.82  | gonzalezbenjamin@ortiz.com               | bgibson               | recognize-another   | Lake Charlesstad         | Faroe Islands      
 1979-10-02 | 20220304193709_48484edf-8b44-44bf-b500-200e21db685f | 138.15.169.25   | davidwalker@hinton.com                   | samanthagalloway      | teacher-lot-still   | South Donna              | Togo               
 1976-01-07 | 20220304193709_e1e12131-37e4-4445-91b8-8119aebe776a | 172.148.166.134 | timothy04@clark.info                     | paul02                | shoulder-finish     | New Christopherville     | Djibouti           
 1992-08-25 | 20220304193709_799f7fe3-6611-4aae-a8ea-d22c145c8225 | 169.93.26.209   | ubeltran@gmail.com                       | gerald95              | rule-represent      | East Christopher         | Lesotho            
(query aborted by user)

Query 20220304_194004_00000_e4xjt, FINISHED, 1 node
Splits: 18 total, 18 done (100.00%)
0:01 [4.4K rows, 4.37MB] [5.58K rows/s, 5.54MB/s]
````

![Python](https://github.com/tspannhw/FLiP-PY-FakeDataPulsar/blob/main/fakeusertable.jpg?raw=true)
![Python](https://github.com/tspannhw/FLiP-PY-FakeDataPulsar/blob/main/fakeusertabledescr.jpg?raw=true)
![Python](https://github.com/tspannhw/FLiP-PY-FakeDataPulsar/blob/main/prestoquery.jpg?raw=true)
![Python](https://github.com/tspannhw/FLiP-PY-FakeDataPulsar/blob/main/pulsarsqlresults.jpg?raw=true)


## How to Use

* Step 1:  Import Faker, Add Your Provider

````
from faker import Faker
from faker.providers import internet, address, automotive, barcode, company, date_time, geo, job, misc, person
from faker.providers import phone_number, user_agent

fake = Faker()
fake.add_provider(internet)

````

* Step 2:  Create or Import Your Schema

````
# Pulsar Message Schema
class PulsarUser (Record):
    created_dt = String()
    user_id = String()
    ipv4_public = String()
````

* Step 3:  Connect to Your Cluster and Build a Producer

````
client = pulsar.Client('pulsar://pulsar1:6650')
producer = client.create_producer(topic='persistent://public/default/fakeuser' ,schema=JsonSchema(PulsarUser),properties={"producer-name": "fake-py-sensor","producer-id": "fake-user" })


## TODO

* create parameters for URL, Login, Topic, producer name, producer id, fields, options, schema - maybe class?, # of rows or continuous


## References

* https://faker.readthedocs.io/en/stable/providers.html
* https://faker.readthedocs.io/en/master/
