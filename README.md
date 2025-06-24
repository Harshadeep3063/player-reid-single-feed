# Player Re-Identification in a Single Video Feed

## 🎯 Assignment Objective
Re-identify and track players in a single 15-second sports video using a YOLO-based object detector and DeepSORT tracker. The goal is to maintain consistent player IDs throughout the clip, even when players leave and re-enter the frame.

---

## 📂 Folder Structure
```
📦 **YOLOv11 Model**: [Download best.pt](https://drive.google.com/file/d/1DhuBuOU9hmHI8nadghFuCd6s56WJmewU/view?usp=drive_link)

player-reid-single-feed/
├── input/
│   ├── 15sec_input_720p.mp4         # Provided video
│
├── output/
│   └── fixed_output.mp4             # Final output with re-ID visualization
│
├── src/
│   ├── reid_main.py                # Main pipeline script
│   ├── detector.py                 # YOLOv8 detector wrapper
│   └── tracker.py                  # DeepSORT tracker (with MobileNet embedder)
│
├── helpers/
│   ├── draw.py                     # Utilities for drawing bounding boxes
│   └── __init__.py                 # Empty init for module structure
```

---

## 🚀 How to Run (in Google Colab)

### ✅ 1. Upload ZIP to Colab
- Upload `player-reid-single-feed.zip`
- Unzip and enter folder:
```python
!unzip -q player-reid-single-feed.zip -d player-reid-single-feed
%cd player-reid-single-feed/player-reid-single-feed
```

### ✅ 2. Install Dependencies
```python
!pip install ultralytics opencv-python deep_sort_realtime
```

### ✅ 3. Run the Code
```python
!python src/reid_main.py
```

### ✅ 4. View Output in Colab
```python
from IPython.display import HTML
from base64 import b64encode

mp4 = open("output/reid_output.mp4",'rb').read()
data_url = "data:video/mp4;base64," + b64encode(mp4).decode()
HTML(f'''
<video width=640 height=360 controls>
    <source src="{data_url}" type="video/mp4">
</video>
''')
```

---

## 🧠 Components

### 🔍 Detection: `best.pt`
- Custom fine-tuned YOLOv11 model
- Detects players and ball

### 🔄 Tracking: DeepSORT
- MobileNet embedder
- IOU-based association
- Maintains ID across frames & re-entries

### 🎨 Visualization: `helpers/draw.py`
- Player ID shown above head
- Fixed color palette
- Frame number and optional FPS overlay

---

## 📊 Output Example
- Video: `output/reid_output.mp4`
- FPS: ~7.9 (CPU) | Time: ~47s
- 375 frames processed
- Consistent tracking throughout

---

## ✅ Result Summary
| Requirement                        | Status |
|-----------------------------------|--------|
| Used provided video + model       | ✅     |
| Consistent player ID tracking     | ✅     |
| Visual clarity (labels, colors)   | ✅     |
| Code runs fully in Colab          | ✅     |
| Output video is correct & playable| ✅     |

---

## 🧑‍💻 Author
**Bandari Harshadeep Reddy**  
A Recent B.Tech Graduate – CSE (Data Science)  
CVR College of Engineering

---

## 📝 Notes
- Runtime can be further improved using YOLOv5s or frame skipping.
- `cv2.destroyAllWindows()` is skipped in Colab due to GUI limitations.
- Re-encoding with `ffmpeg` was used for clean playback.
