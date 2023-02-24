#use monte screen recorder API
#https://www.youtube.com/watch?v=-rWG_jQnLCY

import subprocess
import time


def start_record():
    # Set the dimensions and frame rate of the screen capture
    width = 1920
    height = 1080
    framerate = 30

    # Set the path to the ffmpeg executable
    ffmpeg_path = '/path/to/ffmpeg'

    # Set the path to save the screen capture video
    output_path = '/path/to/output.mp4'

    # Set the display to capture (e.g. :0 for the first display)
    display = ':0'

    # Start the screen capture using ffmpeg
    command = [ffmpeg_path, '-f', 'x11grab', '-s', f'{width}x{height}', '-r', str(framerate), '-i', display, '-c:v', 'libx264', '-crf', '0', '-preset', 'ultrafast', output_path]

    # ffmpeg_path, '-f', 'x11grab', '-s', f'1920x1080', '-r', '30', '-i', ':0', '-c:v', 'libx264', '-crf', '0', '-preset', 'ultrafast', output_path
    subprocess.run(command)

    print('Screen capture complete!')


def start_record2():
    # Set the duration of the recording in seconds
    duration = 60

    # Start the recording
    proc = subprocess.Popen(['ffmpeg', '-f', 'x11grab', '-s', '1920x1080', '-i', ':0.0', '-vcodec', 'libx264', 'output.mp4'])

    # Wait for the specified duration
    time.sleep(duration)

    # Stop the recording
    proc.terminate()







import cv2

def screen_record2():
    # Set up the video capture
    capture = cv2.VideoCapture(0)

    # Set the width and height of the capture
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

    # Set the frame rate of the capture
    capture.set(cv2.CAP_PROP_FPS, 60)

    # Create a VideoWriter object to write the video to a file
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 60.0, (1920, 1080))

    # Start capturing frames from the screen
    while True:
        # Capture a frame from the screen
        ret, frame = capture.read()

        # Write the frame to the output file
        out.write(frame)

        # Show the frame on the screen (optional)
        cv2.imshow('Screen', frame)

        # Check for user input to stop the recording
        key = cv2.waitKey(1)
        if key == 27:  # Escape key
            break

    # Release the VideoCapture and VideoWriter objects
    capture.release()
    out.release()

    # Close all windows
    cv2.destroyAllWindows()


