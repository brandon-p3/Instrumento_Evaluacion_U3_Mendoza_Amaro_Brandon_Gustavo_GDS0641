from machine import Pin, PWM, SPI
from time import sleep, time
from hcsr04 import HCSR04
from max7219 import Matrix8x8
from _thread import start_new_thread  # Importar para hilos

# -------------------- Configuración de pines y objetos --------------------

IN1 = Pin(16, Pin.OUT)
IN2 = Pin(17, Pin.OUT)
IN3 = Pin(33, Pin.OUT)
IN4 = Pin(32, Pin.OUT)
pins = [IN1, IN2, IN3, IN4]

BUZZER_PIN = Pin(15, Pin.OUT)

spi = SPI(1, baudrate=10000000, polarity=0, phase=0, sck=Pin(25), mosi=Pin(27))
cs = Pin(26, Pin.OUT)
matrix = Matrix8x8(spi, cs, 4)

sensor = HCSR04(trigger_pin=5, echo_pin=18, echo_timeout_us=24000)

led1 = Pin(16, Pin.OUT)
led2 = Pin(17, Pin.OUT)
led3 = Pin(23, Pin.OUT)

pwm_servo = PWM(Pin(14), freq=50)

sequence_left = [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
]

sequence_right = sequence_left[::-1]

# -------------------- Melodía --------------------

notes = [262, 349, 349, 392, 349, 330, 294, 294, 294, 294, 392, 392, 440, 392, 349, 330, 262]
durations = [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.8, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.8]

def reproducir_melodia():
    pwm = PWM(BUZZER_PIN)  # Inicializa el buzzer como PWM
    pwm.duty(512)  # Configura la intensidad del sonido (50%)

    for note, duration in zip(notes, durations):
        if not en_rutina:
            break
        pwm.freq(note)  # Cambia la frecuencia para la nota actual
        sleep(duration)

    pwm.deinit()  # Detiene el buzzer al finalizar

# -------------------- Funciones de control --------------------

def step_motor(sequence, steps=512, delay=0.002):
    for _ in range(steps):
        for step in sequence:
            for i in range(len(pins)):
                pins[i].value(step[i])
            sleep(delay)

def mover_servo(angulo):
    duty = int(40 + (angulo / 180) * 77)
    pwm_servo.duty(duty)

def mostrar_texto_hoho():
    mensaje = "HO HO HO   "
    longitud_mensaje = len(mensaje) * 8

    for posicion in range(longitud_mensaje):
        if not en_rutina:
            break
        matrix.fill(0)
        matrix.text(mensaje, -posicion, 0, 1)
        matrix.show()
        sleep(0.1)

def mostrar_texto_feliz_navidad():
    mensaje = "Feliz Navidad   "
    longitud_mensaje = len(mensaje) * 8

    for posicion in range(longitud_mensaje):
        if not en_rutina:
            break
        matrix.fill(0)
        matrix.text(mensaje, -posicion, 0, 1)
        matrix.show()
        sleep(0.1)

def parpadear_leds():
    while True:
        led2.on()
        sleep(0.2)
        led3.on()
        sleep(0.2)
        led2.off()
        sleep(0.2)
        led3.off()
        sleep(0.2)

def rutina_navidad():
    global en_rutina
    en_rutina = True
    led1.on()  # Enciende el LED1 al iniciar el mecanismo
    print("¡Se ha activado el mecanismo de Navidad!")
    
    # Inicia los hilos secundarios
    start_new_thread(reproducir_melodia, ())
    start_new_thread(mostrar_texto_hoho, ())

    # Realiza el saludo
    mover_servo(0)
    sleep(1)
    mover_servo(20)
    sleep(1)
    mover_servo(0)
    mover_servo(0)
    sleep(1)
    mover_servo(20)
    sleep(1)
    mover_servo(0)

    # Gira el motor a la derecha y luego a la izquierda
    step_motor(sequence_left, steps=512)
    step_motor(sequence_right, steps=512)

    # Cambia el mensaje a "Feliz Navidad"
    start_new_thread( mostrar_texto_feliz_navidad, ())
    mover_servo(0)
    sleep(1)
    mover_servo(20)
    sleep(1)
    mover_servo(0)
    mover_servo(0)
    sleep(1)
    mover_servo(20)
    sleep(1)
    mover_servo(0)

    led1.off()  # Apaga el LED1 al terminar el mecanismo
    en_rutina = False

# -------------------- Hilo para los LEDs navideños --------------------

def _start_leds_thread():
    start_new_thread(parpadear_leds, ())

# -------------------- Ejecución principal --------------------

en_rutina = False

# Inicia el parpadeo de LEDs navideños en un hilo separado
_start_leds_thread()

while True:
    distancia = sensor.distance_cm()
    if distancia < 10 and not en_rutina:
        rutina_navidad()
        print("¡Se acabo!")
    sleep(0.1)
