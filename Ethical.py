# Port Scanner - Built by Olamide
# Scans ports 1-500 and identifies common services
# FTP(21), SSH(22), HTTP(80), HTTPS(443)
target=input("What is your target? ")
for port in range(1,501):
  if port ==21:
  	print(f"Scanning port  {port} - FTP ")
  elif port ==22:
  	print(f"Scanning port  {port} - SSH ")
  elif port ==80:
  	print(f"Scanning port  {port} - HTTP ")
  elif port ==443:
  	print(f"Scanning port  {port} - HTTPS ")
  else:
  	print(f"Scanning port  {port} ")
