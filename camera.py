#Import the necessary Packages for this software to run
import mediapipe
import cv2

from clock import render_clock
import canvas as cnvs
from off import clear_display
import select

from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.oled.device import ssd1309

from page import Page
from page_machine import PageMachine

#Use MediaPipe to draw the hand framework over the top of hands it identifies in Real-Time
drawingModule = mediapipe.solutions.drawing_utils
handsModule = mediapipe.solutions.hands

#Use CV2 Functionality to create a Video stream and add some values
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')

def wrap_with_delay(f1, delay):
    def f2(device):
        f1(device)
        select.select([],[],[],delay)
    return f2

# Makes a list of the pages for the page machine
def make_page_list():
    page_list = []


    page_list.append(Page("Off", on_enter_func= clear_display))
    page_list.append(Page("Clock", on_enter_func= render_clock, while_running_func=wrap_with_delay(render_clock,0.1)))
    page_list.append(Page("Canvas", on_enter_func=cnvs.run_canvas))
    page_list.append(Page("Weather", on_enter_func=lambda x: x))
    return page_list

serial = spi(port=0, address=0)
device = ssd1309(serial)

pages = make_page_list()

pm = PageMachine(pages, device=device)

#Add confidence values and extra settings to MediaPipe hand tracking. As we are using a live video stream this is not a static
#image mode, confidence values in regards to overall detection and tracking and we will only let two hands be tracked at the same time
#More hands can be tracked at the same time if desired but will slow down the system
with handsModule.Hands(static_image_mode=False, min_detection_confidence=0.7, min_tracking_confidence=0.7, max_num_hands=2) as hands:

#Create an infinite loop which will produce the live feed to our desktop and that will search for hands
    while True:
        #run whjile running of current state
        pm.current_state.while_running_func(pm.device)


        ret, frame = cap.read()
           #Unedit the below line if your live feed is produced upsidedown
           #flipped = cv2.flip(frame, flipCode = -1)
           
           #Determines the frame size, 640 x 480 offers a nice balance between speed and accurate identification
        frame1 = cv2.resize(frame, (320, 240))
           
           #Produces the hand framework overlay ontop of the hand, you can choose the colour here too)
        results = hands.process(cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB))

        pos_dict = {0:(0,0),8:(0,0),12:(0,0),16:(0,0),20:(0,0)}
           
           #In case the system sees multiple hands this if statment deals with that and produces another hand overlay
        if results.multi_hand_landmarks != None:
            for handLandmarks in results.multi_hand_landmarks:
                drawingModule.draw_landmarks(frame1, handLandmarks, handsModule.HAND_CONNECTIONS)
                
                #Below is Added Code to find and print to the shell the Location X-Y coordinates of Index Finger, Uncomment if desired
                for point in handsModule.HandLandmark:
                    
                    normalizedLandmark = handLandmarks.landmark[point]
                    pixelCoordinatesLandmark= drawingModule._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, 640, 480)
                    
                    # Using the Finger Joint Identification Image we know that point 8 represents the tip of the Index Finger
                    if point == 8 or point == 12 or point == 0 or point == 16 or point == 20:  #bottom + finger tips
                        # print(pixelCoordinatesLandmark)
                        pos_dict[point] = pixelCoordinatesLandmark
        
        if(pos_dict[0] and pos_dict[8] and pos_dict[12] and pos_dict[16] and pos_dict[20]):
            height = max(abs(pos_dict[12][1] - pos_dict[0][1]),abs(pos_dict[8][1] - pos_dict[0][1]),abs(pos_dict[16][1] - pos_dict[0][1]),abs(pos_dict[20][1] - pos_dict[0][1]))
            if(abs(pos_dict[8][1] - pos_dict[0][1]) > height/2 and abs(pos_dict[12][1] - pos_dict[0][1]) > height/2 and abs(pos_dict[20][1] - pos_dict[0][1]) < height/2 and abs(pos_dict[16][1] - pos_dict[0][1]) < height/2 and abs(pos_dict[8][0] - pos_dict[12][0]) < 20):
                print("clk")
                pm.go_to(1) #go to clock
            elif(abs(pos_dict[8][1] - pos_dict[0][1]) > height/2 and abs(pos_dict[12][1] - pos_dict[0][1]) > height/2 and abs(pos_dict[16][1] - pos_dict[0][1]) > height/2 and abs(pos_dict[20][1] - pos_dict[0][1]) < height/2 and abs(pos_dict[8][0] - pos_dict[12][0]) < 20 and abs(pos_dict[12][0] - pos_dict[16][0]) < 20):
                print('canvas')
                pm.go_to(2) #go to canvas
            elif(abs(pos_dict[8][1] - pos_dict[0][1]) > height/2 and abs(pos_dict[12][1] - pos_dict[0][1]) < height/2 and abs(pos_dict[16][1] - pos_dict[0][1]) < height/2 and abs(pos_dict[20][1] - pos_dict[0][1]) > height/2):
                print('off')
                pm.go_to(0) #go to canvas

                        
                        
        
        #Below shows the current frame to the desktop 
        # cv2.imshow("Frame", frame1)
        # key = cv2.waitKey(1) & 0xFF
        
        #Below states that if the |q| is press on the keyboard it will stop the system
        # if key == ord("q"):
        #     break