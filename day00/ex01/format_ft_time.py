import time
from datetime import datetime
second_since_chhal_hadi = time.time()
print(f"Seconds since January 1, 1970: {second_since_chhal_hadi:,} or {second_since_chhal_hadi:.2e}  in scientific notation")
now = datetime.now()
formated_date = now.strftime("%b, %d, %Y")
print(f"{formated_date}")