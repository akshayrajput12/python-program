import qrcode



data='''In English We say 
Please Come in My life and Make it beautiful
But miss reva for you i say 


Ek Nazar Dekho to Gujara Ho Jaye.
Is Toote Hue Dil Ko Sahara ho Jaye
Yun to Meri kasti Lehro Mai Fasi hai
Tum Hath Thamo to Kinara Ho jaye'''


img =qrcode.make(data)

img.save('F:\python/reva.png')