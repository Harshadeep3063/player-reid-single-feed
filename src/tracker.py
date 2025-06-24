from deep_sort_realtime.deepsort_tracker import DeepSort

class PlayerTracker:
    def __init__(self):
        self.tracker = DeepSort(
            max_age=30,
            embedder="mobilenet", 
            half=True,
            bgr=True
        )

    def update(self, detections, frame):
        return self.tracker.update_tracks(detections, frame=frame)
