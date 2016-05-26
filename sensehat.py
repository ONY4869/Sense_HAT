from sense_hat import SenseHat

while True:
  sense = SenseHat()
  temperature = sense.temperature

  green = (0, 255, 0)
  white = (255, 255, 255)

  temp = 64 * temperature / 100

  pixels = [green if i < temp else white for i in range(64)]

  sense.set_pixels(pixels)
  tempValue = sense.get_temperature()
  print("Temperature: %s C" % tempValue)
