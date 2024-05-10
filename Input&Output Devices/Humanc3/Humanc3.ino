#include <WiFi.h>
// #include <ESP8266WiFi.h>
// #include <ESP8266WebServer.h>
#include <WebSocketsClient.h>
#include <WebSocketsServer.h>

const int buttonPin1 = 13; 
const int buttonPin2 = 12; 
const int buttonPin3 = 14; 
const int buttonPin4 = 27; 
const int buttonPin5 = 26; 
const int buttonPin6 = 25; 
const int buttonPin7 = 33; 

const int ledPin1 = 15; 
const int ledPin2 = 4; 
const int ledPin3 = 16; 
const int ledPin4 = 17; 
const int ledPin5 = 18; 
const int ledPin6 = 19; 
const int ledPin7 = 21;


WebSocketsServer webSocket = WebSocketsServer(5532);

 const char* ssid = "SSID";
 const char* password = "PASSWORD";

const char* webSocketServerHost = "your_computer_ip";
// const uint16_t webSocketServerPort = 5532;

void setup() {
  pinMode(buttonPin1, INPUT);
  pinMode(buttonPin2, INPUT);
  pinMode(buttonPin3, INPUT);
  pinMode(buttonPin4, INPUT);
  pinMode(buttonPin5, INPUT);
  pinMode(buttonPin6, INPUT);
  pinMode(buttonPin7, INPUT);

  pinMode(ledPin1, OUTPUT);
  pinMode(ledPin2, OUTPUT);
  pinMode(ledPin3, OUTPUT);
  pinMode(ledPin4, OUTPUT);
  pinMode(ledPin5, OUTPUT);
  pinMode(ledPin6, OUTPUT);
  pinMode(ledPin7, OUTPUT);

  Serial.begin(115200);

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected Successfully");
  webSocket.begin();
  webSocket.onEvent(webSocketEvent);
  // 获取并打印ESP8266的IP地址
  IPAddress ip = WiFi.localIP();
  Serial.print("ESP32 wroom的IP地址: ");
  Serial.println(ip);
}

void loop() {
  webSocket.loop();
  int buttonState1 = digitalRead(buttonPin1);
  int buttonState2 = digitalRead(buttonPin2);
  int buttonState3 = digitalRead(buttonPin3);
  int buttonState4 = digitalRead(buttonPin4);
  int buttonState5 = digitalRead(buttonPin5);
  int buttonState6 = digitalRead(buttonPin6);
  int buttonState7 = digitalRead(buttonPin7);

  if (buttonState1 == HIGH) {  
    Serial.println("C3");
    //webSocket.sendTXT("C4");  // 发送音符
    webSocket.broadcastTXT("C3");
    digitalWrite(ledPin1, HIGH);
    delay(400);  // 简单的防抖动
  }else{
    digitalWrite(ledPin1, LOW);
  }
  
  if (buttonState2 == HIGH) {  
    Serial.println("D3");
    //webSocket.sendTXT("D4");  // 发送音符
    webSocket.broadcastTXT("D3");
    digitalWrite(ledPin2, HIGH);
    delay(400);  // 简单的防抖动
  }else{
    digitalWrite(ledPin2, LOW);
  }

  if (buttonState3 == HIGH) {  
    Serial.println("E3");
    //webSocket.sendTXT("D4");  // 发送音符
    webSocket.broadcastTXT("E3");
    digitalWrite(ledPin3, HIGH);
    delay(400);  // 简单的防抖动
  }else{
    digitalWrite(ledPin3, LOW);
  }

  if (buttonState4 == HIGH) {  
    Serial.println("F3");
    //webSocket.sendTXT("D4");  // 发送音符
    webSocket.broadcastTXT("F3");
    digitalWrite(ledPin4, HIGH);
    delay(400);  // 简单的防抖动
  }else{
    digitalWrite(ledPin4, LOW);
  }

  if (buttonState5 == HIGH) {  
    Serial.println("G3");
    //webSocket.sendTXT("D4");  // 发送音符
    webSocket.broadcastTXT("G3");
    digitalWrite(ledPin5, HIGH);
    delay(400);  // 简单的防抖动
  }else{
    digitalWrite(ledPin5, LOW);
  }

  if (buttonState6 == HIGH) {  
    Serial.println("A3");
    //webSocket.sendTXT("D4");  // 发送音符
    webSocket.broadcastTXT("A3");
    digitalWrite(ledPin6, HIGH);
    delay(400);  // 简单的防抖动
  }else{
    digitalWrite(ledPin6, LOW);
  }

  if (buttonState7 == HIGH) {  
    Serial.println("B3");
    //webSocket.sendTXT("D4");  // 发送音符
    webSocket.broadcastTXT("B3");
    digitalWrite(ledPin7, HIGH);
    delay(400);  // 简单的防抖动
  }else{
    digitalWrite(ledPin7, LOW);
  }
}
 void webSocketEvent(uint8_t num, WStype_t type, uint8_t * payload, size_t length) {
  // 处理 WebSocket 事件
 }