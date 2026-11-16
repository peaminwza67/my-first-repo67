price = float(input("กรอกราคาเต็มของสินค้า (บาท): "))
discount_percent = float(input("กรอกเปอร์เซ็นต์ส่วนลด (%): "))

discount = price * (discount_percent / 100)
vat = (price - discount) * 0.07
net_price = (price - discount) + vat

print(f"\nราคาเต็ม: {price:.2f} บาท")
print(f"เปอร์เซ็นต์ส่วนลด: {discount_percent:.2f}%")
print(f"ส่วนลด: {discount:.2f} บาท")
print(f"VAT 7%: {vat:.2f} บาท")
print(f"ราคาสุทธิที่ต้องจ่าย: {net_price:.2f} บาท")
