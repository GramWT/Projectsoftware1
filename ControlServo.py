import serial # serial
import time # delay
servo = serial.Serial("COM6", 9600) # Bluetooth

class Servo(): #ควมคุมองศาของ Servo
    def LA0(self): # LA = Servo ตัวที่1
        servo.write(bytearray([0])) # Servo angle control
        time.sleep(0.05) # delay 0.05 S
    def LA20(self):
        servo.write(bytearray([4]))
        time.sleep(0.05)
    def LA40(self):
        servo.write(bytearray([8]))
        time.sleep(0.05)
    def LA60(self):
        servo.write(bytearray([12]))
        time.sleep(0.05)
    def LA80(self):
        servo.write(bytearray([16]))
        time.sleep(0.05)
    def LA100(self):
        servo.write(bytearray([20]))
        time.sleep(0.05)
    def LA120(self):
        servo.write(bytearray([24]))
        time.sleep(0.05)
    def LA140(self):
        servo.write(bytearray([28]))
        time.sleep(0.05)
    def LA160(self):
        servo.write(bytearray([32]))
        time.sleep(0.05)
    def LA180(self):
        servo.write(bytearray([36]))
        time.sleep(0.05)
    def LB0(self):# LB = Servo ตัวที่2
        servo.write(bytearray([37]))
        time.sleep(0.05)
    def LB20(self):
        servo.write(bytearray([41]))
        time.sleep(0.05)
    def LB40(self):
        servo.write(bytearray([45]))
        time.sleep(0.05)
    def LB60(self):
        servo.write(bytearray([49]))
        time.sleep(0.05)
    def LB80(self):
        servo.write(bytearray([53]))
        time.sleep(0.05)
    def LB100(self):
        servo.write(bytearray([57]))
        time.sleep(0.05)
    def LB120(self):
        servo.write(bytearray([61]))
        time.sleep(0.05)
    def LB140(self):
        servo.write(bytearray([65]))
        time.sleep(0.05)
    def LB160(self):
        servo.write(bytearray([69]))
        time.sleep(0.05)
    def LB180(self):
        servo.write(bytearray([73]))
        time.sleep(0.05)
    def LC0(self):# LC = Servo ตัวที่3
        servo.write(bytearray([74]))
        time.sleep(0.05)
    def LC20(self):
        servo.write(bytearray([78]))
        time.sleep(0.05)
    def LC40(self):
        servo.write(bytearray([82]))
        time.sleep(0.05)
    def LC60(self):
        servo.write(bytearray([86]))
        time.sleep(0.05)
    def LC80(self):
        servo.write(bytearray([90]))
        time.sleep(0.05)
    def LC100(self):
        servo.write(bytearray([94]))
        time.sleep(0.05)
    def LC120(self):
        servo.write(bytearray([98]))
        time.sleep(0.05)
    def LC140(self):
        servo.write(bytearray([102]))
        time.sleep(0.05)
    def LC160(self):
        servo.write(bytearray([106]))
        time.sleep(0.05)
    def LC180(self):
        servo.write(bytearray([110]))
        time.sleep(0.05)
    def LD0(self):# LD = Servo ตัวที่4
        servo.write(bytearray([111]))
        time.sleep(0.05)
    def LD20(self):
        servo.write(bytearray([115]))
        time.sleep(0.05)
    def LD40(self):
        servo.write(bytearray([119]))
        time.sleep(0.05)
    def LD60(self):
        servo.write(bytearray([123]))
        time.sleep(0.05)
    def LD80(self):
        servo.write(bytearray([127]))
        time.sleep(0.05)
    def LD100(self):
        servo.write(bytearray([131]))
        time.sleep(0.05)
    def LD120(self):
        servo.write(bytearray([135]))
        time.sleep(0.05)
    def LD140(self):
        servo.write(bytearray([139]))
        time.sleep(0.05)
    def LD160(self):
        servo.write(bytearray([143]))
        time.sleep(0.05)
    def LD180(self):
        servo.write(bytearray([147]))
        time.sleep(0.05)
    def LE0(self):# LE = Servo ตัวที่5
        servo.write(bytearray([148]))
        time.sleep(0.05)
    def LE20(self):
        servo.write(bytearray([152]))
        time.sleep(0.05)
    def LE40(self):
        servo.write(bytearray([156]))
        time.sleep(0.05)
    def LE60(self):
        servo.write(bytearray([160]))
        time.sleep(0.05)
    def LE80(self):
        servo.write(bytearray([164]))
        time.sleep(0.05)
    def LE100(self):
        servo.write(bytearray([168]))
        time.sleep(0.05)
    def LE120(self):
        servo.write(bytearray([172]))
        time.sleep(0.05)
    def LE140(self):
        servo.write(bytearray([176]))
        time.sleep(0.05)
    def LE160(self):
        servo.write(bytearray([180]))
        time.sleep(0.05)
    def LE180(self):
        servo.write(bytearray([184]))
        time.sleep(0.05)

