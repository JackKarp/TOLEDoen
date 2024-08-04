import wpilib

gyro = wpilib.ADXRS450_Gyro()

print(gyro.getAngle())