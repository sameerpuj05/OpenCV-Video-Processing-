# Code to Measure time taken by program to execute.
# from asyncio.windows_events import NULL
import time

# import the opencv library and numpy library
import cv2
import numpy as np

# define a video capture object
vid = cv2.VideoCapture(0)
avg_fps=0
loop_count=0

while(True):
	# store starting time
	begin = time.time()

	# Capture the video frame
	# by frame
	ret, frame = vid.read()

	frame = cv2.resize(frame, (640, 480), fx = 0, fy = 0,
                         interpolation = cv2.INTER_CUBIC)
 

	# Convert to grayscale.
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	# Blur using 5 * 5 kernel.
	gray_blurred = cv2.blur(gray, (5, 5))

	# Apply Hough transform on the blurred image.
	detected_circles = cv2.HoughCircles(gray_blurred, 
					cv2.HOUGH_GRADIENT, 1, 20, param1 = 50,
				param2 = 30, minRadius = 60, maxRadius = 80)
	
	# Draw circles that are detected.
	if detected_circles is not None:
	
		# Convert the circle parameters a, b and r to integers.
		detected_circles = np.uint16(np.around(detected_circles))
	
		for pt in detected_circles[0, :]:
			a, b, r = pt[0], pt[1], pt[2]
	
			# Draw the circumference of the circle.
			cv2.circle(frame, (a, b), r, (0, 255, 0), 2)
	
			# Draw a small circle (of radius 1) to show the center.
			cv2.circle(frame, (a, b), 1, (0, 0, 255), 3)
			cv2.imshow("Detected Circle", frame)
	
	# else: Display Blurred Gray Image
	else:
		cv2.imshow("Detected Circle", gray_blurred)

	# the 'q' button is set as the
	# quitting button you may use any
	# desired button of your choice
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

	# store end time
	end = time.time()

	# print average fps approx after every 1 sec 
	loop_count=loop_count+1
	avg_fps=( (avg_fps*(loop_count-1) )+ ( 1/(end-begin) ) )/loop_count
	if loop_count>30:
		loop_count=1
		print(f"Average processing FPS is {round(avg_fps)} ")

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()