# Ball-Tracking

Real-time ball tracking system for an Autonomous Mobile Robot (AMR) using OpenCV. Detects and tracks a moving red ball from camera/video input and outputs its center coordinates (x, y) and radius for every frame, enabling closed-loop control.

**Files:**

ball tracking.py — Video 1: Basic ball tracking under good lighting

ball tracking_vid2.py — Video 2 (Bonus): Ball tracking with variable lighting, background noise, and occlusion handling

**How it works:**

Rescale – Frame is downscaled to 50% for performance

HSV Conversion – Frame converted to HSV for reliable color-based masking

Color Masking – Dual HSV range used for red (since red wraps around the hue spectrum at 0° and 180°)

Morphological Operations (Video 2) – Erosion removes thin line noise, dilation restores ball shape

Contour Detection – Contours found on the binary mask

Ball Localization – Minimum enclosing circle gives center (x, y) and radius

Occlusion Handling (Video 2) – Last known position displayed in red when ball is hidden behind an obstacle



**Output:**

Green circle: actively detected ball with center coordinates and radius

Red circle (Video 2): last known position when ball is occluded

Coordinates and radius printed to console each frame and also overlaied on the frame.

**Requirements:** 
       pip install opencv-python numpy
       
**Usage:**
       Update the video path in the code and run:

Press d to exit.

Note: Video files not included. Place your input videos at the paths specified in the code.
