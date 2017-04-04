# send a single fax
fax = interfax.deliver(
  # a valid fax number
  fax_number='+11111111112',
  # a path to an InterFAX
  # compatible file
  files=['path/to/fax.pdf']
)
