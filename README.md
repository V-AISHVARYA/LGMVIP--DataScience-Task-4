# **LGMVIP-DataScience-Task-4**
**IMAGE TO PENCIL SKETCH WITH PYTHON**


This repository contains a Python project that focuses on converting RGB images into pencil sketches. The idea behind this project is to provide a simple and intuitive tool that can transform regular images into artistic pencil sketches.
This project serves to work using divide function from cv2 Library in Python.

**STEPS INVOLVED:**  
Image Loading: The RGB image is loaded using a popular image processing library.  
Grayscale Conversion: The RGB image is converted into grayscale to simplify the processing.  
Inversion: The grayscale image is inverted to simulate the appearance of a pencil sketch.  
Blur: A Gaussian blur is applied to the inverted grayscale image to achieve a smoother, more artistic look.  
Blend: The blurred inverted grayscale image is blended with the original grayscale image to introduce pencil-like textures.  
Pencil Sketch:The blende image is the pencil sketch generated,artistically interpreting the original image.  

PREREQISITES:
>python latest version installed  
>vs code(with python extension installed) or any IDE (should support cv2 library)  
>Opencv Library installed in your python environment  
To Install:pip install opencv-python  

