import discord
from discord.ext import commands

class dict_data(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    # ลองใช้เมธอด List
    # @commands.command()

    # รับข้อความจาก User ใน Topic ต่างๆ
    @commands.Cog.listener("on_message")
    async def on_message(self, message):

            #dictionary
        if message.content == "!dict":
            emBed = discord.Embed(title="Dictionary", description="Dictionary คือประเภทข้อมูลที่เก็บข้อมูลในรูปแบบคู่ของ Key และ Value โดยที่ Key \
            ใช้สำหรับเป็น Index ในการเข้าถึงข้อมูลและ Value เป็นค่าข้อมูลที่สอดคล้องกับ Key ของมัน\nDictionary Method ที่ใช้บ่อยในการทำโจทย์พิมพ์ !list ตามด้วยชื่อ Method เพื่อเรียกดู", color=0x6F9DC3)
            emBed.add_field(name="clear", value='ลบข้อมูลทั้งหมดภายใน Dictionary')
            emBed.add_field(name="copy", value='คัดลอก Dictionary ทั้งหมดไปยังอันใหม่')
            emBed.add_field(name="fromkeys", value='คืนค่า dictionary ด้วย key หรือ value ที่กำหนด')
            emBed.add_field(name="get", value='ส่งค่าข้อมูลใน Dictionary จาก Key ที่กำหนด')
            emBed.add_field(name="items", value='ส่งค่ากลับเป็นออบเจ็คของ Key และ Value')
            emBed.add_field(name="keys", value='ส่งค่ากลับเป็น List ของ Key ทั้งหมดใน Dictionary')
            emBed.add_field(name="pop", value='ส่งค่ากลับเป็นค่าสุดท้ายใน Dictionary')
            emBed.add_field(name="popitem", value='ส่งค่ากลับเป็น Tuple ออบเจ็คของ Key และ Value')
            emBed.add_field(name="setdefault", value='ส่งค่ากลับเป็นค่าของ Key ที่กำหนด ถ้าหากไม่มี Key อยู่ใส่ข้อมูลเข้าไปใน Dictionary')
            emBed.add_field(name="update", value='อัพเดท Dictionary กับคู่ของ Key และ Value จากออบเจ็คอื่น และเขียนทับ Key ที่มีอยู่')
            emBed.add_field(name="values", value='ส่งค่ากลับเป็น List ของ Value ทั้งหมดใน Dictionary')
            await message.channel.send(embed=emBed)



    #ดิ้ก clear
        elif message.content == "!dict clear":
            emBed = discord.Embed(title="dict.clear", description="ใช้ลบข้อมูลทั้งหมดภายใน Dictionary", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='car =	{\n  "brand": "Ford",\n  "model": "Mustang",\n  "year": 1964\n}\ncar.clear()\nprint(car)')
            emBed.add_field(name="ผลลัพธ์", value='{}')
            emBed.add_field(name="ลองใช้ clear", value='โดยการพิม do clear (ข้อความที่ต้องการ)', inline=False)
            await message.channel.send(embed=emBed)
        



    #ดิ้ก copy
        elif message.content == "!dict copy":
            emBed = discord.Embed(title="dict.copy", description="ใช้คัดลอก Dictionary ทั้งหมดไปยังอันใหม่", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='car = {\n  "brand": "Ford",\n  "model": "Mustang",\n  "year": 1964\n}\nx = car.copy()\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value="{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}")
            emBed.add_field(name="ลองใช้ clear", value='โดยการพิม do copy (ข้อความที่ต้องการ)', inline=False)
            await message.channel.send(embed=emBed)


    #ดิ้ก fromkeys
        elif message.content == "!dict fromkeys":
            emBed = discord.Embed(title="dict.fromkeys", description="ใช้คืนค่า dictionary ด้วย key หรือ value ที่กำหนด", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='x = ("key1", "key2", "key3")\ny = 0\nthisdict = dict.fromkeys(x, y)\nprint(thisdict)')
            emBed.add_field(name="ผลลัพธ์", value="['key1': 0, 'key2': 0, 'key3': 0]")
            emBed.add_field(name="ลองใช้ fromkeys", value='โดยการพิม do fromkeys (ข้อความที่ต้องการ)', inline=False)
            await message.channel.send(embed=emBed)



    #ดิ้ก get
        elif message.content == "!dict get":
            emBed = discord.Embed(title="dict.get", description="ใช้ส่งค่าข้อมูลใน Dictionary จาก Key ที่กำหนด", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='car = {\n  "brand": "Ford",\n  "model": "Mustang",\n  "year": 1964\n}\nx = car.get("model")\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value='Mustang')
            emBed.add_field(name="ลองใช้ get", value='โดยการพิม do get (ข้อความที่ต้องการ)', inline=False)
            await message.channel.send(embed=emBed)




    #ดิ้ก items
        elif message.content == "!dict items":
            emBed = discord.Embed(title="dict.items", description="ใช้ส่งค่ากลับเป็นออบเจ็คของ Key และ Value", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='car = {\n  "brand": "Ford",\n  "model": "Mustang",\n  "year": 1964\n}\nx = car.items()\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value="dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)]")
            emBed.add_field(name="ลองใช้ items", value='โดยการพิม do items (ข้อความที่ต้องการ)', inline=False)
            await message.channel.send(embed=emBed)



    #ดิ้ก key
        elif message.content == "!dict keys":
            emBed = discord.Embed(title="dict.keys", description="ใช้ส่งค่ากลับเป็น List ของ Key ทั้งหมดใน Dictionary", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='car = {\n  "brand": "Ford",\n  "model": "Mustang",\n  "year": 1964\n}\nx = car.keys()\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value="dict_keys(['brand', 'model', 'year'])")
            emBed.add_field(name="ลองใช้ keys", value='โดยการพิม do keys (ข้อความที่ต้องการ)', inline=False)
            await message.channel.send(embed=emBed)



    #ดิ้ก pop
        elif message.content == "!dict pop":
            emBed = discord.Embed(title="dict.pop", description="ใช้ส่งค่ากลับเป็นค่าสุดท้ายใน Dictionary", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='car = {\n  "brand": "Ford",\n  "model": "Mustang",\n  "year": 1964\n}\ncar.pop("model")\nprint(car)')
            emBed.add_field(name="ผลลัพธ์", value="{'brand': 'Ford', 'year': 1964}")
            emBed.add_field(name="ลองใช้ pop", value='โดยการพิม do pop (ข้อความที่ต้องการ)', inline=False)
            await message.channel.send(embed=emBed)


    #ดิ้ก popitem
        elif message.content == "!dict pop":
            emBed = discord.Embed(title="dict.popitem", description="ใช้ส่งค่ากลับเป็น Tuple ออบเจ็คของ Key และ Value", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='car = {\n  "brand": "Ford",\n  "model": "Mustang",\n  "year": 1964\n}\ncar.popitem()\nprint(car)')
            emBed.add_field(name="ผลลัพธ์", value="{'brand': 'Ford', 'model': 'Mustang'}")
            emBed.add_field(name="ลองใช้ popitem", value='โดยการพิม do popitem (ข้อความที่ต้องการ)', inline=False)
            await message.channel.send(embed=emBed)

        
    #ดิ้ก setdefault
        elif message.content == "!dict setdefault":
            emBed = discord.Embed(title="dict.setdefault", description="ใช้ส่งค่ากลับเป็นค่าของ Key ที่กำหนด ถ้าหากไม่มี Key อยู่ใส่ข้อมูลเข้าไปใน Dictionary", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='car = {\n  "brand": "Ford",\n  "model": "Mustang",\n  "year": 1964\n}\nx = car.setdefault("model", "Bronco")\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value='Mustang')
            emBed.add_field(name="ลองใช้ setdefault", value='โดยการพิม do set default (ข้อความที่ต้องการ)', inline=False)
            await message.channel.send(embed=emBed)


    #ดิ้ก update
        elif message.content == "!dict update":
            emBed = discord.Embed(title="dict.update", description="ใช้อัพเดท Dictionary กับคู่ของ Key และ Value จากออบเจ็คอื่น และเขียนทับ Key ที่มีอยู่", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='car = {\n  "brand": "Ford",\n  "model": "Mustang",\n  "year": 1964\n}\ncar.update({"color": "White"})\nprint(car)')
            emBed.add_field(name="ผลลัพธ์", value="{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'White'}")
            emBed.add_field(name="ลองใช้ update", value='โดยการพิม do update (ข้อความที่ต้องการ)', inline=False)
            await message.channel.send(embed=emBed)


    #ดิ้ก values
        elif message.content == "!dict values":
            emBed = discord.Embed(title="dict.values", description="ใช้ส่งค่ากลับเป็น List ของ Value ทั้งหมดใน Dictionary", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='car = {\n  "brand": "Ford",\n  "model": "Mustang",\n  "year": 1964\n}\nx = car.values()\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value="dict_values(['Ford', 'Mustang', 1964])")
            emBed.add_field(name="ลองใช้ values", value='โดยการพิม do values (ข้อความที่ต้องการ)', inline=False)
            await message.channel.send(embed=emBed)
            

def setup(bot):
    bot.add_cog(dict_data(bot))

