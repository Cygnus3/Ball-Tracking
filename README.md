# Ball-Tracking

Real-time ball tracking system for an Autonomous Mobile Robot (AMR) using OpenCV. 
Detects and tracks a moving red ball from video input and outputs its center coordinates (x, y) and radius for every frame, enabling closed-loop control.

**How it works:**

Rescale – Frame is downscaled to 50% for performance

HSV Conversion – Frame converted to HSV for reliable color-based masking

Color Masking – Dual HSV range used for red (since red wraps around the hue spectrum at 0° and 180°)

Contour Detection – Contours found on the binary mask

Ball Localization – Minimum enclosing circle gives center (x, y) and radius

Overlay – Circle and coordinates drawn on the original frame


**Output :**

Green circle drawn around the ball
Center coordinates and radius printed to console and overlaid on frame

**Requirements:**
pip install opencv-python numpy

**Usage:**

Update the video path in the code and run:
     "ball tracking.py"
     Press d to exit.

**NOTE** : Video file not included. Place your input video at the path specified in the code.

