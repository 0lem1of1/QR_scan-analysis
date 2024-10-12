import cv2
from pyzbar.pyzbar import decode
from datetime import datetime

def decode_qr(frame):
    decoded_objects = decode(frame)
    product_list = []

    for obj in decoded_objects:
        qr_data = obj.data.decode('utf-8')
        name, ex_date = qr_data.split(',')

        #parsing ex_date as a datetime object
        ex_date = datetime.strptime(ex_date, '%Y-%m-%d')

        product_list.append((name, ex_date))

    return product_list

def sort_products_by_expiry(products):
    return sorted(products, key=lambda x: x[1])

cap = #considering this as webcam capture

all_products = []

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Failed to capture video frame.")
        break

    products_in_frame = decode_qr(frame)
    if products_in_frame:
        all_products.extend(products_in_frame)
        print("Detected Products:", products_in_frame)

    cv2.imshow("QR Code Scanner", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

sorted_products = sort_products_by_expiry(all_products)

print("\nSorted Products by Expiry Date:")
for product in sorted_products:
    print(f"Product: {product[0]}, Expiry Date: {product[1].strftime('%Y-%m-%d')}")

cap.release()
cv2.destroyAllWindows()
