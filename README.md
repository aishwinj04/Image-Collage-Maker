### Image Collage Maker

This Python script creates a collage of images by arranging them in a grid with margins. It reads images from a directory given that all the images are of the same size, and arranges them into a grid. The final collage is saved as a new image file.

### Features:
- In this version, all images must be the same size.
- Organizes images in a 2x3 grid (customizable by adjusting rows and columns).
- Adds margins between images for better spacing and appearance.
- Works with images in a specified directory (ignores `.DS_Store` files on macOS).
- Saves the final collage as a new image (`grid.JPG`).

### Prerequisites:
- Python 3.x
- OpenCV (`cv2`)
- NumPy
