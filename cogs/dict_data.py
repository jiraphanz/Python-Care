import discord
from discord.ext import commands

class dict_data(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    # ลองใช้เมธอด Dictionary
    # ลองใช้ clear
    @commands.command()
    async def dclear(self, ctx):
        dict = {"brand": "Ford", "model": "Mustang", "year": "1964"}
        dict.clear()
        emBed = discord.Embed(title="ลองใช้ dict.clear", description="", color=0x6F9DC3)
        emBed.add_field(name="ตัวอย่างโค้ด", value='dict = {\n"brand": "Ford",\n"model": "Mustang",\n"year": "1964"\n}\ndict.clear()\nprint(dict)')
        emBed.add_field(name="ผลลัพธ์", value='{0}' .format(dict))
        await ctx.channel.send(embed=emBed)

    # ลองใช้ copy
    @commands.command()
    async def dcopy(self, ctx):
        dict = {"brand": "Ford", "model": "Mustang", "year": "1964"}
        x = dict.copy()
        emBed = discord.Embed(title="ลองใช้ dict.copy", description="", color=0x6F9DC3)
        emBed.add_field(name="ตัวอย่างโค้ด", value='dict = {\n"brand": "Ford",\n"model": "Mustang",\n"year": "1964"\n}\nx = dict.copy()\nprint(x)')
        emBed.add_field(name="ผลลัพธ์", value='{0}' .format(x))
        await ctx.channel.send(embed=emBed)

    # ลองใช้ fromkeys
    @commands.command()
    async def dfromkeys(self, ctx, *, par):
        dict = {"brand": "Ford", "model": "Mustang", "year": "1964"}
        y = str(par)
        x = dict.fromkeys(dict, y)
        emBed = discord.Embed(title="ลองใช้ dict.fromkeys", description="", color=0x6F9DC3)
        emBed.add_field(name="ตัวอย่างโค้ด", value='y = {0}\nx = dict.fromkeys(dict, y)\nprint(x)' .format(par))
        emBed.add_field(name="ผลลัพธ์", value='{0}' .format(x))
        await ctx.channel.send(embed=emBed)

    # ลองใช้ get
    @commands.command()
    async def dget(self, ctx, *, par):
        dict = {"brand": "Ford", "model": "Mustang", "year": "1964"}
        x = dict.get(par)
        emBed = discord.Embed(title="ลองใช้ dict.get", description="", color=0x6F9DC3)
        emBed.add_field(name="ตัวอย่างโค้ด", value='x = dict.get("{0}")\nprint(x)' .format(par))
        emBed.add_field(name="ผลลัพธ์", value='{0}' .format(x))
        await ctx.channel.send(embed=emBed)

    # ลองใช้ items
    @commands.command()
    async def ditems(self, ctx):
        dict = {"brand": "Ford", "model": "Mustang", "year": "1964"}
        x = dict.items()
        emBed = discord.Embed(title="ลองใช้ dict.items", description="", color=0x6F9DC3)
        emBed.add_field(name="ตัวอย่างโค้ด", value='dict = {\n"brand": "Ford",\n"model": "Mustang",\n"year": "1964"\n}\nx = dict.items()\nprint(x)')
        emBed.add_field(name="ผลลัพธ์", value='{0}' .format(x))
        await ctx.channel.send(embed=emBed)

    # ลองใช้ keys
    @commands.command()
    async def dkeys(self, ctx):
        dict = {"brand": "Ford", "model": "Mustang", "year": "1964"}
        x = dict.keys()
        emBed = discord.Embed(title="ลองใช้ dict.keys", description="", color=0x6F9DC3)
        emBed.add_field(name="ตัวอย่างโค้ด", value='dict = {\n"brand": "Ford",\n"model": "Mustang",\n"year": "1964"\n}\nx = dict.keys()\nprint(x)')
        emBed.add_field(name="ผลลัพธ์", value='{0}' .format(x))
        await ctx.channel.send(embed=emBed)

    # ลองใช้ pop
    @commands.command()
    async def dpop(self, ctx, *, par):
        dict = {"brand": "Ford", "model": "Mustang", "year": "1964"}
        dict.pop(par)
        emBed = discord.Embed(title="ลองใช้ dict.pop", description="", color=0x6F9DC3)
        emBed.add_field(name="ตัวอย่างโค้ด", value='dict.pop("{0}")\nprint(dict)' .format(par))
        emBed.add_field(name="ผลลัพธ์", value='{0}' .format(dict))
        await ctx.channel.send(embed=emBed)

    # ลองใช้ popitem
    @commands.command()
    async def dpopitem(self, ctx):
        dict = {"brand": "Ford", "model": "Mustang", "year": "1964"}
        dict.popitem()
        emBed = discord.Embed(title="ลองใช้ dict.keys", description="", color=0x6F9DC3)
        emBed.add_field(name="ตัวอย่างโค้ด", value='dict = {\n"brand": "Ford",\n"model": "Mustang",\n"year": "1964"\n}\ndict.popitem()\nprint(dict)')
        emBed.add_field(name="ผลลัพธ์", value='{0}' .format(dict))
        await ctx.channel.send(embed=emBed)

    # ลองใช้ setdefault
    @commands.command()
    async def dset(self, ctx, par, par2):
        dict = {"brand": "Ford", "model": "Mustang", "year": "1964"}
        x = dict.setdefault(par, par2)
        emBed = discord.Embed(title="ลองใช้ dict.setdefault", description="", color=0x6F9DC3)
        emBed.add_field(name="ตัวอย่างโค้ด", value='x = dict.setdefault("{0}", "{1}")\nprint(x)' .format(par, par2))
        emBed.add_field(name="ผลลัพธ์", value='{0}' .format(x))
        await ctx.channel.send(embed=emBed)

    # ลองใช้ update
    @commands.command()
    async def dupdate(self, ctx, par, par2):
        dict = {"brand": "Ford", "model": "Mustang", "year": "1964"}
        dict.update({par: par2})
        emBed = discord.Embed(title="ลองใช้ dict.update", description="", color=0x6F9DC3)
        emBed.add_field(name="ตัวอย่างโค้ด", value='dict.update({"{0}", "{1}"})\nprint(dict)' .format(par, par2))
        emBed.add_field(name="ผลลัพธ์", value='{0}' .format(dict))
        await ctx.channel.send(embed=emBed)

    # ลองใช้ popitem
    @commands.command()
    async def dvalues(self, ctx):
        dict = {"brand": "Ford", "model": "Mustang", "year": "1964"}
        x = dict.values()
        emBed = discord.Embed(title="ลองใช้ dict.keys", description="", color=0x6F9DC3)
        emBed.add_field(name="ตัวอย่างโค้ด", value='dict = {\n"brand": "Ford",\n"model": "Mustang",\n"year": "1964"\n}\nx = dict.values()\nprint(x)')
        emBed.add_field(name="ผลลัพธ์", value='{0}' .format(x))
        await ctx.channel.send(embed=emBed)

    # รับข้อความจาก User ใน Topic ต่างๆ
    @commands.Cog.listener("on_message")
    async def on_message(self, message):

        #Dictionary
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



    #Dict clear
        elif message.content == "!dict clear":
            emBed = discord.Embed(title="dict.clear", description="ใช้ลบข้อมูลทั้งหมดภายใน Dictionary", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='car =	{\n  "brand": "Ford",\n  "model": "Mustang",\n  "year": 1964\n}\ncar.clear()\nprint(car)')
            emBed.add_field(name="ผลลัพธ์", value='{}')
            emBed.add_field(name="ลองใช้ clear", value='โดยการพิม !dclear', inline=False)
            await message.channel.send(embed=emBed)
        



    #Dict copy
        elif message.content == "!dict copy":
            emBed = discord.Embed(title="dict.copy", description="ใช้คัดลอก Dictionary ทั้งหมดไปยังอันใหม่", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='car = {\n  "brand": "Ford",\n  "model": "Mustang",\n  "year": 1964\n}\nx = car.copy()\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value="{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}")
            emBed.add_field(name="ลองใช้ clear", value='โดยการพิม !dcopy', inline=False)
            await message.channel.send(embed=emBed)


    #Dict fromkeys
        elif message.content == "!dict fromkeys":
            emBed = discord.Embed(title="dict.fromkeys", description="ใช้คืนค่า dictionary ด้วย key หรือ value ที่กำหนด", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='x = ("key1", "key2", "key3")\ny = 0\nthisdict = dict.fromkeys(x, y)\nprint(thisdict)')
            emBed.add_field(name="ผลลัพธ์", value="['key1': 0, 'key2': 0, 'key3': 0]")
            emBed.add_field(name="ลองใช้ fromkeys", value='โดยการพิม !dfromkeys ค่า value ที่ต้องการ (dict คือ {"brand": "Ford", "model": "Mustang", "year": "1964"})', inline=False)
            await message.channel.send(embed=emBed)



    #Dict get
        elif message.content == "!dict get":
            emBed = discord.Embed(title="dict.get", description="ใช้ส่งค่าข้อมูลใน Dictionary จาก Key ที่กำหนด", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='car = {\n  "brand": "Ford",\n  "model": "Mustang",\n  "year": 1964\n}\nx = car.get("model")\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value='Mustang')
            emBed.add_field(name="ลองใช้ get", value='โดยการพิม !dget คีย์ที่ต้องการดู (dict คือ {"brand": "Ford", "model": "Mustang", "year": "1964"})', inline=False)
            await message.channel.send(embed=emBed)




    #Dict items
        elif message.content == "!dict items":
            emBed = discord.Embed(title="dict.items", description="ใช้ส่งค่ากลับเป็นออบเจ็คของ Key และ Value", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='car = {\n  "brand": "Ford",\n  "model": "Mustang",\n  "year": 1964\n}\nx = car.items()\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value="dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)]")
            emBed.add_field(name="ลองใช้ items", value='โดยการพิม !ditems', inline=False)
            await message.channel.send(embed=emBed)



    #Dict key
        elif message.content == "!dict keys":
            emBed = discord.Embed(title="dict.keys", description="ใช้ส่งค่ากลับเป็น List ของ Key ทั้งหมดใน Dictionary", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='car = {\n  "brand": "Ford",\n  "model": "Mustang",\n  "year": 1964\n}\nx = car.keys()\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value="dict_keys(['brand', 'model', 'year'])")
            emBed.add_field(name="ลองใช้ keys", value='โดยการพิม !dkeys', inline=False)
            await message.channel.send(embed=emBed)



    #Dict pop
        elif message.content == "!dict pop":
            emBed = discord.Embed(title="dict.pop", description="ใช้ส่งค่ากลับเป็นค่าสุดท้ายใน Dictionary", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='car = {\n  "brand": "Ford",\n  "model": "Mustang",\n  "year": 1964\n}\ncar.pop("model")\nprint(car)')
            emBed.add_field(name="ผลลัพธ์", value="{'brand': 'Ford', 'year': 1964}")
            emBed.add_field(name="ลองใช้ pop", value='โดยการพิม !dpop คีย์ที่ต้องการลบ (dict คือ {"brand": "Ford", "model": "Mustang", "year": "1964"})', inline=False)
            await message.channel.send(embed=emBed)


    #Dict popitem
        elif message.content == "!dict popitem":
            emBed = discord.Embed(title="dict.popitem", description="ใช้ส่งค่ากลับเป็น Tuple ออบเจ็คของ Key และ Value", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='car = {\n  "brand": "Ford",\n  "model": "Mustang",\n  "year": 1964\n}\ncar.popitem()\nprint(car)')
            emBed.add_field(name="ผลลัพธ์", value="{'brand': 'Ford', 'model': 'Mustang'}")
            emBed.add_field(name="ลองใช้ popitem", value='โดยการพิม !dpopitem', inline=False)
            await message.channel.send(embed=emBed)

        
    #Dict setdefault
        elif message.content == "!dict setdefault":
            emBed = discord.Embed(title="dict.setdefault", description="ใช้ส่งค่ากลับเป็นค่าของ Key ที่กำหนด ถ้าหากไม่มี Key อยู่ใส่ข้อมูลเข้าไปใน Dictionary", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='car = {\n  "brand": "Ford",\n  "model": "Mustang",\n  "year": 1964\n}\nx = car.setdefault("model", "Bronco")\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value='Mustang')
            emBed.add_field(name="ลองใช้ setdefault", value='โดยการพิม !dset (คีย์ที่ต้องการ, ค่า value *ทั้งสองตัวห้ามเว้นวรรค) (dict คือ {"brand": "Ford", "model": "Mustang", "year": "1964"})', inline=False)
            await message.channel.send(embed=emBed)


    #Dict update
        elif message.content == "!dict update":
            emBed = discord.Embed(title="dict.update", description="ใช้อัพเดท Dictionary กับคู่ของ Key และ Value จากออบเจ็คอื่น และเขียนทับ Key ที่มีอยู่", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='car = {\n  "brand": "Ford",\n  "model": "Mustang",\n  "year": 1964\n}\ncar.update({"color": "White"})\nprint(car)')
            emBed.add_field(name="ผลลัพธ์", value="{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'White'}")
            emBed.add_field(name="ลองใช้ update", value='โดยการพิม !dupdate (คีย์ที่ต้องการ, ค่า value *ทั้งสองตัวห้ามเว้นวรรค) (dict คือ {"brand": "Ford", "model": "Mustang", "year": "1964"})', inline=False)
            await message.channel.send(embed=emBed)


    #Dict values
        elif message.content == "!dict values":
            emBed = discord.Embed(title="dict.values", description="ใช้ส่งค่ากลับเป็น List ของ Value ทั้งหมดใน Dictionary", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='car = {\n  "brand": "Ford",\n  "model": "Mustang",\n  "year": 1964\n}\nx = car.values()\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value="dict_values(['Ford', 'Mustang', 1964])")
            emBed.add_field(name="ลองใช้ values", value='โดยการพิม !dvalues', inline=False)
            await message.channel.send(embed=emBed)
            

def setup(bot):
    bot.add_cog(dict_data(bot))

