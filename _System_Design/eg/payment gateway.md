https://www.youtube.com/watch?v=NxjGFIgFCbg

Term no Note
how card payment work
how 3D secure card payment
req
considertation
high level architecture
API
payment processor


# Payment Gateway
    a service which allow us to make payments online while making purchasing from e-commerse web site

# Payment Gateway Provider(PSP)
    it's the service which makes usre that money is transfer from payer's account to merchant account

# Issurer Bank
    bank to which Buyer is realted to
# card associations
    VISA/MASTER/AMEX

# PCI DSS
    payment card inustry data security standard.
    compliance when save your card info

# acquiring bank
    seller side
# 3D secure 

# ISO-8583 EFT swtich message format for card payment processing

Functional
  - allow multiple ways of payments
  - secure payment detail
  - secure transactions
  - avoid double payment
  - fast response
  - Handle timeout and failure

Non Functional
- highly consistent
- highly available
- scalabl

Design Considerations
- multiple subsystems to hand diff kind of payment card, internet banking, UPI
- Secure Payment detail. Protegrity to encrypt PII
- Use SSL
- Consistency and availalbley should be choose over partition toleranee. avoid duplicate
- scalable


seller webiste -> payment ingestion -> transaction ID genertor(unique ID)

transaction id and other payment detail (payment bank, merchant) in DB  structured schema  RDBMS is good (partition based on (date, type)) -> message to the queue

queue -> payment processor (update DB)
         > analytics 


Payment Ingestion
    - getFormForCardPayment
    - postRequestForCardPayment
    - --
    - --
    - gettransctionIDbyTransctionType
  
Payment Processor
    - processUPIPayment
    - processCardPayment
    - processUInternatePayment
    - retryOnFail

FailedQueue (new topic)

Payment Retry Service
    if status - fail, retry
    from bank indicate already success using same(unique) transaction id
    if already process

Payment Clearing Service (once a day or twice a day)
    not cleared.  settled the account -> credited the account -> money go to seller


