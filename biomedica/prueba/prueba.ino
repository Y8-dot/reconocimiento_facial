int led = 13;

void setup() {
pinMode(led, OUTPUT);
Serial.begin(9600);

}

void loop() {

  Serial.println("Inicio");
  if(Serial.available() >= 0){

    char option = Serial.read();
    switch(option){
      case '0':
      Serial.println("Inicializando, parpadea para iniciar");
      break;
      
      case '1': //aqui es la acción que hará cuando detecte el primer parpadeo
      Serial.println("Primer parpadeo");
      digitalWrite(led, HIGH);
      delay(2000);
      digitalWrite(led, 0);
      delay(2000);
      break;

      case '2': //acción que hara al segundo parpadeo
      Serial.println("Segundo parpadeo");
      digitalWrite(led, HIGH);
      delay(1000);
      digitalWrite(led, 0);
      delay(1000);
      break;      

      case '3': //la acción que hará al tercer parpadeo
      Serial.println("Tercer parpadeo");
      digitalWrite(led, HIGH);
      delay(500);
      digitalWrite(led, 0);
      delay(500);
      break;

      default:
      Serial.println("Te pasaste");
    }

  }

}
