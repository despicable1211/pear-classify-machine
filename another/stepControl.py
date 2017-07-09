# -* coding:utf-8 -*-
import RPi.GPIO as GPIO  
import time
        

class stepControl():
    fixber_flag = 0
    IN1 = 31    # pin11  
    IN2 = 33
    IN3 = 35  
    IN4 = 37
    IN5 = 16
    IN6 = 18
    #IN7 = 12
    IN8 = 32
    IN9 = 36
    
    def __init__(self):
        self.setup()
        
    def setStep(self,w1, w2, w3, w4):  
        GPIO.output(self.IN1, w1)  
        GPIO.output(self.IN2, w2)  
        GPIO.output(self.IN3, w3)  
        GPIO.output(self.IN4, w4)  
  
    def stop(self):  
        setStep(0, 0, 0, 0)  
      
    def forward(self,delay, steps):
        for i in range(0, steps):  
            self.setStep(1, 0, 0, 0)  
            time.sleep(delay)  
            self.setStep(1, 0, 1, 0)  
            time.sleep(delay)  
            self.setStep(0, 0, 1, 0)  
            time.sleep(delay)  
            self.setStep(0, 1, 1, 0)  
            time.sleep(delay)
            self.setStep(0, 1, 0, 0)
            time.sleep(delay)  
            self.setStep(0, 1, 0, 1)
            time.sleep(delay)  
            self.setStep(0, 0, 0, 1)
            time.sleep(delay)  
            self.setStep(1, 0, 0, 1)
            time.sleep(delay)  
      
    def backward(self,delay, steps):
        for i in range(0, steps):  
            self.setStep(0, 0, 0, 1)  
            time.sleep(delay)  
            self.setStep(0, 1, 0, 1)  
            time.sleep(delay)  
            self.setStep(0, 1, 0, 0)  
            time.sleep(delay)  
            self.setStep(0, 1, 1, 0)  
            time.sleep(delay)
            self.setStep(0, 0, 1, 0)  
            time.sleep(delay)  
            self.setStep(1, 0, 1, 0)  
            time.sleep(delay)  
            self.setStep(1, 0, 0, 0)  
            time.sleep(delay) 
            self.setStep(1, 0, 0, 1)  
            time.sleep(delay)
        
    def setup(self):  
        GPIO.setwarnings(False)  
        GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location  
        GPIO.setup(self.IN1, GPIO.OUT)      # Set pin's mode is output  
        GPIO.setup(self.IN2, GPIO.OUT)  
        GPIO.setup(self.IN3, GPIO.OUT)  
        GPIO.setup(self.IN4, GPIO.OUT)
        GPIO.setup(self.IN8, GPIO.OUT)
        GPIO.setup(self.IN9, GPIO.OUT)
        GPIO.setup(self.IN5, GPIO.OUT)
        GPIO.setup(self.IN6, GPIO.OUT)
        #GPIO.setup(self.IN7, GPIO.IN, pull_up_down = GPIO.PUD_UP)
        #GPIO.add_event_detect(self.IN7,GPIO.FALLING,callback=self.fixber)        
            
    def fixber(self,channel):
        print "光纤信号检测成功"
        self.fixber_flag = 1
        time.sleep(2)
        
    def control(self,step):
        direction = 0
        if(step<0):
            direction = 2
            step = 0-step
        print "backward..."
        GPIO.output(self.IN5, 1)
        time.sleep(0.3)
        GPIO.output(self.IN5, 0)
        print step
        if(direction == 2):
            self.forward(0.0005, step)
        else:
            self.backward(0.0005, step)  # 512 steps --- 360 angle  
        GPIO.output(self.IN6, 1)
        time.sleep(0.3)
        GPIO.output(self.IN6 , 0) 
        print "forward..."
        if(direction == 2):
            self.backward(0.0005, step)  # 512 steps --- 360 angle
        else:
            self.forward(0.0005, step)

    def motorGO(self,step):
        GPIO.output(self.IN8, 1)
        GPIO.output(self.IN9, 1)
        self.control(step)
        GPIO.output(self.IN8, 0)
        GPIO.output(self.IN9, 0)
                
if __name__ == '__main__':     # Program start from here
    stepclass = stepControl()
    stepclass.setup()
    stepclass.setStep(0, 0, 0, 0)
    GPIO.setup(12,GPIO.IN,pull_up_down = GPIO.PUD_UP)
    try:  
        while True:
            if(GPIO.input(12) == GPIO.LOW):
                stepclass.motorGO(-115)
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child function destroy() will be  executed.  
        GPIO.cleanup()    
        
