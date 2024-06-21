import cv2
import torch
import numpy as np 

# Set the device to CPU or CUDA if available
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Load the pre-trained YOLOv5 model (e.g., YOLOv5s)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
model.to(device).eval()

# Start the webcam
cap = cv2.VideoCapture("vid1.mp4")
area1=[(559,236),(1455,234),(1566,715),(553,717)]

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame from BGR to RGB (required for YOLOv5)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Perform inference
    results = model(frame)

    # Filter results for "person" class (class index 0 for COCO dataset)
    person_results = results.pred[0][results.pred[0][:, -1] == 0]  # Class index 0 for "person"


    print(person_results)
    # Draw bounding boxes for "person" class detections
    for person in person_results:
        bbox = person[:4].int().cpu().numpy()
        conf = person[4].cpu().numpy()
        center_x = int(bbox[0] + bbox[2]) // 2
        center_y = int(bbox[1] + bbox[3]) // 2
        roiresult = cv2.pointPolygonTest(np.array(area1,np.int32),(center_x,center_y),False)
        print(roiresult)   
        if roiresult >=0:     
            cv2.circle(frame,(center_x,center_y),5,(0,255,0),-1)
            cv2.rectangle(frame, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (0, 255, 0), 2)
            cv2.putText(frame, f'Person: {conf:.2f}', (bbox[0], bbox[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Convert the frame back to BGR for displaying with OpenCV
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    cv2.polylines(frame,[np.array(area1,np.int32)],True,(0,0,255),2)

    # Display the frame with person detections
    cv2.imshow('YOLOv5 Person Detection', frame)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close the window
cap.release()
cv2.destroyAllWindows()
