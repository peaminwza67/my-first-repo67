def calculate_price(price, discount_percent, vat_percent=7):
    if price < 0 or not 0 <= discount_percent <= 100 or vat_percent < 0:
        raise ValueError("กรุณาตรวจสอบราคาและเปอร์เซ็นต์ที่ระบุ")

    discount = price * discount_percent / 100
    price_after_discount = price - discount
    vat = price_after_discount * vat_percent / 100
    total = price_after_discount + vat

    return discount, price_after_discount, vat, total


discount, discounted_price, vat, total = calculate_price(1000, 20)

print(f"ส่วนลด: {discount:.2f} บาท")
print(f"ราคาหลังหักส่วนลด: {discounted_price:.2f} บาท")
print(f"VAT: {vat:.2f} บาท")
print(f"ราคาสุทธิ: {total:.2f} บาท")
