import cv2
import time

def video2frames(
    video_path, 
    frame_start = 0,
    frame_count = None,
    frame_stride = 1,
    logging=False):
    """Generator yields image frames given a video path.

    `PEP 484`_ type annotations are supported. If attribute, parameter, and
    return types are annotated according to `PEP 484`_, they do not need to be
    included in the docstring:

    Args:
        video_path (pathlike): path to a video file

        frame_start: frame number to yield first. Defaults to 0.

        frame_count: number of frames to yield total. Defaults None (end of video)

        frame_stride: yield every Nth frame. Defaults to 1.

        logging (bool, optional): enable verbose console logging. Defaults to False.

    Returns:
        yields image frames

    """
    cap = cv2.VideoCapture(video_path)
    f = 0
    while(cap.isOpened()):
        yf = f - frame_start

        f += 1
        
        ret, frame = cap.read()


        if yf < 0 or yf % frame_stride != 0:
            continue

        yf /= frame_stride

        if frame_count is not None and yf >= frame_count:
            break

        t = time.time()
        
        
        if not ret:
            break
            
        if logging:
            print('read frame {} and yield as {} in {}s'.format(str(f), str(yf), str(time.time() - t)))
        
        yield frame
        
    cap.release()

