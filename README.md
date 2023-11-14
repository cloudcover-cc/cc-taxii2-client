# cc-taxii2-client
## CloudCover minimal TAXII2.1 Python client library.

Basic usage:

```python
>>> from cc_taxii2_client import CCTaxiiClient
>>> connection = CCTaxiiClient("testaccount", "XxXxXx")
>>> connection
CCTaxiiClient(account='testaccount', url='https://taxii2.cloudcover.net', headers={'Accept': 'application/taxii+json;version=2.1', 'Content-Type': 'application/taxii+json;version=2.1', 'Authorization': 'Basic dGVzdF9hY2NvdW50Olh4WHhYeA=='})
>>>
>>> connection.get_collections()
['decb0efc-6a36-4dd7-a4dd-7f955f42b977']
>>>
conection.get_collections("testaccount")
['c774c554-038c-46a6-8339-9ddfae4cd871']
>>>
>>> from cc_taxii2_client import count_indicators
>>> generate_indicators = connection.get_cc_indicators_generator(private=True, follow_pages=True)
>>> count_indicators(generate_indicators)
711
>>> 
>>> generate_indicators = connection.get_cc_indicators_generator(private=True, limit=2, added_after="2023-11-03T19:07:51.812746Z", follow_pages=True)
>>> next(generate_indicators)
[CCIndicator(created='2023-11-03T19:07:51.812746Z', description='#Recon# ICMP PING', id='indicator--5c46d792-93a9-435c-a04f-b843de740fe6', modified='2023-11-03T19:07:51.812746Z', name='CloudCover Detected IOC', pattern="[ipv4-addr:value = '13.127.11.123']", pattern_type='stix', pattern_version='2.1', spec_version='2.1', type='indicator', valid_from='2023-11-03T19:07:51.812746Z'), CCIndicator(created='2023-11-03T19:07:51.816509Z', description='#Recon# ICMP PING', id='indicator--3d217760-a17a-41b4-af5f-5b5bf72ff396', modified='2023-11-03T19:07:51.816509Z', name='CloudCover Detected IOC', pattern="[ipv4-addr:value = '34.219.199.125']", pattern_type='stix', pattern_version='2.1', spec_version='2.1', type='indicator', valid_from='2023-11-03T19:07:51.816509Z')]
>>>
>>> next(generate_indicators)
[CCIndicator(created='2023-11-03T19:07:51.817258Z', description='#Recon# ICMP PING', id='indicator--6b405c16-ac9b-4446-8d13-1cc17a4cf867', modified='2023-11-03T19:07:51.817258Z', name='CloudCover Detected IOC', pattern="[ipv4-addr:value = '34.218.245.10']", pattern_type='stix', pattern_version='2.1', spec_version='2.1', type='indicator', valid_from='2023-11-03T19:07:51.817258Z'), CCIndicator(created='2023-11-03T19:07:51.817689Z', description='#Recon# ICMP PING', id='indicator--401dcddb-8757-4f05-bde5-6d324d6cbda6', modified='2023-11-03T19:07:51.817689Z', name='CloudCover Detected IOC', pattern="[ipv4-addr:value = '3.74.157.199']", pattern_type='stix', pattern_version='2.1', spec_version='2.1', type='indicator', valid_from='2023-11-03T19:07:51.817689Z')]
>>>
>>> from cc_taxii2_client import ip_search
>>> generate_indicators = connection.get_cc_indicators_generator(private=True, follow_pages=True)
>>> ip_search("13.127.11.123")
[CCIndicator(created='2023-11-03T19:07:51.812746Z', description='#Recon# ICMP PING', id='indicator--5c46d792-93a9-435c-a04f-b843de740fe6', modified='2023-11-03T19:07:51.812746Z', name='CloudCover Detected IOC', pattern="[ipv4-addr:value = '13.127.11.123']", pattern_type='stix', pattern_version='2.1', spec_version='2.1', type='indicator', valid_from='2023-11-03T19:07:51.812746Z')
>>>
>>> from cc_taxii2_client import description_search
>>> generate_indicators = connection.get_cc_indicators_generator(private=True, follow_pages=True)
>>> indicators = description_search("Recon", generate_indicators)
>>> len(indicators)
711
>>>
>>> from itertools import chain
>>> generate_indicators = connection.get_cc_indicators_generator(private=True, follow_pages=True, matches={"type": "indicator", "id": "indicator--5c46d792-93a9-435c-a04f-b843de740fe6,indicator--6b405c16-ac9b-4446-8d13-1cc17a4cf867"})
>>> list(chain(*generate_indicators))
[CCIndicator(created='2023-11-03T19:07:51.812746Z', description='#Recon# ICMP PING', id='indicator--5c46d792-93a9-435c-a04f-b843de740fe6', modified='2023-11-03T19:07:51.812746Z', name='CloudCover Detected IOC', pattern="[ipv4-addr:value = '13.127.11.123']", pattern_type='stix', pattern_version='2.1', spec_version='2.1', type='indicator', valid_from='2023-11-03T19:07:51.812746Z'), CCIndicator(created='2023-11-03T19:07:51.817258Z', description='#Recon# ICMP PING', id='indicator--6b405c16-ac9b-4446-8d13-1cc17a4cf867', modified='2023-11-03T19:07:51.817258Z', name='CloudCover Detected IOC', pattern="[ipv4-addr:value = '34.218.245.10']", pattern_type='stix', pattern_version='2.1', spec_version='2.1', type='indicator', valid_from='2023-11-03T19:07:51.817258Z')]

```
