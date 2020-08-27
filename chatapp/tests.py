from django.test import TestCase

# Create your tests here.
import json

text = '{"a":"abc", "c":"cba"}'

a = json.loads(text)
print(a)