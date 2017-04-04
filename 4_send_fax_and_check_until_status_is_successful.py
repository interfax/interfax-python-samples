import time

fax = interfax.deliver(
  fax_number='+11111111112',
  files=['path/to/fax.pdf']
)

# wait for the fax to send
# successfully
while True:
  # reload the fax data
  fax = fax.reload()
  # sleep if pending
  if fax.status < 0:
    time.sleep(10)
  else:
    # output on success or error
    if fax.status == 0:
      print("Sent!")
    else:
      print("Error: #{fax.status}")
    break
