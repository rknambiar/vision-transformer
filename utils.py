import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import ImageGrid

def show_numpy_image(image, fig_size):
    fig = plt.figure(figsize=fig_size)
    plt.imshow(image)
    plt.axis('off')
    plt.show()

def show_numpy_image_grid(images, fig_size, rows, cols):
    """Show images as a grid"""

    if (images.shape[0] != rows * cols): 
        raise ValueError("Number of rows * cols should be equal to the number of elements")

    fig = plt.figure(figsize=(4., 4.))
    grid = ImageGrid(fig, 111,  # similar to subplot(111)
                    nrows_ncols=(rows, cols),  # creates 2x2 grid of axes
                    axes_pad=0.1,  # pad between axes in inch.
                    )

    for x, ax in enumerate(grid):
        # Iterating over the grid returns the Axes.
        ax.imshow(images[x])
    
    plt.axis('off')
    plt.show()