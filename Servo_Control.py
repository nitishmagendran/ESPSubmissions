from machine import Pin, PWM
servo = PWM(Pin(2))
def mapping(x, in_min, in_max, ou_min, ou_max):
    return max(min(ou_max, (x - in_min) * (ou_max - ou_min) // (in_max - in_min) + ou_min), ou_min)




servo.freq(50)
inp_angle = int(input("Please enter the angle for servo: "))
out = mapping(abs(inp_angle),0,180,20,120)
if inp_angle>=0:
    pass
else:
    out = -1*(out)
servo.duty(out)
