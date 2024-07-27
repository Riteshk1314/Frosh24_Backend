# import qrcode.image.svg
# factory = qrcode.image.svg.SvgPathFillImage
# svg_img=qrcode.make(444555, image_factory=factory)
# svg_img.save("444555.svg")
# import pyzbar.pyzbar as pyzbar
# import cv2 
# import numpy
# def scan():
#     i=0
#     cap=cv2.VideoCapture(0)
#     while i<4:
#         _,frame=cap.read()
#         decoded=pyzbar.decode(frame)
#         for obj in decoded:
#             print(obj.data)
#             i=i+1
#         cv2.imshow("QRCode",frame)
#         cv2.waitKey(5)
#         cv2.destroyAllWindows
        
# def qr_maker(value, registration_id):
#     factory = qrcode.image.svg.SvgPathFillImage
#     svg_img=qrcode.make(444555, image_factory=factory)
#     return(svg_img.save(f"{registration_id}.svg"))
# # scan()
