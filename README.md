# Color_task

Task:- Find the Dominant color along with it, Find the color of Border in the image.

Approach:- Used color intensity of each pixel to find dominant & border color of Image.


1. **Dominant color approach**

      *The color image is 3d matrix made up of 3 color panels i.e Red,Green,Blue.So here each pixel hold array of intensities of rgb values in range from (0,255) i.e [red_value,green_value,blue_value]. So I created a color list, traversed over all pixel of image and then converted each pixel array of intensities to color code,After appending to list found most dominant color by maximum number of times particular color appear in list.


2. **Border color approach**

      *For border color of image,I created a list and stored color code from pixel intensity of 4 border strip/sides surrounding image and took the most dominant color by number of times particular color appear in list. 


**Step for Execution:-**

  1. Create a Virtual Environment
  2. Install requirements using pip install -r requirements.txt
  3. Run Flask app using "python app.py"
  4. Post request at "/run endpoint by running testing.py.


**Deployement:-**

It can be done on pythonanywhere cloud server.
