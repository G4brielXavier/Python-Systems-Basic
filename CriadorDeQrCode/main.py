import qrcode
import time

print("Gerador de QrCode")
print(" ")

link_to_qrcode = input("URL to Convert: https://")

print(f'Criando o QRCode para o link {link_to_qrcode} .')
time.sleep(0.5)
print(f'Criando o QRCode para o link {link_to_qrcode} ..')
time.sleep(0.5)
print(f'Criando o QRCode para o link {link_to_qrcode} ...')
time.sleep(0.5)

qr_code_main = qrcode.make(link_to_qrcode)

time.sleep(1)
name_file_qr_code_save = input("File name: ")

time.sleep(0.5)
qr_code_main.save(f'{name_file_qr_code_save}.png')

print(f'QRCode salvo! \n Nome: {name_file_qr_code_save}')