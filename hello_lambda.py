import json

def endresult(nameofperson):
  if nameofperson == "david":
     return "Hello {}".format(nameofperson)
  elif nameofperson != "david":
     return "Welcome back {}".format(nameofperson)  
  else: 
     return "{}".format(nameofperson)
def get_handler(event, context):
    return { "message": "Hello, World!" }

def post_handler(event, context):
   # body=json.loads(event)
    nameofperson= event['name']

    return {
        'statusCode': 200,
        'body': json.dumps(endresult(nameofperson))
    }

def del_handler(event,context):
    nameofperson= event['name']

    return {
        'statusCode': 200,
        'body': json.dumps(endresult(nameofperson))
    }
     




     

