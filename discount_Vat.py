function calculatePrice(price, discountPercent, vatPercent = 7) {
  if (price < 0 || discountPercent < 0 || discountPercent > 100 || vatPercent < 0) {
    throw new Error("กรุณาตรวจสอบราคาและเปอร์เซ็นต์ที่ระบุ");
  }

  const discount = price * (discountPercent / 100);
  const priceAfterDiscount = price - discount;
  const vat = priceAfterDiscount * (vatPercent / 100);
  const total = priceAfterDiscount + vat;

  return { discount, priceAfterDiscount, vat, total };
}

const result = calculatePrice(1000, 20);

console.log(`ส่วนลด: ${result.discount} บาท`);
console.log(`ราคาหลังหักส่วนลด: ${result.priceAfterDiscount} บาท`);
console.log(`VAT: ${result.vat} บาท`);
console.log(`ราคาสุทธิ: ${result.total} บาท`);
