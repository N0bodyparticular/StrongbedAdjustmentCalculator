# SMC (c) 2020 dont copy - play nice
# CMRR Strong Bed Calculator - after Colwell 2020
# calculates the "Strong Bed Adjustment" Value form inputs and rules.

sbd = float(input("Enter Strong Bed Difference >"))
thsb = float(input("Enter Thickness of Strong Bed >"))
thwr = float(input("Enter Thickness of suspended weak rock from Strong Bed >"))
actk = float(input("Enter Anchor Thickness >"))


override_value = None

# rules
if (thsb < 0.30) or (actk < 0.30): # rule #3
    override_value = 0.0

if (thsb > 1.22): # rule #4
    thsb = 1.22

if (thwr > 2.59): # rule #5
    thwr = 2.59

if (thwr < 0.52): # rule #6
    thwr = 0.52

spadj = ((0.72 * sbd * thsb) - 2.5) * (1 - (0.1 * (3.28 * thwr - 1.7))) # actual calculation. I don't know if it is actually correct though.

# more rules

if spadj < 0.0: # rule #1
    override_value = 0.0

if spadj > (0.9 * sbd): # rule #2
    override_value = 0.9 * sbd

if override_value == None:
    print("Strong Bed Adjustment (SPADJ) = " + str(spadj))
else:
    print("Strong Bed Adjustment (SPADJ) = " + str(override_value))

input("Press enter to exit...")





