// C++ code
//
int min_safe_temp = 0;

int max_safe_temp = 0;

int critical_temp = 0;

int current_temp = 0;

void setup()
{
  pinMode(A0, INPUT);
  pinMode(13, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(4, OUTPUT);

  min_safe_temp = 20;
  max_safe_temp = 40;
  critical_temp = 55;
}

void loop()
{
  current_temp = (-40 + 0.488155 * (analogRead(A0) - 20));
  if (current_temp <= max_safe_temp && current_temp >= min_safe_temp) {
    digitalWrite(13, HIGH);
    digitalWrite(12, LOW);
  } else {
    digitalWrite(13, LOW);
    digitalWrite(12, HIGH);
  }
  if (current_temp >= 55) {
    digitalWrite(4, HIGH);
  } else {
    digitalWrite(4, LOW);
  }
  delay(10); // Delay a little bit to improve simulation performance
}
