# QR code generator
    ZXing (“Zebra Crossing”) is the popular API for QR code processing in Java
    img -> text 
# payment gateway
# Microservices
# load balancers
# mysql database

[link] https://www.youtube.com/watch?v=rdJIM3jcICE

functional requirement

- create QR code
- read QR code
- register buyer and seller
- transfer money from buyer to seller (distributed)
- database schema


seller
    - seller_id
    - name
    - tax_id
    - phone
    - email

seller_wallet
    - seller_wallet_id
    - seller_id
    - balance
seller_transaction
    - id
    - buyer_id
    - purchese_item
    - amount

buyer
    - buyer_id
    - buyer_name
    - phone
    - email
buyer_wallet
    - buyer_wallet_id
    - buyer_id
    - balance
buyer_transction
    - id
    - seller_id
    - buyer_id
    - item
    - amount
    - STATUS pending or cancelled


Two types
    1. POS generate QR code
    2. street vendor style, use mobile app. seller print out QR code





seller app
    LB: resgisterSeller
        getQRCodeForBiz -> zxing
        CreateSellerWallet
        transferMontyBuyerWalletToBank


buyer app
    LB: getdatafrom QRcode
        register Buyer
        create BuyerWallet
        tranferMoney to BuyerWallet
        tranferMoney From Buyer to Seller [saga] pattern  https://microservices.io/patterns/data/saga.html


seller schema
buyer schema


