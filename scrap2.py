from bs4 import BeautifulSoup as soup
import requests
#api testing data
# brand = ['ASUS', 'MSI', 'MSI', 'Sapphire Tech', 'EVGA', 'GIGABYTE', 'XFX', 'Sapphire Tech', 'ASRock', 'EVGA', 'ASUS', 'GIGABYTE']
# title = ['ASUS ROG STRIX AMD Radeon RX 5700 XT Overclocked 8G GDDR6 HDMI DisplayPort Gaming Graphics Card (ROG-STRIX-RX5700XT-O8G-GAMING)', 'MSI GeForce GTX 1660 SUPER DirectX 12 GTX 1660 SUPER VENTUS XS OC 6GB 192-Bit GDDR6 PCI Express 3.0 x16 HDCP Ready Video Card', 'MSI GeForce RTX 2060 DirectX 12 RTX 2060 VENTUS XS 6G OC 6GB 192-Bit GDDR6 PCI Express 3.0 x16 HDCP Ready Video Card', 'SAPPHIRE PULSE Radeon RX 5600 XT DirectX 12 100419P6GL 6GB 192-Bit GDDR6 PCI Express 4.0 ATX Video Card', 'EVGA GeForce GTX 1660 XC GAMING, 06G-P4-1163-KR, 6GB GDDR5, HDB Fan', 'GIGABYTE Radeon RX 5700 XT DirectX 12 GV-R57XTGAMING-8GD 8GB 256-Bit GDDR6 PCI Express 4.0 x16 ATX Video Card', 'XFX Radeon RX 5600 XT RX-56XT6DF46 Video Card THICC II PRO-14GBPS 6GB BOOST UP TO 1620M D6  3xDP HDMI', 'SAPPHIRE PULSE Radeon RX 5500 XT DirectX 12 100418P4GL 4GB 128-Bit GDDR6 PCI Express 4.0 ATX Video Card', 'ASRock Challenger D Radeon RX 5500 XT DirectX 12 RX5500XT CLD 4GO 4GB 128-Bit GDDR6 PCI Express 4.0 x8 HDCP Ready Video Card', 'EVGA GeForce RTX 2060 XC GAMING, 6GB GDDR6, HDB Fan Graphics Card 06G-P4-2063-KR', 'ASUS GeForce RTX 2060 Overclocked 6G GDDR6 Dual-Fan EVO Edition VR Ready HDMI DisplayPort DVI Graphics Card (DUAL-RTX2060-O6G-EVO)', 'GIGABYTE Radeon RX 5600 XT DirectX 12 GV-R56XTGAMING OC-6GD 6GB 192-Bit GDDR6 PCI Express 4.0 x16 ATX Video Card']
# image = ['//c1.neweggimages.com/NeweggImage/ProductImageCompressAll300/14-126-344-V14.jpg', '//c1.neweggimages.com/NeweggImage/ProductImageCompressAll300/14-137-475-V01.jpg', '//c1.neweggimages.com/NeweggImage/ProductImageCompressAll300/14-137-396-V04.jpg', '//c1.neweggimages.com/NeweggImage/ProductImageCompressAll300/14-202-364-V01.jpg', '//c1.neweggimages.com/NeweggImage/ProductImageCompressAll300/14-487-438-V01.jpg', '//c1.neweggimages.com/NeweggImage/ProductImageCompressAll300/14-932-299-S01.jpg', '//c1.neweggimages.com/NeweggImage/ProductImageCompressAll300/14-150-835-S01.jpg', '//c1.neweggimages.com/NeweggImage/ProductImageCompressAll300/14-202-361-1.jpg', '//c1.neweggimages.com/NeweggImage/ProductImageCompressAll300/14-930-026-V03.jpg', '//c1.neweggimages.com/NeweggImage/ProductImageCompressAll300/14-487-423-V08.jpg', '//c1.neweggimages.com/NeweggImage/ProductImageCompressAll300/14-126-349-V01.jpg', '//c1.neweggimages.com/NeweggImage/ProductImageCompressAll300/14-932-244-S03.jpg']
# price =['459', '249', '339', '289', '239', '409', '299', '179', '179', '379', '329', '289']
# shipping_status=['Free Shipping', 'Free Shipping', 'Free Shipping', '$3.99 Shipping', 'Free Shipping', 'Free Shipping', 'Free Shipping', '$3.99 Shipping', 'Free Shipping', 'Free Shipping', '$3.99 Shipping', '$6.99 Shipping']


page_html = requests.get('https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38#').text
page_soup = soup(page_html,'lxml')
brand= []
title=[]
image =[]
price=[]
shipping_status=[]

for item in page_soup.find_all('div',class_='item-container'):
    brand.append(item.find('a',class_='item-brand').img['title'])
    title.append(item.img['title'])
    image.append(item.img['data-src'])
    price.append(item.find('li',class_='price-current').strong.text)
    shipping_status.append(item.find('li',class_='price-ship').text.strip())
api = [{'brand':brand, 'title':title, 'image':image, 'price': price, 'shipping_status':shipping_status} for brand,title,image,price,shipping_status in zip(brand,title,image,price,shipping_status)]

print(api)


