price = float(input("กรอกราคาเต็มของสินค้า (บาท): "))
  discount_percent = float(input("กรอกเปอร์เซ็นต์ส่วนลด (%): "))

  if price < 0 or not (0 <= discount_percent <= 100):
    print("ข้อผิดพลาด: กรุณากรอกราคาตั้งแต่ 0 ขึ้นไป และส่วนลดระหว่าง 0 - 100%")
  else:
    discount = price * (discount_percent / 100)
    price_after_discount = price - discount
    vat = price_after_discount * 0.07
    net_price = price_after_discount + vat

    print("\n--- สรุปรายการ ---")
    print(f"ราคาเต็ม: {price:,.2f} บาท")
    print(f"ส่วนลด ({discount_percent:.2f}%): {discount:,.2f} บาท")
    print(f"ราคาหลังหักส่วนลด: {price_after_discount:,.2f} บาท")
    print(f"VAT 7%: {vat:,.2f} บาท")
    print(f"ราคาสุทธิที่ต้องจ่าย: {net_price:,.2f} บาท")
