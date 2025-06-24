# ✅ File: helpers/draw.py
import cv2
import colorsys
import hashlib

# Generate a consistent color for each ID using a hash
def get_color_by_id(track_id):
    hue = (hash(track_id) % 360) / 360.0
    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
    return int(r * 255), int(g * 255), int(b * 255)

def draw_boxes(frame, tracks, frame_number=None, fps=None):
    for track in tracks:
        if not track.is_confirmed():
            continue

        track_id = track.track_id
        ltrb = track.to_ltrb()
        x1, y1, x2, y2 = map(int, ltrb)
        color = get_color_by_id(track_id)

        # Draw thicker rectangle
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, thickness=3)

        # Label text
        label = f"Player {track_id}"

        # Get text size for background box
        (text_w, text_h), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2)
        label_bg_x1 = x1
        label_bg_y1 = y1 - text_h - 10
        label_bg_x2 = x1 + text_w + 6
        label_bg_y2 = y1

        # Add translucent background for text
        overlay = frame.copy()
        cv2.rectangle(overlay, (label_bg_x1, label_bg_y1), (label_bg_x2, label_bg_y2), color, -1)
        alpha = 0.6
        cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0, frame)

        # Put label above the box
        cv2.putText(frame, label, (x1 + 3, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)

    # Add FPS and Frame info if provided
    if frame_number is not None:
        text = f"Frame: {frame_number}"
        cv2.putText(frame, text, (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)

    if fps is not None:
        text = f"FPS: {fps:.1f}"
        cv2.putText(frame, text, (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)

    return frame
