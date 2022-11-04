"""
The following table lists the sound level in decibels for several common noises.
Noise               |   Decibel Level
----------------------------------------
Jackhammer          |       130 dB
Gas Lawnmower       |       106 dB
Alarm Clock         |        70 dB
Quiet Room          |        40 dB

Write a program that reads a sound level in decibels from the user. If the user
enters a decibel level that matches one of the noises in the table then your program
should display a message containing only that noise. If the user enters a number
of decibels between the noises listed then your program should display a message
indicating which noises the value is between. Ensure that your program also generates
reasonable output for a value smaller than the quietest noise in the table, and for a
value larger than the loudest noise in the table.
"""
NOISE_JACKHAMMER = 130
NOISE_LAWNMOWER = 106
NOISE_ALARM_CLOCK = 70
NOISE_QUIET_ROOM = 40

noise_level = float(input("Enter the noise level: "))
if noise_level > NOISE_JACKHAMMER:
    print("The noise level is higher than the noise level of a jackhammer")
elif noise_level == NOISE_JACKHAMMER:
    print("The noise level is the noise level of a jackhammer")
elif NOISE_LAWNMOWER < noise_level < NOISE_JACKHAMMER:
    print("The noise level is between the noise level of a gas lawnmower and a jackhammer")
elif noise_level == NOISE_LAWNMOWER:
    print("The noise level is the noise level of a gas lawnmower")
elif NOISE_ALARM_CLOCK < noise_level < NOISE_LAWNMOWER:
    print("The noise level is the between the noise level of an alarm clock and a gas lawnmower")
elif noise_level == NOISE_ALARM_CLOCK:
    print("The noise level is the noise level of an alarm clock")
elif NOISE_QUIET_ROOM < noise_level < NOISE_ALARM_CLOCK:
    print("The noise level is the between the noise level of quite room and an alarm clock")
elif noise_level == NOISE_QUIET_ROOM:
    print("The noise level is the noise level of a quite room")
else:
    print("The noise level is less than the noise level of a quite room")
