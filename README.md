# Line Following Robot using COMPUTER VISION
  The project focuses on developing an autonomous system where a vehicle can detect and follow a path using image processing technology. With Raspberry Pi as the main processor, the system utilizes a camera to capture images from the environment. Through computer vision algorithms, such as line detection and analysis, the vehicle identifies the position of the path and adjusts its direction to stay on course. This technology has broad potential applications in areas like automation, mobile robotics, and intelligent transportation systems.
# Hardware
  * Raspberry Pi 3B+
  * Wedcam Logitech 720p
  * L298N driver motor ...
#Software
  * Raspberry Pi OS: Linux OS based
  * Geany IDE
# Processing algorithm

1. Capture image from the camera: The camera mounted on the Raspberry Pi continuously captures images.

2. Convert color space: The captured image is typically in RGB (Red, Green, Blue) format. To make color processing easier, the image can be converted to the HSV (Hue, Saturation, Value) color space. The HSV color space is more convenient for detecting colors because the hue (color) and saturation (intensity of color) are separated from brightness (value).

3. Color thresholding: Using OpenCV, you can define the color range corresponding to the line, such as white or yellow. By applying the cv2.inRange() function, a color threshold is set to filter out only the pixels that match the specified line color. Any pixels within this color range will be retained, while others will be discarded (turned black).

4. Create a mask: The result of the thresholding is a binary image where the line is preserved (white), and the surrounding areas (black) are discarded. This mask isolates the line in the image.

5. Detect and locate the line: After obtaining the binary image, you can use techniques like finding contours or applying the Hough Line Transform algorithm to accurately detect the shape and position of the line.

6. Adjust direction: Based on the position of the line in the frame, the vehicle will adjust its direction. For example, if the line appears on the left side of the frame, the vehicle knows it needs to turn left, and vice versa.
# Diagram
![image](https://github.com/user-attachments/assets/2827a8e6-e9e2-4b06-88a8-40bd66877731)
# Final product
![image](https://github.com/user-attachments/assets/4f5d167e-b2b5-41b0-97f3-0e46d5c04484)
# Video demo
https://github.com/user-attachments/assets/4d807aad-5caa-452e-bb35-274d636bba1e




