import cv2
import numpy as np
import RPi.GPIO as GPIO

cap = cv2.VideoCapture(0)  # Get video source from the webcam
cap.set(3, 160)  # Adjust frame size to 160x120 pixels
cap.set(4, 120)
in1 = 15  # Declare GPIO pin of the Raspberry Pi
in2 = 17  # Declare GPIO pin of the Raspberry Pi
in3 = 27  # Declare GPIO pin of the Raspberry Pi
in4 = 22  # Declare GPIO pin of the Raspberry Pi
en1 = 12  # Declare GPIO pin of the Raspberry Pi
en2 = 13  # Declare GPIO pin of the Raspberry Pi
GPIO.setmode(GPIO.BCM)  # Set RPi.GPIO mode as BCM (can choose between BCM and BOARD, here BCM is selected)
GPIO.setup(en1, GPIO.OUT)  # Set the direction of en1, en2, in1, in2, in3, in4 pins to output
GPIO.setup(en2, GPIO.OUT)  # Set the direction of en1, en2, in1, in2, in3, in4 pins to output
GPIO.setup(in1, GPIO.OUT)  # Set the direction of en1, en2, in1, in2, in3, in4 pins to output
GPIO.setup(in2, GPIO.OUT)  # Set the direction of en1, en2, in1, in2, in3, in4 pins to output
GPIO.setup(in3, GPIO.OUT)  # Set the direction of en1, en2, in1, in2, in3, in4 pins to output
GPIO.setup(in4, GPIO.OUT)  # Set the direction of en1, en2, in1, in2, in3, in4 pins to output
p1 = GPIO.PWM(en1, 100)  # Set PWM output parameters for en1 with a frequency of 100
p2 = GPIO.PWM(en2, 100)  # Set PWM output parameters for en2 with a frequency of 100

GPIO.output(in1, GPIO.LOW)  # Set output to LOW
GPIO.output(in2, GPIO.LOW)  # Set output to LOW
GPIO.output(in3, GPIO.LOW)  # Set output to LOW
GPIO.output(in4, GPIO.LOW)  # Set output to LOW

while True:
    ret, frame = cap.read()  # Capture image from webcam and store it in ret (boolean) and frame (image) variables
    low_b = np.uint8([110, 110, 110])  # Set up lower color range
    high_b = np.uint8([0, 0, 0])  # Set up upper color range
    mask = cv2.inRange(frame, high_b,
                       low_b)  # Use inRange function to create a mask with input being the frame, and color thresholds
    contours, hierarchy = cv2.findContours(mask, 1,
                                           cv2.CHAIN_APPROX_NONE)  # Contour detection function, with input as the mask. 'contours' is a list of contours, 'hierarchy' is a list of vectors.

    if len(contours) > 0:  # If the number of contours is greater than 0, a line is detected
        key = cv2.contourArea  # Calculate the area of the contours
        c = max(contours, key=cv2.contourArea)  # Calculate the largest contour area in the frame
        cv2.drawContours(frame, c, -1, (0, 255, 0),
                         3)  # Draw the contour on the frame based on the largest contour area; -1 means draw all contours. Set color and thickness.
        M = cv2.moments(c)  # Calculate the center of mass (moments) from the largest contour
        if M["m00"] != 0:
            cx = int(M['m10'] / M['m00'])  # Calculate the centroid (center) using a formula
            cy = int(M['m01'] / M['m00'])  # Calculate the centroid (center) using a formula
            print("CX: " + str(cx) + "  CY: " + str(cy))  # Output the centroid coordinates

            if cx <= 40:  # If the x-coordinate of the centroid is less than or equal to 40, the car turns left
                print("Turn Left")
                p1.start(75)  # Start PWM with a duty cycle of 75
                p2.start(80)  # Start PWM with a duty cycle of 80
                GPIO.output(in1, GPIO.LOW)  # Set output to control the motor
                GPIO.output(in2, GPIO.HIGH)
                GPIO.output(in3, GPIO.HIGH)
                GPIO.output(in4, GPIO.LOW)

            if 40 < cx < 120:  # If the x-coordinate of the centroid is between 40 and 120, the car moves straight
                print("On Track!")
                p1.start(65)  # Start PWM with a duty cycle of 65
                p2.start(70)  # Start PWM with a duty cycle of 70
                GPIO.output(in1, GPIO.LOW)  # Set output to control the motor
                GPIO.output(in2, GPIO.HIGH)
                GPIO.output(in3, GPIO.LOW)
                GPIO.output(in4, GPIO.HIGH)

            if cx >= 120:  # If the x-coordinate of the centroid is greater than or equal to 120, the car turns right
                print("Turn Right")
                p1.start(75)  # Start PWM with a duty cycle of 75
                p2.start(80)  # Start PWM with a duty cycle of 80
                GPIO.output(in1, GPIO.HIGH)  # Set output to control the motor
                GPIO.output(in2, GPIO.LOW)
                GPIO.output(in3, GPIO.LOW)
                GPIO.output(in4, GPIO.HIGH)

            cv2.circle(frame, (cx, cy), 5, (255, 255, 255),
                       -1)  # Draw a circle at the centroid on the frame, with a radius of 5 pixels
    else:
        print("I don't see the line")
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.LOW)
        GPIO.output(in3, GPIO.LOW)
        GPIO.output(in4, GPIO.LOW)

    cv2.imshow("Mask", mask)  # Display the mask
    cv2.imshow("Frame", frame)  # Display the frame

    if cv2.waitKey(1) & 0xff == ord('q'):  # 1 is the time in ms, 'q' is to quit
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.LOW)
        GPIO.output(in3, GPIO.LOW)
        GPIO.output(in4, GPIO.LOW)
        break

cap.release()
cv2.destroyAllWindows()
