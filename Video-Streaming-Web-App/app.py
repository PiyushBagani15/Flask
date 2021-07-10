from flask import Flask,render_template,Response
import cv2

app=Flask(__name__)
camera=cv2.VideoCapture(0)

def generate_frames():
    while True:
            
        ## read the camera frame
        success,frame=camera.read()
        if not success:
            break
        else:
            ret,buffer=cv2.imencode('.jpg',frame) #encode
            frame=buffer.tobytes() #converting in bytes The bytes() method returns a immutable bytes object initialized with the given size and data.
                                                    
        ### Here we use the yield instead of return because it has to come multiple times to pass the image
        yield(b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame') # this we know beca
    #use of documentation
if __name__=="__main__":
    app.run(debug=True)

   
