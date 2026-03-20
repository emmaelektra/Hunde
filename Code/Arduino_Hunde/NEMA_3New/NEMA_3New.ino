// =========================
// Arduino Nano -> 3x DRV8825
// Robust version:
// - stable inputs with INPUT_PULLUP
// - trigger only on edge, not continuously
// - one forward/back cycle per trigger
// =========================

// ---------- FT232H control inputs ----------
const int motor1ControlPin = 2;
const int motor2ControlPin = 3;
const int motor3ControlPin = 4;

// ---------- DRV8825 control outputs ----------
const int motor1StepPin = 5;

const int motor1DirPin  = 6;

const int motor2StepPin = 7;
const int motor2DirPin  = 8;

const int motor3StepPin = 9;
const int motor3DirPin  = 10;

// ---------- motion settings ----------
const int stepsPerMove = 100;      // forward 100 steps, then back 100 steps
const int stepDelayUs  = 1000;     // smaller = faster; 1000 is a reasonable starting point
const int dirSetupUs   = 100;      // direction setup time before stepping

// ---------- previous input states ----------
bool lastMotor1State = HIGH;
bool lastMotor2State = HIGH;
bool lastMotor3State = HIGH;

// ---------- helper: one motor cycle ----------
void runMotor(int stepPin, int dirPin, int speedDelayUs) {
  // Forward
  digitalWrite(dirPin, LOW);
  delayMicroseconds(dirSetupUs);

  for (int i = 0; i < stepsPerMove; i++) {
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(speedDelayUs);
    digitalWrite(stepPin, LOW);
    delayMicroseconds(speedDelayUs);
  }

  delay(100);

  // Backward
  digitalWrite(dirPin, HIGH);
  delayMicroseconds(dirSetupUs);

  for (int i = 0; i < stepsPerMove; i++) {
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(speedDelayUs);
    digitalWrite(stepPin, LOW);
    delayMicroseconds(speedDelayUs);
  }

  // Leave outputs in a defined state
  digitalWrite(stepPin, LOW);
}

void setup() {
  // Use internal pullups so inputs are stable.
  // ACTIVE = LOW
  pinMode(motor1ControlPin, INPUT_PULLUP);
  pinMode(motor2ControlPin, INPUT_PULLUP);
  pinMode(motor3ControlPin, INPUT_PULLUP);

  pinMode(motor1StepPin, OUTPUT);
  pinMode(motor1DirPin, OUTPUT);

  pinMode(motor2StepPin, OUTPUT);
  pinMode(motor2DirPin, OUTPUT);

  pinMode(motor3StepPin, OUTPUT);
  pinMode(motor3DirPin, OUTPUT);

  digitalWrite(motor1StepPin, LOW);
  digitalWrite(motor1DirPin, LOW);

  digitalWrite(motor2StepPin, LOW);
  digitalWrite(motor2DirPin, LOW);

  digitalWrite(motor3StepPin, LOW);
  digitalWrite(motor3DirPin, LOW);
}

void loop() {
  bool motor1State = digitalRead(motor1ControlPin);
  bool motor2State = digitalRead(motor2ControlPin);
  bool motor3State = digitalRead(motor3ControlPin);

  // Trigger once on falling edge: HIGH -> LOW
  if (lastMotor1State == HIGH && motor1State == LOW) {
    runMotor(motor1StepPin, motor1DirPin, stepDelayUs);
  }

  if (lastMotor2State == HIGH && motor2State == LOW) {
    runMotor(motor2StepPin, motor2DirPin, stepDelayUs);
  }

  if (lastMotor3State == HIGH && motor3State == LOW) {
    runMotor(motor3StepPin, motor3DirPin, stepDelayUs);
  }

  lastMotor1State = motor1State;
  lastMotor2State = motor2State;
  lastMotor3State = motor3State;
}