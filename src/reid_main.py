# ✅ File: src/reid_main.py
import cv2
import os
import sys
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.detector import PlayerDetector
from helpers.draw import draw_boxes
from src.tracker import PlayerTracker

def main():
    video_path = 'input/15sec_input_720p.mp4'
    model_path = 'input/best.pt'
    output_path = 'output/reid_output.mp4'

    cap = cv2.VideoCapture(video_path)
    width, height = 480, 270
    fps = cap.get(cv2.CAP_PROP_FPS) or 25.0

    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    detector = PlayerDetector(model_path)
    tracker = PlayerTracker()

    frame_count = 0
    start_time = time.time()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame_count += 1
        frame = cv2.resize(frame, (width, height))

        detections = detector.detect(frame)
        tracks = tracker.update(detections,frame)

        annotated = draw_boxes(frame.copy(), tracks, frame_number=frame_count)
        out.write(annotated)

    cap.release()
    out.release()
    print(f"✅ Done. Time: {time.time() - start_time:.2f}s | Frames: {frame_count}")

if __name__ == "__main__":
    main()
