
# import face_recognition
# import cv2
# import numpy as np
# import csv
# import os
# from datetime import datetime
 
# video_capture = cv2.VideoCapture(0)
 
# jobs_image = face_recognition.load_image_file("photos\jobs.webp")
# jobs_encoding = face_recognition.face_encodings(jobs_image)[0]
 
# ratan_tata_image = face_recognition.load_image_file("photos/tata.jpg")
# ratan_tata_encoding = face_recognition.face_encodings(ratan_tata_image)[0]
 
# sadmona_image = face_recognition.load_image_file("photos/sadmona.jpg")
# sadmona_encoding = face_recognition.face_encodings(sadmona_image)[0]
 
# tesla_image = face_recognition.load_image_file("photos/tesla.jpeg")
# tesla_encoding = face_recognition.face_encodings(tesla_image)[0]
 
# known_face_encoding = [
# jobs_encoding,
# ratan_tata_encoding,
# sadmona_encoding,
# tesla_encoding
# ]
 
# known_faces_names = [
# "jobs",
# "ratan tata",
# "sadmona",
# "tesla"
# ]
 
# students = known_faces_names.copy()
 
# face_locations = []
# face_encodings = []
# face_names = []
# s=True
 
 
# now = datetime.now()
# current_date = now.strftime("%Y-%m-%d")
 
 
 
# f = open(current_date+'.csv','w+',newline = '')
# lnwriter = csv.writer(f)
 
# while True:
#     _,frame = video_capture.read()
#     small_frame = cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
#     rgb_small_frame = small_frame[:,:,::-1]
#     if s:
#         face_locations = face_recognition.face_locations(rgb_small_frame)
#         face_encodings = face_recognition.face_encodings(rgb_small_frame,face_locations)
#         face_names = []
#         for face_encoding in face_encodings:
#             matches = face_recognition.compare_faces(known_face_encoding,face_encoding)
#             name=""
#             face_distance = face_recognition.face_distance(known_face_encoding,face_encoding)
#             best_match_index = np.argmin(face_distance)
#             if matches[best_match_index]:
#                 name = known_faces_names[best_match_index]
#                 print(name)
 
#             face_names.append(name)
#             if name in known_faces_names:
#                 font = cv2.FONT_HERSHEY_SIMPLEX
#                 bottomLeftCornerOfText = (10,100)
#                 fontScale              = 1.5
#                 fontColor              = (255,0,0)
#                 thickness              = 3
#                 lineType               = 2
 
#                 cv2.putText(frame,name+' Present', 
#                     bottomLeftCornerOfText, 
#                     font, 
#                     fontScale,
#                     fontColor,
#                     thickness,
#                     lineType)
 
#                 if name in students:
#                     students.remove(name)
#                     # print(students)
#                     current_time = now.strftime("%H-%M-%S")
#                     lnwriter.writerow([name,current_time])
#     cv2.imshow("attendence system",frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
 
# video_capture.release()
# cv2.destroyAllWindows()
# f.close()








# import face_recognition
# import cv2
# import numpy as np
# import csv
# import os
# from datetime import datetime
 
# video_capture = cv2.VideoCapture(0)
 
# jobs_image = face_recognition.load_image_file("photos/jobs.webp")
# jobs_encoding = face_recognition.face_encodings(jobs_image)[0]
 
# ratan_tata_image = face_recognition.load_image_file("photos/tata.jpg")
# ratan_tata_encoding = face_recognition.face_encodings(ratan_tata_image)[0]
 
# sadmona_image = face_recognition.load_image_file("photos/sadmona.jpg")
# sadmona_encoding = face_recognition.face_encodings(sadmona_image)[0]
 
# tesla_image = face_recognition.load_image_file("photos/tesla.jpeg")
# tesla_encoding = face_recognition.face_encodings(tesla_image)[0]
 
# known_face_encodings = [
#     jobs_encoding,
#     ratan_tata_encoding,
#     sadmona_encoding,
#     tesla_encoding
# ]
 
# known_face_names = [
#     "jobs",
#     "ratan tata",
#     "sadmona",
#     "tesla"
# ]
 
# students = known_face_names.copy()
 
# face_locations = []
# face_encodings = []
# face_names = []
# s = True
 
# now = datetime.now()
# current_date = now.strftime("%Y-%m-%d")
 
# f = open(current_date + '.csv', 'w+', newline='')
# lnwriter = csv.writer(f)
 
# while True:
#     _, frame = video_capture.read()
#     small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
#     rgb_small_frame = small_frame[:, :, ::-1]
    
#     if s:
#         # face_locations = face_recognition.face_locations(rgb_small_frame)
#         face_locations = [(top * 4, right * 4, bottom * 4, left * 4) for (top, right, bottom, left) in face_recognition.face_locations(rgb_small_frame)]

#         face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
#         face_names = []
        
#         for face_encoding in face_encodings:
#             matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
#             name = ""
#             face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
#             best_match_index = np.argmin(face_distances)
            
#             if matches[best_match_index]:
#                 name = known_face_names[best_match_index]
#                 # print(name)
 
#             face_names.append(name)
            
#             if name in known_face_names:
#                 font = cv2.FONT_HERSHEY_SIMPLEX
#                 bottomLeftCornerOfText = (10, 100)
#                 fontScale = 1.5
#                 fontColor = (255, 0, 0)
#                 thickness = 3
#                 lineType = 2
 
#                 cv2.putText(frame, name + ' Present',
#                             bottomLeftCornerOfText,
#                             font,
#                             fontScale,
#                             fontColor,
#                             thickness,
#                             lineType)
 
#                 if name in students:
#                     students.remove(name)
#                     # print(students)
#                     current_time = now.strftime("%H-%M-%S")
#                     lnwriter.writerow([name, current_time])
    
#     cv2.imshow("attendance system", frame)
    
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
 
# video_capture.release()
# cv2.destroyAllWindows()
# f.close()



import cv2
import numpy as np
import csv
import face_recognition
from datetime import datetime

# Load the reference images
jobs_image = face_recognition.load_image_file('photos/jobs.webp')
jobs_encoding = face_recognition.face_encodings(jobs_image)[0]

ratan_tata_image = face_recognition.load_image_file('photos/tata.jpg')
ratan_tata_encoding = face_recognition.face_encodings(ratan_tata_image)[0]

sadmona_image = face_recognition.load_image_file('photos/sadmona.jpg')
sadmona_encoding = face_recognition.face_encodings(sadmona_image)[0]

tesla_image = face_recognition.load_image_file('photos/ram.jpeg')
tesla_encoding = face_recognition.face_encodings(tesla_image)[0]

known_face_encodings = [
    jobs_encoding,
    ratan_tata_encoding,
    sadmona_encoding,
    tesla_encoding
]

known_face_names = [
    "jobs",
    "Amit Chaudhary",
    "sadmona",
    "Chirag"
]

# Open the video capture
video_capture = cv2.VideoCapture(0)

# Create a CSV file for storing face recognition results
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")
csv_file = open(current_date + '.csv', 'w+', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Name', 'Time'])

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # Convert the frame to grayscale for face detection
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    face_locations = face_recognition.face_locations(gray_frame)

    # Encode faces in the frame
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    # Initialize an empty list to store recognized names
    face_names = []

    for face_encoding in face_encodings:
        # Compare face encoding with known encodings
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        # Find the best match
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)

        # If a match is found, use the name of the known face
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        face_names.append(name)
        

    # Display the recognized names on the frame
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        # Save the recognized name and timestamp to the CSV file
        csv_writer.writerow([name, datetime.now().strftime("%H:%M:%S")])

    # Display the resulting frame
    cv2.imshow('Video', frame)



    if matches[best_match_index]:
       print("done")
       break
    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
       
        break

# Release the video capture and close the CSV file
video_capture.release()
csv_file.close()

# Destroy all OpenCV windows
cv2.destroyAllWindows()
