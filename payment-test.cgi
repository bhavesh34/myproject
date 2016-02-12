#!/usr/bin/env python
# -*- coding: UTF-8 -*-
 
#1
import sys
import json
import cgi
import cgitb
import stripe
 
#2
cgitb.enable()
 
print 'Content-Type: text/json'     
print                               
 
#3
stripe.api_key = 'sk_test_jwoiBJMNwlkpbQWaxZ46wief'
 
#4
json_data = sys.stdin.read()
json_dict = json.loads(json_data)
 
#5
stripeAmount = json_dict['stripeAmount']
stripeCurrency = json_dict['stripeCurrency']
stripeToken = json_dict['stripeToken']
stripeDescription = json_dict['stripeDescription']
 
#6
json_response = stripe.Charge.create(amount=stripeAmount, currency=stripeCurrency, card=stripeToken, description=stripeDescription)

print json_response
