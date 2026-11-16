import streamlit as st
st.set_page_config(page_title="คำนวณส่วนลดสินค้าและ VAT 7%", page_icon="🛒")
st.title("🛒 แอปพลิเคชันคำนวณส่วนลดสินค้าและ VAT 7%")
price = st.number_input("กรอกราคาเต็มของสินค้า (บาท):", min_value=0.0, value=0.0, step=1.0, format="%.2f")
discount_percent = st.number_input("กรอกเปอร์เซ็นต์ส่วนลด (%):", min_value=0.0, max_value=100.0, value=0.0, step=1.0, format="%.2f")
discount = price * (discount_percent / 100)   
after_discount = price - discount             
vat = after_discount * 0.07                   
net_price = after_discount + vat               
st.subheader(f"• ราคาเต็มสินค้า: {price:,.2f} บาท (ส่วนลด {discount_percent:.2f}%)")
st.subheader(f"• ส่วนลดที่คำนวณได้: {discount:,.2f} บาท")
st.subheader(f"• ภาษีมูลค่าเพิ่ม (VAT 7%): {vat:,.2f} บาท")
st.subheader(f"• ราคาสุทธิที่ต้องจ่าย: {net_price:,.2f} บาท")
st.divider()
st.caption("นายภีรณัฏร์ พิมมะ เลขที่ 7 ม.4/5")
