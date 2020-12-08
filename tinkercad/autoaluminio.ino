//	Motor 1 (Rueda Izquierda)
int pin1=3;
int pin2=5;

// 	Motor 2	(Rueda Derecha)
int pin3=6;
int pin4=9;

//	Papel aluminio - Pulsador
int pin5=12;

char direccion;				            // Ingresada por teclado..

void motorSetup(){
  pinMode(pin1, OUTPUT);
  pinMode(pin2, OUTPUT);
  pinMode(pin3, OUTPUT);
  pinMode(pin4, OUTPUT);
}

void setup(){
  Serial.begin(9600);		           	// bits por seg
  motorSetup();					        // se configuran como salidas los pines motor
  pinMode(pin5, INPUT_PULLUP);	        // se habilita resistencia pull up utilizada por el pulsador
}

void loop(){
  direccion = lectura();                //Se ingresa la direccion deseada
  if(direccion >= 49 && direccion <=52){
  	enMovimiento();  				//Se realiza el movimiento requerido 
  }
}

char lectura(){
  Serial.println("Ingrese el nro de la direccion deseada:");
  Serial.println("1-Adelante.");
  Serial.println("2-Girar derecha.");
  Serial.println("3-Girar izquierda.");
  Serial.println("4-Atras.");
  while (!Serial.available());{
  	direccion = Serial.read();
    Serial.println();
  }
  
  return direccion;
}

void enMovimiento(){
  Serial.println();
  Serial.println("Auto en movimiento");
  switch(direccion){
    case 49:
    	Serial.println("Adelante");
    	while(digitalRead(pin5)!=0){
        	forward();
        }
    	break;
    
    case 50:
    	Serial.println("Gira a la derecha");
    	while(digitalRead(pin5)!=0){
        	turnRight();
        }
    	break;
    
    case 51:
    	Serial.println("Gira a la izquierda");
    	while(digitalRead(pin5)!=0){
        	turnLeft();
        }
    	break;
    
    case 52:
        Serial.println("Retrocede");    
    	while(digitalRead(pin5)!=0){
        	backward();
        }
    	break;
   
    default:
    	break;
  } 
  stop();
  Serial.println();
  Serial.println("****COLISION****");
  Serial.println("El auto a parado");
  Serial.println();
}

void forward(){
  digitalWrite(pin1, HIGH);
  digitalWrite(pin3, HIGH);
  digitalWrite(pin2, LOW);
  digitalWrite(pin4, LOW);
}

void backward(){
  digitalWrite(pin2, HIGH);
  digitalWrite(pin4, HIGH);
  digitalWrite(pin1, LOW);
  digitalWrite(pin3, LOW);
}

void turnRight(){
  digitalWrite(pin1, LOW);
  digitalWrite(pin3, HIGH);
  digitalWrite(pin2, HIGH);
  digitalWrite(pin4, LOW);
}

void turnLeft(){
  digitalWrite(pin1, HIGH);
  digitalWrite(pin3, LOW);
  digitalWrite(pin2, LOW);
  digitalWrite(pin4, HIGH);
}

void stop(){
  digitalWrite(pin1, LOW);
  digitalWrite(pin3, LOW);
  digitalWrite(pin2, LOW);
  digitalWrite(pin4, LOW);
}