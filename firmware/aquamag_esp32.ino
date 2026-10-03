// AquaMag Scout - sampling skeleton (untested on hardware)
// Reads magnetometer + coil ADC + pressure and prints CSV over serial.

const int COIL_PIN = 34;       // ADC input from pulse-induction coil
const int PRESSURE_PIN = 35;   // ADC input from pressure sensor

void setup() {
  Serial.begin(115200);
  Serial.println("t_ms,mag_uT,coil_mV,pressure_raw");
}

float readMagnetometer() {
  // TODO: replace with I2C read from your magnetometer
  return 0.0;
}

void loop() {
  float coil_mV = analogReadMilliVolts(COIL_PIN);
  int pressure = analogRead(PRESSURE_PIN);
  Serial.printf("%lu,%.2f,%.1f,%d\n", millis(), readMagnetometer(), coil_mV, pressure);
  delay(100);  // 10 Hz
}