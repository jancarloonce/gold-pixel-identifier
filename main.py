import cv2
import numpy as np

def is_gold_color(pixel):
    # Define the range of gold color in RGB
    lower_gold = np.array([200, 150, 0], dtype=np.uint8)
    upper_gold = np.array([255, 200, 50], dtype=np.uint8)

    # Check if the pixel is within the defined range
    return np.all(np.logical_and(pixel >= lower_gold, pixel <= upper_gold))

def detect_gold_color_in_video():
    # Open the camera (default camera index is usually 0)
    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Convert the frame from BGR to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Iterate through each pixel and check if it's gold color
        height, width, _ = frame.shape
        gold_pixels = 0

        for i in range(height):
            for j in range(width):
                pixel = frame_rgb[i, j, :]
                if is_gold_color(pixel):
                    gold_pixels += 1
                    # Optionally, you can mark or visualize the gold pixels in the frame
                    frame[i, j, :] = [0, 255, 0]  # Set the pixel to green

        # Display the result
        cv2.imshow("Gold Color Detection", frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close all windows
    cap.release()
    cv2.destroyAllWindows()

    print(f"Number of gold pixels: {gold_pixels}")

# Call the function to start detecting gold color in the camera video
detect_gold_color_in_video()
