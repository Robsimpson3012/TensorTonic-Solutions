def iou(box_a, box_b):
    """
    Compute Intersection over Union of two bounding boxes.
    """
    box_a_area = (box_a[2] - box_a[0]) * (box_a[3] - box_a[1])
    box_b_area = (box_b[2] - box_b[0]) * (box_b[3] - box_b[1])

    max_xmin = max(box_a[0], box_b[0])
    min_xmax = min(box_a[2], box_b[2])
    max_ymin = max(box_a[1], box_b[1])
    min_ymax = min(box_a[3], box_b[3])

    interArea = max(0, min_xmax - max_xmin) * max(0, min_ymax - max_ymin)

    iou = interArea / float(box_a_area + box_b_area - interArea)
    return iou