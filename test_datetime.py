import datetime
from datetime import timezone

# utc time in ios format


utc = datetime.datetime.now(timezone.utc).isoformat()
print(utc)
print(type(utc))

print(type(datetime.datetime.now()))
