# 1 Convert the time entered in hh,min and sec into seconds.

hours = int(input('Enter Hours :'))
min = int(input('Enter Minutes :'))
sec = int(input('Enter Seconds :'))

total_seconds = ((hours*3600) + (min*60) + (sec))
print(f'Total Seconds is {total_seconds}')