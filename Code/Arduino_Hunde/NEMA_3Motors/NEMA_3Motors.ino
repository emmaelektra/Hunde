// Define the pins for the control signals from the FT232H
const int motor1ControlPin = 2; // Pin connected to FT232H for Motor 1
const int motor2ControlPin = 3; // Pin connected to FT232H for Motor 2
const int motor3ControlPin = 4; // Pin connected to FT232H for Motor 3

// Define the pins for controlling the motors
const int motor1StepPin = 5; // Pin connected to DRV8825 STEP for Motor 1
const int motor1DirPin = 6;  // Pin connected to DRV8825 DIR for Motor 1

const int motor2StepPin = 7; // Pin connected to DRV8825 STEP for Motor 2
const int motor2DirPin = 8;  // Pin connected to DRV8825 DIR for Motor 2

const int motor3StepPin = 9;  // Pin connected to DRV8825 STEP for Motor 3
const int motor3DirPin = 10;  // Pin connected to DRV8825 DIR for Motor 3

void setup() {
  // Set up the control pins as inputs
  pinMode(motor1ControlPin, INPUT);
  pinMode(motor2ControlPin, INPUT);
  pinMode(motor3ControlPin, INPUT);

  // Set up the motor control pins as outputs
  pinMode(motor1StepPin, OUTPUT);
  pinMode(motor1DirPin, OUTPUT);

  pinMode(motor2StepPin, OUTPUT);
  pinMode(motor2DirPin, OUTPUT);

  pinMode(motor3StepPin, OUTPUT);
  pinMode(motor3DirPin, OUTPUT);

  // Initialize the motors to be off
  digitalWrite(motor1StepPin, LOW);
  digitalWrite(motor1DirPin, LOW);

  digitalWrite(motor2StepPin, LOW);
  digitalWrite(motor2DirPin, LOW);

  digitalWrite(motor3StepPin, LOW);
  digitalWrite(motor3DirPin, LOW);
}

void loop() {
  // Check for Motor 1 control signal
  if (digitalRead(motor1ControlPin) == HIGH) {
    runMotor(motor1StepPin, motor1DirPin, 10000);
  }

  // Check for Motor 2 control signal
  if (digitalRead(motor2ControlPin) == HIGH) {
    runMotor(motor2StepPin, motor2DirPin, 10000);
  }

  // Check for Motor 3 control signal
  if (digitalRead(motor3ControlPin) == HIGH) {
    runMotor(motor3StepPin, motor3DirPin, 10000);
  }
}

// Function to run a motor for a specific number of steps
void runMotor(int stepPin, int dirPin, int speedDelay) {
  digitalWrite(stepPin, LOW);

  digitalWrite(dirPin, LOW); // Set direction (adjust as needed)
  delayMicroseconds(100);

  for (int i = 0; i < 100; i++) {  // Example: 200 steps (adjust for your motor)
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(speedDelay);
    digitalWrite(stepPin, LOW);
    delayMicroseconds(speedDelay);
  }

  digitalWrite(dirPin, HIGH); // Set direction (adjust as needed)
  delayMicroseconds(100);

  for (int i = 0; i < 100; i++) {  // Example: 200 steps (adjust for your motor)
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(speedDelay);
    digitalWrite(stepPin, LOW);
    delayMicroseconds(speedDelay);
  }
}