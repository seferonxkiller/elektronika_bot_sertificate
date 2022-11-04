from aiogram.types import Message ,CallbackQuery
from aiogram import executor
from aiogram.utils.callback_data import CallbackData

from config import dp,bot
from keyboard import menuStart, menuPhone, menuzakaz, menuZakazBerish, menuZakazBerish1,menuZakazBerish2,menuNotebook
import logging


@dp.message_handler(commands='start')
async def start(message: Message):
    txt = f"Assalomu alaykum,{message.from_user.full_name}"
    await message.answer(txt,reply_markup=menuStart)


@dp.message_handler(text='Smartfonlar')
async def phones(message: Message):
    await message.answer("tanlang",reply_markup=menuPhone)


@dp.message_handler(text='Samsung')
async def samsung1(message: Message):
    text1 = f" Samsung Galaxy A04s\n" \
           f"Narxi ₹13,499\n" \
           f"Display 6.50-inch (720x1600)\n" \
           f"Processor Samsung Exynos 850\n" \
           f"Front Camera 5MP\n" \
           f"Rear Camera 50MP + 2MP + 2MP\n" \
           f"RAM 4GB Storage 64GB\n" \
           f"Battery Capacity 5000mAh OS Android 12"
    text2 = f"Samsung Galaxy M13\n" \
            f"Narxi ₹10,490\n" \
            f"Display 6.60-inch\n" \
            f"Processor Samsung Exynos 850\n" \
            f"Front Camera 8MP\n" \
            f"Rear Camera 50MP + 5MP + 2MP\n" \
            f"RAM 4GB, 6GB\n" \
            f"Storage 64GB, 128GB\n" \
            f"Battery Capacity 6000mAh\n" \
            f"OS Android 12\n"
    text3 = f"Samsung Galaxy M13 5G\n" \
            f"Narxi ₹11,999\n" \
            f"Display 6.50-inch\n" \
            f"Front Camera 5MP\n" \
            f"Rear Camera 50MP + 2MP\n" \
            f"RAM 4GB, 6GB\n" \
            f"Storage 64GB, 128GB\n" \
            f"Battery Capacity 5000mAh\n" \
            f"OS Android 12\n"
    text4 = f"Samsung Galxy Z Flip 4\n" \
            f"Narxi  ₹89,999\n" \
            f"Display (Primary) 6.70-inch (1080x2640)\n" \
            f"Processor Qualcomm Snapdragon 8+ Gen 1\n" \
            f"Front Camera 10MP\n" \
            f"Rear Camera 12MP + 12MP\n" \
            f"RAM 8GB\n" \
            f"Storage 128GB, 256GB, 512GB\n" \
            f"Battery Capacity 3700mAh\n" \
            f"OS Android 12"


    text5 = f"Samsung Galxy Z Fold4\n" \
            f"Narxi ₹154,999\n" \
            f"Display (Primary) 7.60-inch (2176x1812)\n" \
            f"Processor Qualcomm Snapdragon 8+ Gen 1\b" \
            f"Front Camera 10MP + 4MP\n" \
            f"Rear Camera 50MP + 12MP + 10MP\n" \
            f"RAM 12GB\n" \
            f"Storage 256GB, 512GB\n" \
            f"Battery Capacity 4400mAh\n" \
            f"OS Android 12L\n"


    await message.answer_photo(open("samsung/Samsung Galaxy A04s Narxi ₹13,499.png","rb"),text1,reply_markup=menuzakaz)
    await message.answer_photo(open("samsung/Samsung Galaxy M13 Narxi ₹10,490.png", "rb"), text2,reply_markup=menuzakaz)
    await message.answer_photo(open("samsung/Samsung Galaxy M13 5G Narxi ₹11,999.png","rb"),text3,reply_markup=menuzakaz)
    await message.answer_photo(open("samsung/Samsung Galxy Z Flip 4 Narxi  ₹89,999.png", "rb"), text4,reply_markup=menuzakaz)
    await message.answer_photo(open("samsung/Samsung Galxy Z Fold4 Price ₹154,999.png", "rb"), text5,reply_markup=menuzakaz)


@dp.message_handler(text='Apple')
async def apple(message: Message):
    iphon13 = f"Iphone 13 Pro Max\n" \
              f"Narxi: $630\n" \
              f"Dimensions 	160.8 x 78.1 x 7.7 mm (6.33 x 3.07 x 0.30 in)\n" \
              f"Weight 	240 g (8.47 oz)\n" \
              f"Size 	6.7 inches, 109.8 cm2 (~87.4% screen-to-body ratio)\n" \
              f"OS 	iOS 15, upgradable to iOS 16.1\n" \
              f"Chipset 	Apple A15 Bionic (5 nm)\n" \
              f"CPU 	Hexa-core (2x3.23 GHz Avalanche + 4x1.82 GHz Blizzard)\n" \
              f"GPU 	Apple GPU (5-core graphics)\n"
    iphon14 = f"Iphone 14" \
              f"Narxi: $515"\
              f"Dimensions 	146.7 x 71.5 x 7.8 mm (5.78 x 2.81 x 0.31 in)\n" \
              f"Weight 	172 g (6.07 oz)\n" \
              f"Size 	6.1 inches, 90.2 cm2 (~86.0% screen-to-body ratio)\n" \
              f"OS 	iOS 16, upgradable to iOS 16.1\n"\
              f"Chipset 	Apple A15 Bionic (5 nm)\n" \
              f"CPU 	Hexa-core (2x3.23 GHz Avalanche + 4x1.82 GHz Blizzard)\n" \
              f"GPU 	Apple GPU (5-core graphics)\n"
    iphon14p = f"Iphone 14 Plus\n" \
               f"Narxi: $585\n" \
               f"Dimensions  160.8 x 78.1 x 7.8 mm (6.33 x 3.07 x 0.31 in)\n" \
               f"Weight 	203 g (7.16 oz)\n" \
               f"Size 	6.7 inches, 109.8 cm2 (~87.4% screen-to-body ratio)\n" \
               f"OS 	iOS 16, upgradable to iOS 16.1\n"\
               f"Chipset 	Apple A15 Bionic (5 nm)\n" \
               f"CPU 	Hexa-core (2x3.23 GHz Avalanche + 4x1.82 GHz Blizzard)\n" \
               f"GPU 	Apple GPU (5-core graphics)\n"
    iphon14pr = f"Iphone 14 Pro\n" \
                f"Narxi: $655\n" \
                f"Dimensions 	147.5 x 71.5 x 7.9 mm (5.81 x 2.81 x 0.31 in)\n" \
                f"Weight 	206 g (7.27 oz)\n" \
                f"Size 	6.1 inches, 91.7 cm2 (~87.0% screen-to-body ratio)\n" \
                f"OS 	iOS 16, upgradable to iOS 16.1\n" \
                f"Chipset 	Apple A16 Bionic (4 nm)\n" \
                f"CPU 	Hexa-core (2x3.46 GHz Everest + 4x2.02 GHz Sawtooth)\n" \
                f"GPU 	Apple GPU (5-core graphics)\n"
    iphon14prm = f"Iphone 14 Pro Max\n" \
                 f"Narxi: $725\n" \
                 f"Dimensions 	160.7 x 77.6 x 7.9 mm (6.33 x 3.06 x 0.31 in)\n" \
                 f"Weight 	240 g (8.47 oz)\n" \
                 f"Size 	6.7 inches, 110.2 cm2 (~88.3% screen-to-body ratio)\n" \
                 f"OS 	iOS 16, upgradable to iOS 16.1\n" \
                 f"Chipset 	Apple A16 Bionic (4 nm)\n" \
                 f"CPU 	Hexa-core (2x3.46 GHz Everest + 4x2.02 GHz Sawtooth)\n" \
                 f"GPU 	Apple GPU (5-core graphics)\n"

    await message.answer_photo(open("Apple/Iphone 13 Pro Max $630.png","rb" ),iphon13,reply_markup=menuzakaz)
    await message.answer_photo(open("Apple/Iphone 14 narxi $515.png","rb"),iphon14,reply_markup=menuzakaz)
    await message.answer_photo(open("Apple/Iphne 14 Plus Narxi $585.png","rb"),iphon14p,reply_markup=menuzakaz)
    await message.answer_photo(open("Apple/Iphone 14 Pro narxi $655.png","rb"),iphon14pr,reply_markup=menuzakaz)
    await message.answer_photo(open("Apple/Iphone 14 Pro max narxi $725.png","rb"),iphon14prm,reply_markup=menuzakaz)

@dp.message_handler(text='Redmi')
async def redmi(message: Message):
    black = f"Xiaomi Black Shark 5 Rs" \
            f"Narxi: $520"\
            f"Dimensions 	163.7 x 76.2 x 9.9 mm (6.44 x 3.00 x 0.39 in)\n" \
            f"Weight 	220 g (7.76 oz)\n" \
            f"Size 	6.67 inches, 107.4 cm2 (~86.1% screen-to-body ratio)\n" \
            f"OS 	Android 12, Joy UI 12.8\n" \
            f"Chipset 	Qualcomm SM8350 Snapdragon 888/888+ 5G (5 nm)\n" \
            f"GPU 	Adreno 660\n"\
            f"CPU 	Octa-core (1x2.84/3.0 GHz Cortex-X1 & 3x2.42 GHz Cortex-A78 & 4x1.80 GHz Cortex-A55)\n" \

    pro = f"Xiaomi 12 Pro\n" \
          f"Narxi: $700\n" \
          f"Dimensions 	162.9 x 76 x 7.9 mm (6.41 x 2.99 x 0.31 in)\n" \
          f"Weight 	187 g (6.60 oz)\n" \
          f"Size 	6.67 inches, 107.4 cm2 (~86.8% screen-to-body ratio)\n" \
          f"OS 	Android 12, MIUI 13\n"\
          f"Chipset 	MediaTek Dimensity 1080 (6 nm)\n" \
          f"CPU 	Octa-core (2x2.6 GHz Cortex-A78 & 6x2.0 GHz Cortex-A55)\n" \
          f"GPU 	Mali-G68 MC4\n"
    i = f"Xiaomi 11i Hyperchange\n" \
        f"Narxi: $360\n" \
        f"Dimensions 	163.7 x 76.2 x 8.3 mm (6.44 x 3.00 x 0.33 in)\n" \
        f"Weight 	207 g (7.30 oz)\n" \
        f"Size 	6.67 inches, 107.4 cm2 (~86.1% screen-to-body ratio)\n" \
        f"OS 	Android 11, upgradable to Android 12, MIUI 13Chipset 	MediaTek Dimensity 920 (6 nm)\n" \
        f"CPU 	Octa-core (2x2.5 GHz Cortex-A78 & 6x2.0 GHz Cortex-A55)\n" \
        f"GPU 	Mali-G68 MC4\n"
    spro = f"Xiaomi 12s Pro\n" \
           f"Narxi: $700\n" \
           f"Dimensions 	163.6 x 74.6 x 8.2 mm or 8.7 mm\n" \
           f"Weight 	203 g / 204 g (7.16 oz)\n" \
           f"Size 	6.73 inches, 109.4 cm2 (~89.6% screen-to-body ratio)\n" \
           f"OS 	Android 12, MIUI 13\n" \
           f"Chipset 	Qualcomm SM8475 Snapdragon 8+ Gen 1 (4 nm)\n" \
           f"CPU 	Octa-core (1x3.19 GHz Cortex-X2 & 3x2.75 GHz Cortex-A710 & 4x1.80 GHz Cortex-A510)\n" \
           f"GPU 	Adreno 730\n"
    shark = f"Xiaomi Black Shark 4s Pro\n" \
            f"Narxi: $755\n" \
            f"Dimensions 	163.7 x 76.2 x 9.9 mm (6.44 x 3.00 x 0.39 in)\n" \
            f"Weight 	220 g (7.76 oz)\n" \
            f"Size 	6.67 inches, 107.4 cm2 (~86.1% screen-to-body ratio)\n" \
            f"OS 	Android 11, Joy UI 12.8\n" \
            f"Chipset 	Qualcomm SM8350 Snapdragon 888+ 5G (5 nm)\n" \
            f"CPU 	Octa-core (1x3.0 GHz Cortex-X1 & 3x2.42 GHz Cortex-A78 & 4x1.80 GHz Cortex-A55)\n" \
            f"GPU 	Adreno 660\n"


    await message.answer_photo(open("Redmi/Xiaomi Black Shark 5 Rs Narxi $520.png","rb"),black,reply_markup=menuzakaz)
    await message.answer_photo(open("Redmi/Xiaomi 12 Pro Narxi $700.png","rb"),pro,reply_markup=menuzakaz)
    await message.answer_photo(open("Redmi/Xiaomi 11i Hyperchange narxi $360.png","rb"),i,reply_markup=menuzakaz)
    await message.answer_photo(open("Redmi/Xiaomi 12s Pro Narxi $700.png","rb"),spro,reply_markup=menuzakaz)
    await message.answer_photo(open("Redmi/Xiaomi Black Shark 4s Pro narxi $755.png","rb"),shark,reply_markup=menuzakaz)

@dp.message_handler(text='OPPO')
async def oppo(message: Message):

    A57e = f"Oppo A57e\n" \
           f"Narxi: $180\n" \
           f"Dimensions 163.7 x 75 x 8 mm (6.44 x 2.95 x 0.31 in)\n" \
           f"Weight 187 g\n" \
           f"Screen Size 6.56 inches\n" \
           f"CPU Octa-core (4x2.3 GHz Cortex-A53 & 4x1.8 GHz Cortex-A53)\n" \
           f"Chipset MediaTek MT6765G Helio G35 (12 nm)\n" \
           f"GPU PowerVR GE8320\n"
    A77s = f"Oppo A77s\n" \
           f"Narxi: $240\n" \
           f"Dimensions 3.8 x 75 x 8 mm (6.45 x 2.95 x 0.31 in)\n" \
           f"Weight 187 g\n" \
           f"Screen Size 6.56 inches\n" \
           f"CPU Octa-core (2x2.4 GHz Cortex-A76 & 6x2.0 GHz Cortex-A55)\n" \
           f"Chipset Qualcomm Snapdragon 680\n" \
           f"GPU Adreno 610\n"
    A57s = f"Oppo A57e\n" \
           f"Narxi: $199\n" \
           f"Dimensions 63.8 x 75 x 8 mm (6.45 x 2.95 x 0.31 in)\n" \
           f"Weight 87 g\n" \
           f"Screen Size 6.56 inches\n" \
           f"CPU Octa-core (2x2.4 GHz Cortex-A76 & 6x2.0 GHz Cortex-A55)\n" \
           f"Chipset MediaTek MT6765G Helio G35 (12 nm)\n" \
           f"GPU PowerVR GE8320\n"


    A77 = f"Oppo A77 2022\n" \
          f"Narxi: $199\n" \
          f"Dimensions 163.8 x 75 x 8 mm (6.45 x 2.95 x 0.31 in)\n" \
          f"Weight 190 g\n" \
          f"CPU Octa-core (2x2.4 GHz Cortex-A76 & 6x2.0 GHz Cortex-A55)\n" \
          f"Chipset MediaTek Helio G35\n" \
          f"GPU Mali-G57 MC2\n"
    Reno8 = f"Reno8 Pro 5g\n" \
            f"Narxi: $575\n" \
            f"Dimensions 161.2 x 74.2 x 7.3 mm (6.35 x 2.92 x 0.29 in)\n" \
            f"Weight 183g\n" \
            f"CPU Octa-core (4x2.85 GHz Cortex-A78 & 4x2.0 GHz Cortex-A55\n" \
            f"Chipset MediaTek Dimensity 8100-Max (5 nm)\n" \
            f"GPU Mali-G610 MC6\n"


    await message.answer_photo(open("OPPO/Oppo A57s narxi $199.png","rb"),A57s,reply_markup=menuzakaz)
    await message.answer_photo(open("OPPO/Oppo A77s narxi $240.png","rb"),A77s,reply_markup=menuzakaz)
    await message.answer_photo(open("OPPO/Oppo A 57e narxi $180.png","rb"),A57e,reply_markup=menuzakaz)
    await message.answer_photo(open("OPPO/Oppo A77 2022 narxi $199.png", "rb"),A77,reply_markup=menuzakaz)
    await message.answer_photo(open("OPPO/Oppo Reno8 Pro 5g  Narxi $575.png", "rb"),Reno8,reply_markup=menuzakaz)


@dp.message_handler(text='VIVO')
async def oppo(message: Message):
    Y77e = f"Vivo Y77e\n" \
           f"Narxi: $265" \
           f"Dimensions 164 x 75.8 x 8.3 mm (6.46 x 2.98 x 0.33 in)\n" \
           f"Weight 194 g\n" \
           f"CPU Octa-core (2x2.4 GHz Cortex-A76 & 6x2.0 GHz Cortex-A55)\n" \
           f"Chipset MediaTek MT6833P Dimensity 810\n" \
           f"GPU Mali-G57 MC2\n"
    Y52t = f"Vivo Y52t\n" \
           f"Nari: $185\n" \
           f"Dimensions 164 x 75.3 x 8.5 mm (6.46 x 2.96 x 0.33 in)\n" \
           f"Weight 198g\n" \
           f"CPU Octa-core (2x2.2 GHz Cortex-A76 & 6x2.0 GHz Cortex-A55)\n" \
           f"Chipset MediaTek MT6833 Dimensity 700 5G (7 nm)\n" \
           f"GPU Mali-G57\n"
    Z6 = f"Vivo Iqoo Z6 5g\n" \
         f"Narxi: $245\n" \
         f"Dimensions 164 x 75.8 x 8.6 mm (6.46 x 2.98 x 0.34 in)\n" \
         f"Weight 194 g\n" \
         f"CPU Octa-core (2x2.2 GHz Kryo 660 Gold & 6x1.7 GHz Kryo 660 Silver)\n" \
         f"Chipset Qualcomm SM6375 Snapdragon 778G+\n" \
         f"GPU Adreno 642L"
    X = f"Vivo X Fold Plus\n" \
        f"Narxi: $1400\n" \
        f"Dimensions Unfolded: 162 x 144.9 x 6.3 mm\n" \
        f"Folded: 162 x 74.5 x 14.6 mm\n" \
        f"Weight 311 g\n" \
        f"CPU Octa-core (1x3.19 GHz Cortex-X2 & 3x2.75 GHz Cortex-A710 & 4x1.80 GHz Cortex-A510)\n" \
        f"Chipset Qualcomm SM8250 Snapdragon 8+ Gen 1\n" \
        f"GPU Adreno 730"
    Z6lite = f"Vivo Iqoo Z6 Lite\n" \
             f"Narxi: $175" \
             f"Dimensions 4 x 75.8 x 8.3 mm (6.46 x 2.98 x 0.33 in)\n" \
             f"Weight 194 g\n" \
             f"CPU Octa-core (4x2.4 GHz Kryo 265 Gold & 4x1.9 GHz Kryo 265 Silver)\n" \
             f"Chipset Qualcomm SM6225 Snapdragon 4 Gen 1\n" \
             f"GPU Adreno 610"

    await message.answer_photo(open("ViVO/Vivo Y77e narxi $265.png","rb"),Y77e,reply_markup=menuzakaz)
    await message.answer_photo(open("ViVO/Vivo Y52t Narxi $185.png","rb"),Y52t,reply_markup=menuzakaz)
    await message.answer_photo(open("ViVO/Vivo Iqoo Z6 5g narxi $245.png","rb"),Z6,reply_markup=menuzakaz)
    await message.answer_photo(open("ViVO/Vivo X Fold Plus Narxi $1400.png", "rb"),X,reply_markup=menuzakaz)
    await message.answer_photo(open("ViVO/Vivo Iqoo Z6 Lite Narxi $175.png", "rb"),Z6lite, reply_markup=menuzakaz)

@dp.message_handler(text='Realmi')
async def oppo(message: Message):
    deg = f"Realmi 9i 5g\n" \
         f"Narxi: $190\n" \
         f"Dimensions 164.4 x 75.1 x 8.1 mm (6.47 x 2.96 x 0.32 in)\n" \
         f"Weight 187 g\n" \
         f"CPU Octa-core (2x2.4 GHz Cortex-A76 & 6x2.0 GHz Cortex-A55)\n" \
         f"Chipset MediaTek MT6833P Dimensity 810\n" \
         f"GPU Mali-G57 MC2"
    C33 = f"Realmi C33\n" \
          f"Narxi: $110\n" \
          f"Dimensions 164.2 x 75.7 x 8.3 mm (6.46 x 2.98 x 0.33 in)\n" \
          f"Weight 197 gram\n" \
          f"CPU Octa-core (2x2.0 GHz Cortex-A75 & 6x1.7 GHz Cortex-A55)\n" \
          f"Chipset Unisoc Tiger T612\n" \
          f"GPU Mali-G57"
    C30 = f"Realmi C30s\n" \
          f"Narxi: $95\n" \
          f"Dimensions 164.2 x 75.7 x 8.5 mm (6.46 x 2.98 x 0.33 in)\n" \
          f"Weight 186 g\n" \
          f"CPU Octa-core 1.6 GHz Cortex-A55\n" \
          f"Chipset -\n" \
          f"GPU IMG8322"
    Q5x = f"Realmi Q5x\n" \
          f"Narxi: $150\n" \
          f"Dimensions 164.3 x 75.6 x 8.5 mm (6.47 x 2.98 x 0.33 in)\n" \
          f"Weight 184 g\n" \
          f"CPU Octa-core (2x2.2 GHz Kryo 570 & 6x1.8 GHz Kryo 570)\n" \
          f"Chipset MediaTek Dimensity 700\n" \
          f"GPU Mali-G52"
    Q5 = f"Realmi Q5 Carnival Edition\n" \
         f"Narxi: $355\n" \
         f"Dimensions 164.3 x 75.6 x 8.5 mm (6.47 x 2.98 x 0.33 in)\n" \
         f"Weight 195 g\n" \
         f"CPU Octa-core (2x2.2 GHz Kryo 570 & 6x1.8 GHz Kryo 570)\n" \
         f"Chipset Qualcomm Snapdragon 695\n" \
         f"GPU Adreno 619"


    await message.answer_photo(open("Realmi/Realmi 9i 5g narxi $190.png","rb"),deg,reply_markup=menuzakaz)
    await message.answer_photo(open("Realmi/Realmi C33 narxi $110 .png","rb"),C33,reply_markup=menuzakaz)
    await message.answer_photo(open("Realmi/Realmi C30s narxi $95.png","rb"),C30,reply_markup=menuzakaz)
    await message.answer_photo(open("Realmi/Realmi Q5x narxi $150.png", "rb"),Q5x, reply_markup=menuzakaz)
    await message.answer_photo(open("Realmi/Realmi Q5 Carnival Edition narxi $355.png", "rb"),Q5, reply_markup=menuzakaz)

@dp.message_handler(text='Huawei')
async def oppo(message: Message):
    Enjoy = f"Huawei 50\n" \
            f"Narxi: $195\n" \
            f"Dimensions 165.2 x 76 x 9.2 mm (6.50 x 2.99 x 0.36 in)\n" \
            f"Weight 188 g\n" \
            f"CPU Octa-core (2x2.0 GHz Cortex-A76 & 6x2.0 GHz Cortex-A55)\n" \
            f"Chipset Kirin 710\n" \
            f"GPU Mali-G51 MP4"
    Nova = f"Huawei Nova 10z\n" \
           f"Narxi: $245" \
           f"Dimensions 160.7 x 73.3 x 8.4 mm (6.33 x 2.89 x 0.33 in)\n" \
           f"Weight 179 g\n" \
           f"CPU Octa-core (4x2.4 GHz Kryo 670 & 4x1.8 GHz Kryo 670)\n" \
           f"Chipset Qualcomm SM7325 Snapdragon 778G 4G\n" \
           f"GPU Adreno 642L"
    Mate = f"Huawei Mate Xs 2" \
           f"Narxi: $1510\n" \
           f"Dimensions Unfolded: 156.5 x 139.3 x 5.4 mm\n" \
           f"Folded: 156.5 x 75.5 x 11.1 mm\n" \
           f"Weight 255 g / 257 g (8.99 oz)\n" \
           f"CPU Octa-core (1x2.84 GHz Kryo 680 & 3x2.42 GHz Kryo 680 & 4x1.80 GHz Kryo 680\n" \
           f"Chipset Qualcomm SM8350 Snapdragon 888 4G\n" \
           f"GPU Adreno 660"
    Y90 = f"Nova Y90\n" \
          f"Narxi: $299\n" \
          f"Dimensions 163.3 x 74.7 x 8.4 mm (6.43 x 2.94 x 0.33 in)\n" \
          f"Weight 195 grams\n" \
          f"CPU Octa-core (4x2.4 GHz Kryo 265 Gold & 4x1.9 GHz Kryo 265 Silver)\n" \
          f"Chipset Qualcomm SM6225 Snapdragon 680 4G\n" \
          f"GPU Adreno 610"

    Pro = f"Nova 10 Pro\n" \
          f"Narxi: $550\n" \
          f"Dimensions 164.3 x 74.5 x 7.9 mm (6.47 x 2.93 x 0.31 in)\n" \
          f"Weight 191 grams\n" \
          f"CPU Octa-core (1x2.58 GHz Cortex-A76 & 3x2.40 GHz Cortex-A76 & 4x1.84 GHz Cortex-A55)\n" \
          f"Chipset Qualcomm SM7325 Snapdragon 778G 4G\n" \
          f"GPU Adreno 642L"


    await message.answer_photo(open("Huawei/Huawei Enjoy 50 narxi $195.png","rb"),Enjoy,reply_markup=menuzakaz)
    await message.answer_photo(open("Huawei/Huawei Nova 10z narxi $245.png","rb"),Nova,reply_markup=menuzakaz)
    await message.answer_photo(open("Huawei/Huawei Mate Xs 2 narxi $1510.png","rb"),Mate,reply_markup=menuzakaz)
    await message.answer_photo(open("Huawei/Huawei Nova Y90 narxi $299.png", "rb"),Y90, reply_markup=menuzakaz)
    await message.answer_photo(open("Huawei/Huawei Nova 10 Pro narxi $550.png", "rb"),Pro, reply_markup=menuzakaz)

@dp.message_handler(text='Pocco')
async def oppo(message: Message):
    C40 = f"Poco C40\n" \
          f"Narxi: $150\n" \
          f"Dimensions 169.6 x 76.6 x 9.2 mm (6.68 x 3.02 x 0.36 in)\n" \
          f"Weight 204  g\n" \
          f"CPU Octa-core (4x2.0 GHz Cortex-A55 & 4x1.5 GHz Cortex-A55)\n" \
          f"Chipset JLQ JR510 (11 nm)\n" \
          f"GPU Mali-G57 MC1\n"
    M5 = f"Poco M5\n" \
         f"Narxi: $170\n" \
         f"Dimensions 164 x 76.1 x 8.9 mm (6.46 x 3.00 x 0.35 in)\n" \
         f"Weight 201 g\n" \
         f"CPU Octa-core (2x2.2 GHz Cortex-A76 & 6x2.0 GHz Cortex-A55)\n" \
         f"Chipset MediaTek Helio G99\n" \
         f"GPU Mali-G57 MC2\n"

    M5s = f"Poco M5s\n" \
          f"Narxi: $210\n" \
          f"Dimensions 160.5 x 74.5 x 8.3 mm (6.32 x 2.93 x 0.33 in)\n" \
          f"Weight 178.8 g\n" \
          f"CPU Octa-core (2x2.05 GHz Cortex-A76 & 6x2.0 GHz Cortex-A55)\n" \
          f"Chipset Mediatek Helio G95 (12 nm)\n" \
          f"GPU Mali-G76 MC4\n"
    M4 = f"Poco M4 5g\n" \
         f"Narxi: $170\n" \
         f"Dimensions 164 x 76.1 x 8.9 mm (6.46 x 3.00 x 0.35 in)\n" \
         f"Weight 200 g\n" \
         f"CPU Octa-core (1x2.4 GHz Kryo 475 Prime & 1x2.2 GHz Kryo 475 Gold & 6x1.8 GHz\n" \
         f"Chipset MediaTek Dimensity 700\n" \
         f"GPU Mali-G57"

    Pro = f"Poco M4 Pro 4g\n" \
          f"Narxi: $250\n" \
          f"Dimensions 159.9 x 73.9 x 8.1 mm (6.30 x 2.91 x 0.32 in)\n" \
          f"Weight 179 g\n" \
          f"CPU Octa-core (4x2.2 GHz Cortex-A76 & 4x2.0 GHz Cortex-A55)\n" \
          f"Chipset MediaTek Helio G96\n" \
          f"GPU Mali-G57"




    await message.answer_photo(open("Pocco/Poco C40 narxi $150.png","rb"),C40,reply_markup=menuzakaz)
    await message.answer_photo(open("Pocco/Poco M5 narxi $170.png","rb"),M5,reply_markup=menuzakaz)
    await message.answer_photo(open("Pocco/Poco M5s narxi $210.png","rb"),M5s,reply_markup=menuzakaz)
    await message.answer_photo(open("Pocco/Poco M4 5g narxi $170.png","rb"),M4, reply_markup=menuzakaz)
    await message.answer_photo(open("Pocco/Poco M4 Pro 4g narxi $250.png", "rb"),Pro, reply_markup=menuzakaz)


@dp.message_handler(commands='help')
async def help(message: Message):
    await message.answer("shu kishiga yozing https://t.me/Dilshodjon404")
@dp.message_handler(text='Notebooklar')
async def note(message: Message):
    await message.answer("Notebooklar",reply_markup=menuNotebook)

@dp.message_handler(text='HP')
async def hp(message: Message):
    l = f"Hp Laptop\n" \
        f"Narxi: $700\n" \
        f"Core i3-1125G4 Acoustic system (Speakers)\n" \
        f"Trust 2.0\n" \
        f"Leto Compact BLACK + Mouse 2E\n" \
        f"MF211 WL Gray wireless\n"
    f = f"Hp Laptop\n" \
        f"Narxi: $750\n\n" \
        f"Felicette 21C1\n" \
        f"Ryzen 3-5300U quad\n" \
        f"8GB DDR4 1DM 3200\n" \
        f"Acoustic system (Speakers)\n" \
        f" Trust 2.0\n" \
        f"Leto Compact BLACK + Mouse 2E\n" \
        f" MF211 WL Gray wireless $750"
    d = f"Hp Laptop\n" \
        f"Narxi: $660\n" \
        f"Felicette 21C1\n" \
        f"Ryzen 3-5300U quad \n " \
        f"8GB DDR4 1DM 3200 \n " \
        f"Acoustic system (Speakers)\n " \
        f"Trust 2.0\n" \
        f"Leto Compact BLACK + Mouse 2E MF211 \n" \
        f"WL Gray wireless $750"
    await message.answer_photo(open("HP/hp1.png","rb"),l,reply_markup=menuzakaz)
    await message.answer_photo(open("HP/hp2.png","rb"),f,reply_markup=menuzakaz)
    await message.answer_photo(open("HP/hp3.png","rb"),d,reply_markup=menuzakaz)

@dp.message_handler(text='Mackbook')
async def mak(message: Message):
    d = f"Mackbook Pro\n" \
        f"Narxi: $1299\n" \
        f"13-inch"\
        f"Mackbook Pro M1\n" \
        f"Ram: 8GB\n" \
        f"SSD: 256 GB\n"
    a = f"Mackbook Pro\n" \
        f"Narxi: $2499\n" \
        f"14-inch" \
        f"Mackbook Pro M1Pro\n" \
        f"Ram: 16GB\n" \
        f"SSD: 512 GB\n"
    cs = f"Mackbook Pro\n" \
        f"Narxi: $1999\n" \
        f"14-inch" \
        f"Mackbook Pro M2\n" \
        f"Ram: 16GB\n" \
        f"SSD: 512 GB\n"
    await message.answer_photo(open("Mackbook/8gb 256 M2 $1299.png","rb"),d,reply_markup=menuzakaz)
    await message.answer_photo(open("Mackbook/M1Pro 16gb 512Gb $2499 16-inc.png","rb"),a,reply_markup=menuzakaz)
    await message.answer_photo(open("Mackbook/M2 14-inch 16GB 512GB $1999.png","rb"),cs,reply_markup=menuzakaz)


@dp.message_handler(text='Asus')
async def asus(message: Message):
    asus = f"Asus\n" \
           f"Narxi: $1999\n" \
           f"Windows 11 Home - ASUS recommends Windows 11 Pro for business\n" \
           f"Intel® Evo™ certified laptop\n" \
           f"Up to 12th gen Intel® Core™ i9 processor\n" \
           f"Up to NVIDIA® GeForce® RTX 3050 Ti\n" \
           f"Up to 32 GB memory\n" \
           f"Up to 2 TB SSD storage\n" \
           f"Up to 14.5\n" \
           f"2.8K OLED NanoEdge display\n" \
           f"Long-lasting 76 Wh battery"
    asus1 = f"Asus\n" \
            f"Narxi: $2599\n" \
            f"Windows 11 Pro - ASUS recommends Windows 11 Pro for business\n" \
            f"Up to 15.6 4K OLED NanoEdge display\n" \
            f"Up to 12th Intel® Core™ i9 processor\n" \
            f"Up to NVIDIA® GeForce RTX 3070Ti\n" \
            f"Up to 32 GB memory\n" \
            f"Up to 1 TB SSD storage\n" \
            f"NanoEdge 93% screen-to-body ratio\n" \
            f"DCI-P3: 100%"

    asus2 = f"Asus\n" \
            f"Narxi: $2799\n" \
            f"Windows 11 Pro - ASUS recommends Windows 11 Pro for business\n" \
            f"Up to 12th gen Intel® Core™ i9 processor\n" \
            f"Up to NVIDIA® GeForce® RTX 3060\n" \
            f"Up to 32 GB memory\n" \
            f"Up to 2 TB SSD storage\n" \
            f"Up to 16 4K/UHD OLED NanoEdge display\n" \
            f"Long-lasting 96 Wh battery\n" \
            f"ASUS Dial"



    await message.answer_photo(open("Asus/Asus $1999.png","rb"),asus,reply_markup=menuzakaz)
    await message.answer_photo(open("Asus/Asus $2599.png","rb"),asus1,reply_markup=menuzakaz)
    await message.answer_photo(open("Asus/Asus $2799.png","rb"),asus2,reply_markup=menuzakaz)

@dp.message_handler(text='Maishiy texnika')
async def tex(message: Message):
    tr = f"Тип   холодильник двухкамерный\n" \
         f"Количество дверей   2\n" \
         f"Полезный объем   265 л\n" \
         f"Климатический класс\n" \
         f"Уровень ш ума   42 дБ\n" \
         f"Энергопотребление   248 в год, кВт / ч"
    tra = f"Karcher WD 5 V-25\n" \
          f"Narxi: $300"\
          f"Тип 	вертикальный\n" \
          f"Уборка 	сухая\n" \
          f"Потребляемая мощность 	−\n" \
          f"Мощность всасывания 	1100 Вт\n" \
          f"Уровень шума -"
    ty = f"LG F2J5NS6W\n" \
         f"Narxi: $500\n" \
         f"Vazn 60.0 Кг\n" \
         f"Energiya sarflash klassi A+\n"\
         f"Aylantirish payti shovqin darajasi 74 дБ\n" \
         f"Kir yuvish payti shovqin darajasi 55 дБ\n" \
         f"Aylantirish paytida tezligi 1200 об/мин\n" \
         f"Boshqaruv сенсорное\n" \
         f"Displey Есть\n" \
         f"Kir solish joyi фронтальная\n" \
         f"Maksimal sig'imi 6.0 кг\n" \
         f"Joylashuv отдельно стоящая\n" \
         f"Balandligi 85 см\n" \
         f"Chuqurligi 45 см\n" \
         f"Kengligi 60 см\n"

    await message.answer_photo(open("texnika/Artel HD 370 RND Eco White.png","rb"),tr,reply_markup=menuzakaz)
    await message.answer_photo(open("texnika/Karcher WD 5 V-25 $ 300.png","rb"),tra,reply_markup=menuzakaz)
    await message.answer_photo(open("texnika/LG F2J5NS6W $500.png","rb"),ty,reply_markup=menuzakaz)
@dp.message_handler(text="Orqaga👈")
async def orqa(message: Message):
    await message.answer("Orqaga",reply_markup=menuStart)
@dp.callback_query_handler(text="Zakaz")
async def zakaz(call: CallbackQuery):
    await call.message.answer("salom",reply_markup=menuZakazBerish2)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Location")
async def zakaz1(call: CallbackQuery):
    await call.message.answer("zakaz uchun joyingizni jo'nating",menuZakazBerish1)

@dp.callback_query_handler(text="Contact")
async def zakaz1(call: CallbackQuery):
    txt = "Zakazingiz qabul qilindi"
    await call.message.answer("zakaz uchun kontaktingizni jo'nating",txt,menuZakazBerish)

@dp.callback_query_handler(text="Orqaga👈")
async def orqaga(call: CallbackQuery):
    await call.message.answer("orqaga",reply_markup=menuPhone)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="Bosh Menu🏠")
async def menus(call: CallbackQuery):
    await call.message.answer("Bosh Menu🏠",reply_markup=menuStart)


@dp.message_handler(text="Bosh Menu🏠")
async def mensi(message: Message):
    await message.answer("Bosh Menu🏠",reply_markup=menuStart)

if __name__ == '__main__':
    executor.start_polling(dp)