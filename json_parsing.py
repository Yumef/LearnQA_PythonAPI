
import json

json_text = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'
parsed_response = json.loads(json_text)

for key in parsed_response:
    value_response = parsed_response[key]

for i in value_response:
    second = value_response[1]

for key in second:
    if key == 'message':
        message = second[key]

print(message)