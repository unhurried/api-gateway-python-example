from datetime import *
from dateutil.rrule import *

def handler(event, context):
    next_date = rrule(YEARLY, count=1, dtstart=datetime.now(), bymonthday=13, byweekday=FR)[0]
    response = {
        'statusCode': 200,
        'body': "Next 13th Friday is %s" %(next_date.date())
    }
    return response
