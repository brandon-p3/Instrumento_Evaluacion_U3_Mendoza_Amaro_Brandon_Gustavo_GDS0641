# Instrumento_Evaluacion_U3_Mendoza_Amaro_Brandon_Gustavo_GDS0641

## Personaje-Navideño


## Nombre del personaje 

!!  SNOW MAN  ¡¡

##  Nombre Integrantes Equipo

|Nombre | Apellido Paterno | Apellido Materno |
|-|-|-|
|Brandon Gustavo|Mendoza|Amaro|
|Mirza Natzielly|Morales|Lezama|

## Materiales a utilizar (Componentes tecnicos)


|Nom Componente | Descripcion | Cantidad| Precio|
|-|-|-|-|
|ESP32|Microcontrolador con 30 pines con comunicacion WIFI y Bluetooth|1|$120.00|
|Cable dupont|Cables para conexion de prototipos de pruebas|50|$60.00|
|Sensor Ultrasonico Hc-sr04 Arduino Pic Raspberry1|Sensor de proximidad que activara el mecanismo del muñeco|2|$70.00|
|Led|Se utiliza para iluminar el muñeco|3|$3.00|
|Tira Led|Tira de foquitos leds|2|$16.00|
|Motor A Pasos 28byj-48 Con Driver Unl2003 Arduino|Motor a pasos, este movera la cabeza del muñeco|1|$70.00|
|Servomotor Micro Sg90 |Servo motoro que movera el brazo del muñeco|1|$60.00|
|Buzzer Ky-006 Zumbador Pasivo Modulo|Buzzer que emitira una musica navideña|1|$40.00|
|Modulo Matriz Led Max7219 Para Arduino 4 Módulos Rojo|Modulo Matrix que mostrara un mensaje|1|$100.00|

## Materiales a utilizar (Creacion del muñeco)


|Nom Componente | Descripcion | Cantidad| Precio|
|-|-|-|-|
|Base de plastico|Base donde se colocara el muñeco|1|$15.00|
|Bolas chinas|Funcionaran como el cuerpo y la cabeza del muñeco|2|$50.00|
|Bolas de unicel|Simularan nieve y funcionaran como forraje del muñeco |2 paquetes|$16.00|
|Hojas de color|Nariz del muñeco|1|$2.00|
|Ojos locos|Ojos del muñeco|2|$5.00|
|Silicon|Barras de silicon|15|$50.00|
|Lenguetas|Funcionaran como los brazos del muñeco|1 paquetes|$20.00|
|Cartulina negra|Hacer el sombrero del muñeco|1|$5.00|
|Trozo de tela|Bufanda del muñeco|1|$0.00|
|Fomi|Forrar los brazos del muñeco|4|$10.00|
|Carton|Cuerpo interno del muñeco|2|$0.00|


## Software a Utilizar
|Nombre|Version|Tipo Software|
|-|-|-|
|Thonny|4.2.1|Software Libre|
|Node Red|4.0.5|Software Libre|
|dcmotor||Libreria|
|stepper||Libreria|
|ssd1306||Libreria|
|hcsr04||Libreria|
|max7219||Libreria|
|navidad_buzzer||Libreria|
|machine|Integrada|Libreria estándar|
|time|Integrada|Libreria estándar|



## Prototipo en dibujo

<img src="https://github.com/user-attachments/assets/08f983a5-4605-415f-acb1-27033e494bb7"/>


## Comunicacion
La comunicación del usuario con el prototipo se realizará mediante una conexión inalámbrica a través del protocolo Wi-Fi. El ESP32 actuará como un servidor Wi-Fi, permitiendo que el usuario interactúe con el muñeco de nieve mediante una interfaz web. Los comandos enviados desde la interfaz web controlarán diversas funciones del personaje navideño, como cambiar la forma en que se muestran las luces, realizar un saludo, mostrar un mensaje, cambiar la tonada navideña y mover la cabeza del muñeco.

## Arquitectura 
<img src="https://github.com/user-attachments/assets/572ecf2a-7496-427e-9c6f-39efa4db82a3"/>




## Flujo en node-red
![Base de Datos](https://github.com/ABOK451/Personaje-Navide-o/blob/main/imagen_2023-09-30_194854915.png)

## VIDEO EXPLICATIVO DEL FUNCIONAMIENTO 
https://github.com/ABOK451/Personaje-Navide-o/blob/main/VIDEOS_FUNCIONAMIENTO/VID-20231205-WA0007.mp4

## TIKTOK
https://github.com/ABOK451/Personaje-Navide-o/blob/main/VIDEOS_FUNCIONAMIENTO/VID-20231205-WA0007.mp4

## FOTOS DE ELABORACION 
<div style="display: flex; flex-wrap: wrap; gap: 10px; justify-content: center;"> 
  <img src="https://github.com/user-attachments/assets/e2f53b93-2a36-44a9-b994-e9cf476ada86" alt="Imagen 1" style="width: 33%; height: 300px; object-fit: cover; border-radius: 8px;"> 
  <img src="https://github.com/user-attachments/assets/81be7d51-57be-4f49-8efe-86b202cad4a0" alt="Imagen 2" style="width: 33%; height: 300px; object-fit: cover; border-radius: 8px;"> 
  <img src="https://github.com/user-attachments/assets/930605e4-863d-400e-afb1-74bd63bbf1db" alt="Imagen 3" style="width: 33%; height: 300px; object-fit: cover; border-radius: 8px;"> 
  <img src="https://github.com/user-attachments/assets/aac358ca-358d-4f91-a316-20afa47b332a" alt="Imagen 4" style="width: 33%; height: 300px; object-fit: cover; border-radius: 8px;"> 
  <img src="https://github.com/user-attachments/assets/9bf143fc-a258-4d85-968e-25abb2550598" alt="Imagen 5" style="width: 33%; height: 300px; object-fit: cover; border-radius: 8px;"> 
  <img src="https://github.com/user-attachments/assets/7f503e5c-7957-4c7c-8bc1-d20d1e3af157" alt="Imagen 6" style="width: 33%; height: 300px; object-fit: cover; border-radius: 8px;"> 
  <img src="https://github.com/user-attachments/assets/4c759132-3f87-42f5-bd60-4a7e41f1adcb" alt="Imagen 7" style="width: 33%; height: 300px; object-fit: cover; border-radius: 8px;"> 
</div>

## LINK CODIGO 
https://github.com/brandon-p3/Instrumento_Evaluacion_U3_Mendoza_Amaro_Brandon_Gustavo_GDS0641/tree/e06de89bc9803ec0c3f5a43210e0ec5b72716cc7/SnowMan_C%C3%B3digo_Paython


# LINK VIDEOS Y EJERCICIOS REALIZADOS EN CLASE
https://drive.google.com/drive/folders/1NwvHqvySfX4l7kal_qeOEFrnmFDDOmEj?usp=sharing

# Capturas de pantalla de los examenes de NetaCad:

## Modulo 1
<img src="https://github.com/user-attachments/assets/ba8aa2d3-2756-4f22-aaea-e63e0f360f66"/>

## Modulo 2
<img src="https://github.com/user-attachments/assets/948b88e0-c5d8-406b-83ab-c363abac386c"/>

## Modulo 3
<img src="https://github.com/user-attachments/assets/f23021da-57fd-41ee-8bea-4cb9bcebc0b0"/>

## Modulo 4
<img src="https://github.com/user-attachments/assets/9e865d9c-9a2d-40da-b252-d354e13fc1c9"/>

## Modulo 5
<img src="https://github.com/user-attachments/assets/86013590-8c15-45c6-8a05-3bf0fa81fa9f"/>

## Modulo 6
<img src="https://github.com/user-attachments/assets/16ad81c3-e031-41c8-b23f-ca694f7b2638"/>


## Examen final
<img src="https://github.com/user-attachments/assets/d77873d0-9999-4cc7-be51-14f7d784c90d"/>
