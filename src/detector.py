from ultralytics import YOLO
import torch

class PlayerDetector:
    def __init__(self, model_path):
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.model = YOLO(model_path)
        self.model.to(self.device)

    def detect(self, frame):
        results = self.model.predict(source=frame, device=self.device, verbose=False)[0]

        detections = []
        for box in results.boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            w = x2 - x1
            h = y2 - y1
            conf = float(box.conf[0])
            cls = int(box.cls[0]) if box.cls is not None else 0

            if conf > 0.5:
                detections.append([[float(x1), float(y1), float(w), float(h)], conf, cls])

        return detections
