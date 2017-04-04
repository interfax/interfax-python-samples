# get all recent faxes
faxes = interfax.outbound.all()

# cancel all processing faxes
for fax in faxes:
  if fax.status < 0:
    fax.cancel()
