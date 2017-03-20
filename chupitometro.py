                            #include <FastIO.h>
#include <I2CIO.h>
#include <LCD.h>
#include <LiquidCrystal.h>
#include <LiquidCrystal_I2C.h>
#include <LiquidCrystal_SR.h>
#include <LiquidCrystal_SR2W.h>
#include <LiquidCrystal_SR3W.h>



 
 
//Pines en el PCF8574(dir, en,rw,rs,d4,d5,d6,d7,bl, blpol)
//LiquidCrystal_I2C lcd(0x3F, 2, 1, 0, 4, 5, 6, 7, 3, POSITIVE);
LiquidCrystal_I2C lcd(0x27, 2, 1, 0, 4, 5, 6, 7, 3, POSITIVE);
byte letra[8] = {
    B00100,
    B00100,
    B00100,
    B00100,
    B00100,
    B10101,
    B01110,
    B00100
};
byte t_b[8] = {
    B11111,
    B11111,
    B11111,
    B11111,
    B11111,
    B11111,
    B11111,
    B11111
};


/*void setup()
{
  lcd.begin(16,2);
  lcd.backlight();

  lcd.setCursor(0,0);
  lcd.print("Hazme un chupito");  
}*/
int Eje_X = A1 ;
int Eje_Y = A2 ;
char *flojo[4] = {"KoYak","MOra","MOra","KoYak"};
char *medio[4] = {"SAndia","PLatano","SAndia","PLatano"};
char *fuerte[5] = {"RON NEGRO","Whisky","VOdka","RON BLANCO","RON NEGRO"};
char *bonus[4] = {"SAndia","PLatano","KoYak","MOra"};

void setup(){
  Serial.begin(9600);
  lcd.begin(16,2);
  lcd.backlight();
  // registro el nuevo caracter
  lcd.createChar(0, letra);
  lcd.createChar(1, t_b);
  lcd.home();
  lcd.setCursor(0,0);
  lcd.write(byte(1));
  lcd.write(byte(1));
  lcd.print("CHUPITOMETRO");
  lcd.write(byte(1));
  lcd.write(byte(1));
  lcd.write(byte(1));
  lcd.setCursor(0,1);
  // muestro en el LCD el nuevo caracter
  lcd.write(byte(1));
  lcd.write(byte(1));
  lcd.write(byte(1));
  lcd.write(byte(1));
  lcd.write(byte(1));
  lcd.write(byte(0));
  lcd.print("Make");
  lcd.write(byte(0));
  lcd.write(byte(1));
  lcd.write(byte(1));
  lcd.write(byte(1));
  lcd.write(byte(1));
  lcd.write(byte(1));
}


void loop()
{
  int angulo;
  angulo  = map( analogRead(A1), 0, 1024, 0, 180);
  Serial.print(angulo);
  Serial.print("\n");
  delay(100);
  if(angulo > 160){
    angulo = 0;
    lcd.clear();
    delay(100);

      int var =1;
  while(var ==1){
    int selec = 1;
    int select_ =1;
    lcd.setCursor(0,0);
    lcd.print("Nivel:");
    lcd.setCursor(0,1);
    lcd.print("MARICONA");
    delay(1000);
    while (selec ==1){
      angulo  = map( analogRead(A1), 0, 1024, 0, 180);
      if(angulo > 160 && select_==1 ){
            angulo = 0;
            lcd.clear();
            lcd.setCursor(0,0);
            lcd.print("Nivel:");
            lcd.setCursor(0,1);
            lcd.print("NORMAL");
            select_++;
      }
      delay(600);
      angulo  = map( analogRead(A1), 0, 1024, 0, 180);
       if(angulo > 160 && select_==2 ){
            lcd.clear();
            lcd.setCursor(0,0);
            lcd.print("Nivel:");
            lcd.setCursor(0,1);
            lcd.print("J.PLATAS");
            select_++;
      }
      if(angulo < 40){
        lcd.clear();
        lcd.setCursor(0,0);
        lcd.print("GENERANDO");
        lcd.setCursor(0,1);
        lcd.write(byte(1));
        delay(70);
        lcd.write(byte(1));
        delay(70);
        lcd.write(byte(1));
        delay(70);
        lcd.write(byte(1));
        delay(70);
        lcd.write(byte(1));
        delay(70);
                lcd.write(byte(1));
        delay(70);
                lcd.write(byte(1));
        delay(70);
                lcd.write(byte(1));
        delay(70);
                lcd.write(byte(1));
        delay(70);
                lcd.write(byte(1));
        delay(70);
                lcd.write(byte(1));
        delay(70);
                lcd.write(byte(1));
        delay(70);
                lcd.write(byte(1));
        delay(70);
                lcd.write(byte(1));
        delay(70);
        
                lcd.write(byte(1));
        delay(70);

        selec = 0;
        lcd.clear();
        
      }

      
    }

    if (select_ == 1){ //FLOJO
      
      int sum = 0;
      randomSeed(millis());
      int chup = random(0,3);
      delay(5);
      randomSeed(millis());
      int por = random(40,60);
      //por = por + (10 - por);
      lcd.setCursor(0,0);
      lcd.print("CHUPITO:");
      lcd.print(chup);
      lcd.setCursor(0,1);
      lcd.print(flojo[chup]);
      lcd.print(" ");
      lcd.print(por);
      lcd.print("%");
      int a = 0;
      sum = por + sum;
      delay(1000);
      
      while( a == 0){
        //randomSeed(millis());
        angulo = 0;
        angulo  = map( analogRead(A1), 0, 1024, 0, 180);
        if(angulo > 160){
        lcd.clear();
        randomSeed(millis());
        int por = random(40,60);
        delay(5);
        randomSeed(millis());
        int chup = random(0,3);
        if (sum <= 100){
        lcd.setCursor(0,0); 
        lcd.print("CHUPITO:");
        lcd.setCursor(0,1);
        lcd.print(flojo[chup]);
        lcd.print(" ");
        lcd.print(por);
        lcd.print("%");
        sum = por + sum;
        delay(1000);
        }

        else {
          lcd.clear();
          lcd.setCursor(0,0);
          lcd.print("No apoya...");
          delay(1000);
          lcd.setCursor(0,1);
          lcd.print("... no folla");
          delay(2000);
          lcd.clear();
          a = 1;
        }
        }
      }
      
      
      
    }


    if (select_ ==2){
      int sum = 0;

      int ran = random(0,100);

      if(ran <50 ){
        randomSeed(millis());
        randomSeed(millis());
        lcd.print("CHUPITO:");
        int por = random(30,40);
        lcd.setCursor(0,1);
        lcd.print(fuerte[random(0,4)]);
        lcd.print(" ");
        lcd.print(por);
        lcd.print("%");
        sum  = por + sum;
        
        while (sum <= 100){
          randomSeed(millis());
        angulo = 0;
        angulo  = map( analogRead(A1), 0, 1024, 0, 180);
        if(angulo > 160){
        lcd.clear();
        lcd.print("CHUPITO:");
        lcd.setCursor(0,1);
        int por = random(30,40);
        lcd.print(bonus[random(0,4)]);
        lcd.print(" ");
        lcd.print(por);
        lcd.print("%");
        sum  = por + sum;
        delay(1000);
        }
        
        
      }
      }


        if(ran >= 50){
          randomSeed(millis());
        lcd.clear();
        lcd.print("CHUPITO.:");
        int por = random(20,40);
        lcd.setCursor(0,1);
        lcd.print(medio[random(0,3)]);
        lcd.print(" ");
        lcd.print(por);
        lcd.print("%");
        sum  = por + sum;
        
        while (sum <= 100){
          randomSeed(millis());
        angulo = 0;
        angulo  = map( analogRead(A1), 0, 1024, 0, 180);
        if(angulo > 160){
        lcd.clear();
        lcd.print("CHUPITO_:");
        lcd.setCursor(0,1);
        int por = random(20,40);
        lcd.print(bonus[random(0,3)]);
        lcd.print(" ");
        lcd.print(por);
        lcd.print("%");
        sum  = por + sum;
        delay(1000);
        }
        
        
      }
      }
      int z=0;
        while (z == 0){
        angulo = 0;
        angulo  = map( analogRead(A1), 0, 1024, 0, 180);
        if(angulo > 160){
          lcd.clear();
          lcd.setCursor(0,0);
          lcd.print("No apoya...");
          delay(1000);
          lcd.setCursor(0,1);
          lcd.print("... no folla");
          delay(2000);
          z = 1;
          lcd.clear();
        }
        }
          
      
    }

    
   if (select_ ==3){//Fuerte
    randomSeed(millis());
       int sum = 0;
      randomSeed(millis());
      int ran = random(0,100);

      if(ran > 50){
        randomSeed(millis());
        lcd.print("CHUPITO:");
        int por = random(30,40);
        lcd.setCursor(0,1);
        randomSeed(millis());
        lcd.print(fuerte[random(0,4)]);
        lcd.print(" ");
        lcd.print(por);
        lcd.print("%");
        sum  = por + sum;
        
        while (sum <= 100){
        angulo = 0;
        angulo  = map( analogRead(A1), 0, 1024, 0, 180);
        if(angulo > 160){
        lcd.clear();
        lcd.print("CHUPITO:");
        lcd.setCursor(0,1);
        int por = random(30,40);
        randomSeed(millis());
        lcd.print(fuerte[random(0,4)]);
        lcd.print(" ");
        lcd.print(por);
        lcd.print("%");
        sum  = por + sum;
        delay(1000);
        }
        
        
      }
      }


        if(ran <= 50){
        lcd.clear();
        lcd.print("CHUPITO.:");
        int por = random(20,40);
        lcd.setCursor(0,1);
        lcd.print(fuerte[random(0,4)]);
        lcd.print(" ");
        lcd.print(por);
        lcd.print("%");
        sum  = por + sum;
        
        while (sum <= 100){
        angulo = 0;
        angulo  = map( analogRead(A1), 0, 1024, 0, 180);
        if(angulo > 160){
        lcd.clear();
        lcd.print("CHUPITO_:");
        lcd.setCursor(0,1);
        int por = random(20,40);
        lcd.print(medio[random(0,3)]);
        lcd.print(" ");
        lcd.print(por);
        lcd.print("%");
        sum  = por + sum;
        delay(1000);
        }
        
        
      }
      }
      int z=0;
        while (z == 0){
        angulo = 0;
        angulo  = map( analogRead(A1), 0, 1024, 0, 180);
        if(angulo > 160){
          lcd.clear();
          lcd.setCursor(0,0);
          lcd.print("No apoya...");
          delay(1000);
          lcd.setCursor(0,1);
          lcd.print("... no folla");
          delay(2000);
          z = 1;
          lcd.clear();
        }
        }

    
    
   }

    
    
    
    
  }
  }
}

