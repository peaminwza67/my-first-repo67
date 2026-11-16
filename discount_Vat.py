def calculate_price(price, discount_percent, vat_percent=7):
    if price < 0:
        raise ValueError("ราคาต้องไม่ติดลบ")
    if not 0 <= discount_percent <= 100:
        raise ValueError("ส่วนลดต้องอยู่ระหว่าง 0 ถึง 100")
    if vat_percent < 0:
        raise ValueError("VAT ต้องไม่ติดลบ")

    discount = price * discount_percent / 100
    discounted_price = price - discount
    vat = discounted_price * vat_percent / 100
    total = discounted_price + vat

    return discount, discounted_price, vat, total


def main():
    try:
        price = float(input("ราคาสินค้า (บาท): "))
        discount_percent = float(input("ส่วนลด (%): "))
        discount, discounted_price, vat, total = calculate_price(
            price, discount_percent
        )
    except ValueError as error:
        raise SystemExit(f"ข้อมูลไม่ถูกต้อง: {error}")

    print(f"\nส่วนลด: {discount:.2f} บาท")
    print(f"ราคาหลังหักส่วนลด: {discounted_price:.2f} บาท")
    print(f"VAT 7%: {vat:.2f} บาท")
    print(f"ราคาสุทธิ: {total:.2f} บาท")


if __name__ == "__main__":
    main()
