import cv2
import numpy
import sys

threshold_value = 0;
threshold_type = 3;
max_value = 255;
max_type = 4;
max_BINARY_value = 255;

src=None
src_gray=None
dst=None
po1=None
img1=None
po2=None
rect=None
img=None
roiImg=None



window_name = "Threshold Demo";
window_result = "Result";


trackbar_type = "Type: \n 0: Binary \n 1: Binary Inverted \n 2: Truncate \n 3: To Zero \n 4: To Zero Inverted";
trackbar_value = "Value";

drag = 0;
select_flag = 0;

def Threshold_Demo( x ):
    global dst
    #probar con adaptive gaussian thresold
    ret,dst =cv2.threshold( src_gray, threshold_value, max_BINARY_value,threshold_type);

    if(select_flag == 1):
        img1 = dst.clone();
        cv2.rectangle(img1, po1, po2, cv2.RGB(255, 0, 0), 3, 8, 0);
        cv2.imshow(window_name,img1);
    else:
        cv2.imshow( window_name,dst);

def mouseHandler( event,  x,  y,  flags, param):
    if (event == cv2.EVENT_LBUTTONDOWN and not(drag)):
        #/* left button clicked. ROI selection begins */
        po1 = cv2.Point(x, y);
        drag = 1;


    if (event ==cv2.EVENT_MOUSEMOVE and drag):
    #/* mouse dragged. ROI being selected */
        img1 = dst.clone();
        po2 = cv2.Point(x, y);
        cv2.rectangle(img1, po1, po2, cv2.RGB(255, 0, 0), 3, 8, 0);
        cv2.imshow(window_name, img1);

    if (event == cv2.EVENT_LBUTTONUP and drag):

        po2 = cv2.Point(x, y);
        rect = cv2.Rect(po1.x,po1.y,x-po1.x,y-po1.y);
        drag = 0;
        roiImg = dst[po1.y:y,po1.x:x];


    if (event == cv2.EVENT_LBUTTONUP):
    #/* ROI selected */
        select_flag = 1;
        drag = 0;




def main(argv ):
    global src_gray

    #VideoCapture cap = VideoCapture(0); /* Start webcam */

    #VideoCapture cap = VideoCapture("rtsp://admin:labdei2015@192.168.4.108:554/cam/realmonitor?channel=1&subtype=2");


    #cap >> src;
    src= cv2.imread("/home/patentes/Escritorio/ReposCurso/tallerDeProcesamientoDeImagnes/SACD/images/img36.jpg", 3);

    #/// Convert the image to Gray
    src_gray= cv2.cvtColor( src, cv2.COLOR_BGR2GRAY );

    #/// Create a window to display results
    cv2.namedWindow( window_name, cv2.WINDOW_AUTOSIZE );

    
    #/// Create Trackbar to choose type of Threshold
    cv2.createTrackbar( trackbar_type,
    window_name, threshold_type,
    max_type, Threshold_Demo );

    cv2.createTrackbar( trackbar_value,
    window_name, threshold_value,
    max_value, Threshold_Demo );

    #/// Call the function to initialize
    dst=src_gray;
    Threshold_Demo(0);

    #/// Wait until user finishes program
    while(1):
        #//  cap >> src;

        cv2.setMouseCallback(window_name, mouseHandler);
        src_gray = cv2.cvtColor( src, cv2.COLOR_BGR2GRAY );
        Threshold_Demo(0);





        c = cv2.waitKey( 20 );
        if( c == 114 and select_flag == 1 ):
            cv2.imwrite("roiImg.jpg", roiImg);
            """system("ssocr -d -1 -T --charset=decimal roiImg.jpg");


            fp = popen("ssocr -d -1 -T --charset=decimal roiImg.jpg", "r");
            while (fgets(var, sizeof(var), fp) != NULL)
            {
            //prf("%s", var);
            }
            pclose(fp);

            putText(roiImg, var, cvPo(30,30),FONT_HERSHEY_COMPLEX_SMALL, 0.8, cvScalar(200,200,250), 1, AA);
            """
            cv2.imshow( window_result, roiImg);


        if( c == 27 ):
            break;

if __name__ == '__main__':
    main(sys.argv[1:])
