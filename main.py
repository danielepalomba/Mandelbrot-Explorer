import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z**2 + c
        n += 1
    if n == max_iter:
        return max_iter
    return n + 1 - np.log(np.log2(abs(z)))

def generate_mandelbrot(width, height, xmin, xmax, ymin, ymax, max_iter):
    image = np.zeros((width, height))

    for x in range(width):
        for y in range(height):
            zx = xmin + (xmax - xmin) * x / (width - 1)
            zy = ymin + (ymax - ymin) * y / (height - 1)
            c = complex(zx, zy)
            color = mandelbrot(c, max_iter)
            image[x, y] = color

    return image

def plot_mandelbrot(image):
    plt.imshow(image, cmap='hot', extent=(-2, 1, -1, 1))
    plt.colorbar()
    plt.title('Insieme di Mandelbrot')
    plt.show()

width, height = 800, 800
xmin, xmax = -2, 1
ymin, ymax = -1, 1
max_iter = 100

mandelbrot_image = generate_mandelbrot(width, height, xmin, xmax, ymin, ymax, max_iter)
plot_mandelbrot(mandelbrot_image)
