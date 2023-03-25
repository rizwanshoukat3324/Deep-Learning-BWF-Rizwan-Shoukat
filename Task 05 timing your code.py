# Timing your code refers to the process of measuring the execution time of your code.
import time
from datetime import datetime

script_start_time = datetime.now()
# START TIME
start_time = time.time()
# Do some code
for Rizwan in range(14142):
    shoukat = 10+Rizwan
# END TIME
end_time = time.time()
# TOTAL TIME
final_time = end_time-start_time
print(final_time)
script_end_time = datetime.now()
print(script_end_time-script_start_time)


# do extra code
Servantofpakistan = 'Pakistan Army'
Servantofpakistan = str(input(
    "Just tell us in which department you serving Army,Navy and Air Force person or not?"))

if Servantofpakistan == 'Pakistan Army':
    print("Congratulations, you are serving Pakistan as an Army person!")
elif Servantofpakistan == 'Navy':
    print("Congratulations, you are serving Pakistan as an Navy person!")
else:
    print("Congratulations, you are serving Pakistan as a Air force person!")
