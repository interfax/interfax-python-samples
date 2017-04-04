import os

# create a new InterFAX Document
document = interfax.documents.create(
    "test.pdf",
    os.stat("test.pdf").st_size
)

# read the file to send
with open("test.pdf", "rb") as fp:
    cursor = 0
    while True:
        chunk = fp.read(500)
        if not chunk:
            break
        next_cursor = cursor + len(chunk)
        # upload each chunk
        document.upload(cursor, next_cursor-1, chunk)
        cursor = next_cursor

# send the fax
interfax.deliver(
  # a valid fax number
  fax_number='+11111111112',
  # the document URI
  files=[document.uri]
)
