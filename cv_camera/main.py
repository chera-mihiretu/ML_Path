import cv2

# Initialize video capture
cap = cv2.VideoCapture(0)  # Use 0 for the default camera
ESC_KEY = 27  # Escape key


while True:
    ret, frame = cap.read()  # Capture frame
    if not ret:  # Check if frame capture was successful
        print("Error: Could not read frame.")
        break
    frame = cv2.flip(frame, 1)
    frame_copy = frame.copy()  # Make a copy of the frame

    cv2.imshow('Input', frame_copy)  # Display the frame

    if cv2.waitKey(1) & 0xFF == ESC_KEY:  # Exit if ESC is pressed
        break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()
