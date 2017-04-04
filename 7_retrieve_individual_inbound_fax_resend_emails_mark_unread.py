# given an InterFAX fax ID
fax_id = '12345'
# retrieve the fax
fax = interfax.inbound.find(fax_id)
# resend the email
fax.resend()
# mark as unread
fax.mark(False)
