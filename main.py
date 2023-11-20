import cv2

def show_webcam():
    # Open the default camera
    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Display the resulting frame
        cv2.imshow('Webcam Feed', frame)

        # Break the loop when the user presses the 'ESC' key
        if cv2.waitKey(1) == 27 :
            break

    # Release the camera and close the window
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    show_webcam()