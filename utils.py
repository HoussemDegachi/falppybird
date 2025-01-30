
def remove_extention(path):
    return path.split(".")[0]

def get_rect_border(rect, x_thickness, y_thickness):
    return (rect.left - x_thickness, rect.top - y_thickness, rect.width + x_thickness * 2, rect.height + y_thickness * 2 )