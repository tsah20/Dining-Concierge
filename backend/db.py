#
#  Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
#  This file is licensed under the Apache License, Version 2.0 (the "License").
#  You may not use this file except in compliance with the License. A copy of
#  the License is located at
# 
#  http://aws.amazon.com/apache2.0/
# 
#  This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
#  CONDITIONS OF ANY KIND, either express or implied. See the License for the
#  specific language governing permissions and limitations under the License.
#
from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal
import datetime

dynamodb = boto3.resource('dynamodb', region_name='us-east-1', aws_access_key_id='AKIATE76IVCTTWBRM7N2',
         aws_secret_access_key= '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')
table = dynamodb.Table('yelp-restaurants2')

json_filename = 'chinese'

with open("../data/restaurants_{}.json".format(json_filename)) as json_file:
    restaurants = json.load(json_file)
    count= 0
    for restaurant in restaurants:
        try:
            item = {
            'id': restaurant['id'],
            'insertedAtTimestamp': str(datetime.datetime.now().timestamp()*1000),
            'name': restaurant['name'],
            'rating':str(restaurant['rating']),
            'num_reviews': str(restaurant['review_count']),
            'address' : restaurant['location']['display_address'],
            'coordinates': str(restaurant['coordinates']),
            'zipcode': restaurant['location']['zip_code'],
            'cuisine': '{}'.format(json_filename)
            }

            table.put_item(Item=item)
            count+=1
        except:
            pass
    print('Number of restaurants inserted: ', count)
