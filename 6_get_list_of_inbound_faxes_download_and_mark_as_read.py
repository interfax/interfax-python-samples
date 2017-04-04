# get all unread faxes
faxes = interfax.inbound.all(
  unread_only=True
)

for fax in faxes:
  # save the fax image
  image = fax.image()
  image.save("{0}.pdf".format(fax.message_id))
  # # mark as read
  fax.mark(True)
