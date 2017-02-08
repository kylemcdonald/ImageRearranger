import numpy as np

def map_range(x, in_min, in_max, out_min, out_max):
    return out_min + (out_max - out_min) * (x - in_min) / (in_max - in_min)

def plot_images(images, xy, w=None, h=None, blend=np.maximum, canvas_shape=(512, 512), fill=0):    
    if images.ndim == 2:
        side = int(np.sqrt(len(images[0])))
        h = side if h is None else h
        w = side if w is None else w
        images = images.reshape(-1, h, w)
    else:
        h = images.shape[1]
        w = images.shape[2]
    
    min_xy = np.amin(xy, 0)
    max_xy = np.amax(xy, 0)
    
    min_canvas = np.array((0, 0))
    max_canvas = np.array((canvas_shape[0] - h, canvas_shape[1] - w))
    
    canvas = np.full(canvas_shape, fill, dtype=np.uint8)
    for image, pos in zip(images, xy):
        x_off, y_off = map_range(pos, min_xy, max_xy, min_canvas, max_canvas).astype(int)
        for y in range(0, h):
            cy = y_off + y
            for x in range(0, w):
                cx = x_off + x
                canvas[cy, cx] = blend(canvas[cy, cx], image[y, x])

    return canvas