import discord
from discord.ext import commands

class string_data(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    # ลองใช้เมธอด String

    # ลองใช้ islower
    @commands.command()
    async def islower(self, ctx, *, par):
        x = par.islower()
        emBed = discord.Embed(title="ลองใช้ islower", description="", color=0x6F9DC3)
        emBed.add_field(name="ตัวอย่างโค้ด", value='text = "{0}"\nx = text.islower()\nprint(x)' .format(par))
        emBed.add_field(name="ผลลัพธ์", value='{0}' .format(x))
        await ctx.channel.send(embed=emBed)

    # ลองใช้ count
    @commands.command()
    async def count(self, ctx, par, *, par2):
        x = par2.count(par)
        emBed = discord.Embed(title="ลองใช้ count", description="", color=0x6F9DC3)
        emBed.add_field(name="ตัวอย่างโค้ด", value='text = "{1}"\nx = text.count({0})\nprint(x)' .format(par, par2))
        emBed.add_field(name="ผลลัพธ์", value='{0}' .format(x))
        await ctx.channel.send(embed=emBed)

    # ลองใช้ capitalize
    @commands.command()
    async def cap(self, ctx, *, par):
        x = par.capitalize()
        emBed = discord.Embed(title="ลองใช้ capitalize", description="", color=0x6F9DC3)
        emBed.add_field(name="ตัวอย่างโค้ด", value='text = "{0}"\nx = text.capitalize()\nprint(x)' .format(par))
        emBed.add_field(name="ผลลัพธ์", value='{0}' .format(x))
        await ctx.channel.send(embed=emBed)
    
    # ลองใช้ center
    @commands.command()
    async def center(self, ctx, par, *, par2):
        x = par2.center(int(par))
        emBed = discord.Embed(title="ลองใช้ center", description="", color=0x6F9DC3)
        emBed.add_field(name="ตัวอย่างโค้ด", value='text = "{0}"\nx = text.center({1})\nprint(x)' .format(par2, par))
        emBed.add_field(name="ผลลัพธ์", value='{0}' .format(x))
        await ctx.channel.send(embed=emBed)

    # ลองใช้ find
    @commands.command()
    async def find(self, ctx, par, *, par2):
        x = par2.find(par)
        emBed = discord.Embed(title="ลองใช้ find", description="", color=0x6F9DC3)
        emBed.add_field(name="ตัวอย่างโค้ด", value='text = "{1}"\nx = text.find("{0}")\nprint(x)' .format(par, par2))
        emBed.add_field(name="ผลลัพธ์", value='{0}' .format(x))
        await ctx.channel.send(embed=emBed)

    # ลองใช้ index
    @commands.command()
    async def index(self, ctx, par, *, par2):
        x = par2.index(par)
        emBed = discord.Embed(title="ลองใช้ index", description="", color=0x6F9DC3)
        emBed.add_field(name="ตัวอย่างโค้ด", value='text = "{1}"\nx = text.index("{0}")\nprint(x)' .format(par, par2))
        emBed.add_field(name="ผลลัพธ์", value='{0}' .format(x))
        await ctx.channel.send(embed=emBed)

    # ลองใช้ isalnum
    @commands.command()
    async def isalnum(self, ctx, *, par):
        x = par.isalnum()
        emBed = discord.Embed(title="ลองใช้ isalnum", description="", color=0x6F9DC3)
        emBed.add_field(name="ตัวอย่างโค้ด", value='text = "{0}"\nx = text.isalnum()\nprint(x)' .format(par))
        emBed.add_field(name="ผลลัพธ์", value='{0}' .format(x))
        await ctx.channel.send(embed=emBed)

    # ลองใช้ isupper
    @commands.command()
    async def isupper(self, ctx, *, par):
        x = par.isupper()
        emBed = discord.Embed(title="ลองใช้ isupper", description="", color=0x6F9DC3)
        emBed.add_field(name="ตัวอย่างโค้ด", value='text = "{0}"\nx = text.isupper()\nprint(x)' .format(par))
        emBed.add_field(name="ผลลัพธ์", value='{0}' .format(x))
        await ctx.channel.send(embed=emBed)

    # ลองใช้ isnumeric
    @commands.command()
    async def isnumeric(self, ctx, *, par):
        x = par.isnumeric()
        emBed = discord.Embed(title="ลองใช้ isnumeric", description="", color=0x6F9DC3)
        emBed.add_field(name="ตัวอย่างโค้ด", value='text = "{0}"\nx = text.isnumeric()\nprint(x)' .format(par))
        emBed.add_field(name="ผลลัพธ์", value='{0}' .format(x))
        await ctx.channel.send(embed=emBed)

    # ลองใช้ ljust
    @commands.command()
    async def ljust(self, ctx, par, *, par2):
        x = par2.ljust(par)
        emBed = discord.Embed(title="ลองใช้ ljust", description="", color=0x6F9DC3)
        emBed.add_field(name="ตัวอย่างโค้ด", value='text = "{1}"\nx = text.ljust({0})\nprint(x)' .format(par, par2))
        emBed.add_field(name="ผลลัพธ์", value='{0}' .format(x))
        await ctx.channel.send(embed=emBed)

    # ลองใช้ lower
    @commands.command()
    async def lower(self, ctx, *, par):
        x = par.lower()
        emBed = discord.Embed(title="ลองใช้ lower", description="", color=0x6F9DC3)
        emBed.add_field(name="ตัวอย่างโค้ด", value='text = "{0}"\nx = text.lower()\nprint(x)' .format(par))
        emBed.add_field(name="ผลลัพธ์", value='{0}' .format(x))
        await ctx.channel.send(embed=emBed)

    # ลองใช้ lstrip
    @commands.command()
    async def lstrip(self, ctx, *, par):
        x = par.lstrip()
        emBed = discord.Embed(title="ลองใช้ lstrip", description="", color=0x6F9DC3)
        emBed.add_field(name="ตัวอย่างโค้ด", value='text = "{0}"\nx = text.lstrip()\nprint(x)' .format(par))
        emBed.add_field(name="ผลลัพธ์", value='{0}' .format(x))
        await ctx.channel.send(embed=emBed)

    # ลองใช้ replace
    @commands.command()
    async def replace(self, ctx, par, *, par2):
        text = "I love PSIT"
        x = text.replace(par, par2)
        emBed = discord.Embed(title="ลองใช้ replace", description="", color=0x6F9DC3)
        emBed.add_field(name="ตัวอย่างโค้ด", value='text = "I love PSIT"\nx = text.replace("{0}", "{1}")\nprint(x)' .format(par, par2))
        emBed.add_field(name="ผลลัพธ์", value='{0}' .format(x))
        await ctx.channel.send(embed=emBed)

    # ลองใช้ rfind
    @commands.command()
    async def rfind(self, ctx, par, *, par2):
        x = par2.rfind(par)
        emBed = discord.Embed(title="ลองใช้ rfind", description="", color=0x6F9DC3)
        emBed.add_field(name="ตัวอย่างโค้ด", value='text = "{1}"\nx = text.rfind("{0}")\nprint(x)' .format(par, par2))
        emBed.add_field(name="ผลลัพธ์", value='{0}' .format(x))
        await ctx.channel.send(embed=emBed)


    # ลองใช้ strip
    @commands.command()
    async def strip(self, ctx, *, par):
        x = par.strip()
        emBed = discord.Embed(title="ลองใช้ strip", description="", color=0x6F9DC3)
        emBed.add_field(name="ตัวอย่างโค้ด", value='text = "{0}"\nx = text.strip()\nprint(x)' .format(par))
        emBed.add_field(name="ผลลัพธ์", value='{0}' .format(x))
        await ctx.channel.send(embed=emBed)

    # ลองใช้ split
    @commands.command()
    async def split(self, ctx, par, *, par2):
        x = par2.split(par)
        emBed = discord.Embed(title="ลองใช้ split", description="", color=0x6F9DC3)
        emBed.add_field(name="ตัวอย่างโค้ด", value='text = "{1}"\nx = text.split("{0}")\nprint(x)' .format(par, par2))
        emBed.add_field(name="ผลลัพธ์", value='{0}' .format(x))
        await ctx.channel.send(embed=emBed)

    # ลองใช้ swapcase
    @commands.command()
    async def swapcase(self, ctx, *, par):
        x = par.swapcase()
        emBed = discord.Embed(title="ลองใช้ swapcase", description="", color=0x6F9DC3)
        emBed.add_field(name="ตัวอย่างโค้ด", value='text = "{0}"\nx = text.swapcase()\nprint(x)' .format(par))
        emBed.add_field(name="ผลลัพธ์", value='{0}' .format(x))
        await ctx.channel.send(embed=emBed)

    # ลองใช้ upper
    @commands.command()
    async def upper(self, ctx, *, par):
        x = par.upper()
        emBed = discord.Embed(title="ลองใช้ upper", description="", color=0x6F9DC3)
        emBed.add_field(name="ตัวอย่างโค้ด", value='text = "{0}"\nx = text.upper()\nprint(x)' .format(par))
        emBed.add_field(name="ผลลัพธ์", value='{0}' .format(x))
        await ctx.channel.send(embed=emBed)

    # ลองใช้ rsplit


    
    # รับข้อความจาก User ใน Topic ต่างๆ
    @commands.Cog.listener("on_message")
    async def on_message(self, message):

         # String
        if message.content == "!string":
            emBed = discord.Embed(title="String", description="String ในภาษาไพทอน จะถูกล้อมไปด้วย Single Quote\
            หรือ Double Quote\nString Method ที่ใช้บ่อยในการทำโจทย์พิมพ์ !string ตามด้วยชื่อ Method เพื่อเรียกดู", color=0x6F9DC3)
            emBed.add_field(name="capitalize", value='เปลี่ยนตัวแรกให้เป็นตัวพิมพ์ใหญ่')
            emBed.add_field(name="lower", value='เเปลงข้อความตัวใหญ๋ให้เป็นตัวเล็ก')
            emBed.add_field(name="upper", value='เปลี่ยนข้อความให้เป็นตัวใหญ่ทั้งหมด')
            emBed.add_field(name="swapcase", value='สลับข้อความตัวเล็กให้เป็นตัวใหญ่เเละสลับข้อความตัวใหญ่ให้เป็นตัวเล็ก')
            emBed.add_field(name="islower", value='เช็คว่าเป็นตัวพิมพ์เล็กทั้งหมดไหม')
            emBed.add_field(name="isalnum", value='เช็คว่ามีตัวอักษรหรือตัวเลขไหม')
            emBed.add_field(name="isalpha", value='เช็คว่าเป็นตัวอักษรไหม')
            emBed.add_field(name="isupper", value='เช็คว่าเป็นตัวพิมพ์ใหญ่ทั้งหมดไหม')
            emBed.add_field(name="isnumeric", value='เช็คว่าเป็นตัวเลขไหม')
            emBed.add_field(name="ljust", value='ทำให้ข้อความอยู่ฝั่งซ้าย')
            emBed.add_field(name="rjust", value='ทำให้ข้อความอยู่ฝั่งขวา')
            emBed.add_field(name="strip", value='ทำหน้าที่นำช่องว่างทั้้งซ้ายเเละขวาออก')
            emBed.add_field(name="lstrip", value='ทำหน้าที่เอาช่องว่างด้านซ้ายของข้อความออก')
            emBed.add_field(name="count", value='นับจำนวนตัวอักษรในข้อความ')
            emBed.add_field(name="center", value='จัดข้อความให้อยู่ตรงกลาง')
            emBed.add_field(name="find", value='หาตำเเหน่งของข้อความ')
            emBed.add_field(name="index", value='บอกตำเเหน่งของข้อความ')
            emBed.add_field(name="replace", value='เเทนที่ข้อความเก่าด้วยข้อความใหม่')
            emBed.add_field(name="rfind", value='หาตำเเหน่งข้อความจากทางด้านขวา')
            emBed.add_field(name="split", value='เปลี่ยนข้อความเป็น List')
            # emBed.add_field(name="rsplit", value='แยกข้อความเป็นลิสต์โดยใช้คอมม่าและตามด้วยวรรค')
            await message.channel.send(embed=emBed)


        # String เมธอด islower
        elif message.content == "!string islower":
            emBed = discord.Embed(title="string.islower", description="เช็คตัวอักษรทั้งหมดในข้อความว่าเป็นตัวพิมพ์เล็กหรือไม่ถ้าใช่จะ Return ค่าออกมาเป็น True", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "hello world!"\nx = txt.islower()\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value='True')
            emBed.add_field(name="ลองใช้ islower", value='โดยการพิม !islower ข้อความที่ต้องการ', inline=False)
            await message.channel.send(embed=emBed)

        # String เมธอด capitalize
        elif message.content == "!string capitalize":
            emBed = discord.Embed(title="string.capitalize", description="เปลี่ยนตัวอักษรตัวเเรกของประโยคให้เป็นตัวใหญ่เเล้วเปลี่ยนตัวอักษรที่เหลือเป็นตัวเล็ก", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "hello World!"\nx = txt.capitalize()\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value='Hello world!')
            emBed.add_field(name="ลองใช้ capitalize", value='โดยการพิม !cap ข้อความที่ต้องการ', inline=False)
            await message.channel.send(embed=emBed)

        # String เมธอด count
        elif message.content == "!string count":
            emBed = discord.Embed(title="string.count", description="แสดงจำนวนของตัวอักษรที่เราเจอในข้อความตามที่เรากำหนด", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "Psit is veryhard hard"\nx = txt.count("hard")\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value='2')
            emBed.add_field(name="ตัวอย่างเพิ่มเติม", value='สามารถใส่ค่าว่าจะให้เริ่มนับตั้งเเต่ตำเเหน่งไหนและหยุดนับที่ตำแหน่งไหน', inline=False)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "Psit is veryeasy easy" \n x = txt.count("easy", 10, 17)\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value='1')
            emBed.add_field(name="ลองใช้ count", value='โดยการพิม !count คำที่จะนับ, ข้อความที่ต้องการ', inline=False)
            await message.channel.send(embed=emBed)

        # String เมทธอด center
        elif message.content == "!string center":
            emBed = discord.Embed(title="string.center", description="ทำหน้าที่จัดข้อความให้อยู่ตรงกลาง ", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "banana"\nx = txt.count("20")\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value='       banana       ')
            emBed.add_field(name="ตัวอย่างเพิ่มเติม", value='สามารถกำหนดช่องว่างซ้ายขวาให้เป็นตัวเลขหรือตัวอักษรได้เเต่มีข้อระวังคือต้องทำเป็นข้อความเท่านั้น', inline=False)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "banana" \n x = txt.count("20", "O")\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value='OOOOOOObananaOOOOOOO')
            emBed.add_field(name="ลองใช้ center", value='โดยการพิม !center ความยาว, ข้อความต้องการ', inline=False)
            await message.channel.send(embed=emBed)
        
        # String เมทธอด find
        elif message.content == "!string find":
            emBed = discord.Embed(title="string.find", description="หาตำเเหน่งของข้อความที่กำหนดโดยจะเริ่มนับจาก0เเละถ้าหาไม่เจอจะ Return nค่าออกมาเป็น -1 ", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "Hello, welcome to my world."\nx = txt.find("welcome")\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value=7)
            emBed.add_field(name="ตัวอย่างเพิ่มเติม", value='สามารถใส่ค่าเพื่อให้เริ่มหาตำเเหน่งที่ตำเเหน่งไหนเเละหยุดหาที่ตำเเเหน่งไหน', inline=False)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "Hello, welcome to my world." \n x = txt.find("e", 5, 10)\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value=8)
            emBed.add_field(name="ลองใช้ find", value='โดยการพิม !find คำที่จะหา, ข้อความที่ต้องการ', inline=False)
            await message.channel.send(embed=emBed)
        
        # String เมทธอด index
        elif message.content == "!string index":
            emBed = discord.Embed(title="string.index", description="บอกตำเเหน่งของข้อความที่กำหนดโดยจะเริ่มนับจาก 0 เเละถ้าหาไม่เจอจะ Error", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "Hello, welcome to my world."\nx = txt.index("e")\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value=1)
            emBed.add_field(name="ตัวอย่างเพิ่มเติม", value='สามารถใส่ค่าเพื่อให้เริ่มหาตำเเหน่งที่ตำเเหน่งไหนเเละหยุดหาที่ตำเเเหน่งไหน', inline=False)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "Hello, welcome to my world." \n x = txt.find("e", 5, 10)\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value=8)
            emBed.add_field(name="ลองใช้ center", value='โดยการพิม !index ตำเเหน่งที่จะให้เริ่มหา, ตำเเหน่งที่จะให้หยุดหา, ข้อความที่ต้องการ', inline=False)
            await message.channel.send(embed=emBed)
        
        # String เมทธอด isalnum
        elif message.content == "!string isalnum":
            emBed = discord.Embed(title="string.isalnum", description="เช็คข้อความทุกตัวว่าเป็น Alphabet(a-z) เเละมีเลข (0-9) ไหมถ้าตรงตามเงื่อนไขจะ Return ออกมาเป็น True", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "Company12"\nx = txt.isalnum()\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value=True)
            emBed.add_field(name="ลองใช้ isalnum", value='โดยการพิม !isalnum ข้อความที่ต้องการ', inline=False)
            await message.channel.send(embed=emBed)
        
        # String เมทธอด isalpha
        elif message.content == "!string isalpha":
            emBed = discord.Embed(title="string.isalpha", description= "จะ Return ค่าเป็น True เมื่อข้อความทุกตัวเป็น Alphabet(a-z)", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "Company"\nx = txt.isalpha()\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value=True)
            emBed.add_field(name="ลองใช้ isalpha", value='โดยการพิม !isalpha ข้อความที่ต้องการ', inline=False)
            await message.channel.send(embed=emBed)
        
        # String เมทธอด isnumeric
        elif message.content == "!string isnumeric":
            emBed = discord.Embed(title="string.isnumeric", description="จะ Return ค่าเป็น True เมื่อข้อความเป็นตัวเลขทั้งหมด", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "1234345"\nx = txt.isnumeric()\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value=True)
            emBed.add_field(name="ลองใช้ isalpha", value='โดยการพิม !isnumeric ข้อความที่ต้องการ', inline=False)
            await message.channel.send(embed=emBed)
        
        # String เมทธอด isupper
        elif message.content == "!string isupper":
            emBed = discord.Embed(title="string.isupper", description="จะ Return ค่าเป็น True เมื่อข้อความเป็นตัวเลขใหญ่ทั้งหมด", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "CENTER"\nx = txt.isupper()\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value=True)
            emBed.add_field(name="ลองใช้ isalpha", value='โดยการพิม !isupper ข้อความที่ต้องการ', inline=False)
            await message.channel.send(embed=emBed)
        
        # String เมทธอด ljust
        elif message.content == "!string ljust":
            emBed = discord.Embed(title="string.ljust", description="จะ Return ค่าข้อความชิดซ้ายเเล้วช่องว่างที่เหลือจะอยู่ด้านขวา", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "banana"\nx = txt.ljust(20)\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value="banana              ")
            emBed.add_field(name="ตัวอย่างเพิ่มเติม", value='สามารถใส่ค่าเพิ่มอีกตัวเพื่อเปลี่ยนจากช่องว่างเป็น String', inline=False)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "banana" \n x = txt.ljust(20, "O"\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value="bananaOOOOOOOOOOOOOO")
            emBed.add_field(name="ลองใช้ ljust", value='โดยการพิม !ljust ความยาว, ข้อความที่ต้องการ', inline=False)
            await message.channel.send(embed=emBed)
        
        # String เมทธอด lower
        elif message.content == "!string lower":
            emBed = discord.Embed(title="string.lower", description="เเปลงข้อความตัวใหญ๋ให้เป็นตัวเล็ก", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "OOP"\nx = txt.lower()\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value="oop")
            emBed.add_field(name="ลองใช้ lower", value='โดยการพิม !lower ข้อความที่ต้องการ', inline=False)
            await message.channel.send(embed=emBed)
        
        # String เมทธอด lstrip
        elif message.content == "!string lstrip":
            emBed = discord.Embed(title="string.lstrip", description="ทำหน้าที่เอาช่องว่างด้านซ้ายของข้อความออก", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "       OOP  "\nx = txt.lstrip()\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value="OOP  ")
            emBed.add_field(name="ตัวอย่างเพิ่มเติม", value='สามารถนำข้อความที่ไม่ต้องการทางด้านซ้ายออกได้โดยการใส่ข้อความที่ต้องการนำออกไป', inline=False)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "aaaaOOPmm"\nx = txt.lstrip("a")\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value="OOPmm")
            emBed.add_field(name="ลองใช้ lstrip", value='โดยการพิม !lstrip ข้อความที่มีช่องว่างด้านซ้าย', inline=False)
            await message.channel.send(embed=emBed)
        
        # String เมทธอด replace
        elif message.content == "!string replace":
            emBed = discord.Embed(title="string.replace", description="เเทนที่ข้อความเก่าด้วยข้อความใหม่", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "I like bananas"\nx = txt.replace("bananas", "apples")\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value="I like apples")
            emBed.add_field(name="ตัวอย่างเพิ่มเติม", value='ถ้ามีคำซ้ำหลายๆคำสามารถกำหนดได้ว่าจะเเทนเเค่กี่คำ', inline=False)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "one one was a race horse, two was one too."\nx = txt.replace("one", "five", 2)\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value="five five was a race horse, two was one too.")
            emBed.add_field(name="ลองใช้ replace", value='โดยการพิม !replace คำที่ต้องการแทนที่, คำที่จะแทนที่ (ข้อความคือ I love PSIT) ', inline=False)
            await message.channel.send(embed=emBed)
        
        # String เมทธอด rfind
        elif message.content == "!string rfind":
            emBed = discord.Embed(title="string.rfind", description="หาตำเเหน่งจากทางด้านขวาโดยจะเริ่มจาก 0 จะนับตำเเหน่งปกติเเต่จะเอาตำเเหน่งด้านขวาก่อน", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "Hello, welcome to my world."\nx = txt.rfind("e")\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value=13)
            emBed.add_field(name="ตัวอย่างเพิ่มเติม", value='สามารถใส่ค่าเพื่อให้เริ่มหาตำเเหน่งที่ตำเเหน่งไหนเเละหยุดหาที่ตำเเเหน่งไหน', inline=False)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "Hello, welcome to my world."\nx = txt.rfind("e", 5, 10)\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value=8)
            emBed.add_field(name="ลองใช้ rfind", value='โดยการพิม !rfind คำที่ต้องการหา ข้อความที่ต้องการ', inline=False)
            await message.channel.send(embed=emBed)
        
        # String เมทธอด rjust
        elif message.content == "!string rjust":
            emBed = discord.Embed(title="string.rjust", description="Return ค่าออกมาในรูปเเบบที่ข้อความชิดขวาเเล้วช่องว่างอยู่ซ้าย", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "banana"\nx = txt.rjust(20)\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value="              banana")
            emBed.add_field(name="ตัวอย่างเพิ่มเติม", value='สามารถใส่ค่าเพิ่มอีกตัวเพื่อเปลี่ยนจากช่องว่างเป็น String', inline=False)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "banana"\nx = txt.rjust(20, "O")\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value="OOOOOOOOOOOOOObanana")
            # emBed.add_field(name="ลองใช้ rjust", value='โดยการพิม !rjust ข้อความที่ต้องการให้เเทนที่ช่องว่าง', inline=False)
            await message.channel.send(embed=emBed)
        
        # # String เมทธอด rsplit
        # elif message.content == "!string rsplit":
        #     emBed = discord.Embed(title="string.rsplit", description="", color=0x6F9DC3)
        #     emBed.add_field(name="ตัวอย่างโค้ด", value='txt = ""\nx = txt.()\nprint(x)')
        #     emBed.add_field(name="ผลลัพธ์", value="")
        #     emBed.add_field(name="ตัวอย่างเพิ่มเติม", value='', inline=False)
        #     emBed.add_field(name="ตัวอย่างโค้ด", value='txt = ""\nx = txt.()\nprint(x)')
        #     emBed.add_field(name="ผลลัพธ์", value="")
        #     emBed.add_field(name="ลองใช้ rsplit", value='โดยการพิม !rsplit ข้อความที่มีช่องว่างด้านซ้าย', inline=False)
        #     await message.channel.send(embed=emBed)
        
        # String เมทธอด strip
        elif message.content == "!string strip":
            emBed = discord.Embed(title="string.strip", description="ทำหน้าที่นำช่องว่างทั้้งซ้ายเเละขวาออก", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "     banana     "\nx = txt.strip()\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value="banana")
            emBed.add_field(name="ตัวอย่างเพิ่มเติม", value='สามารถกำหนดว่าจะเอาข้อความตัวไหนออก', inline=False)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "mmmbananammm"\nx = txt.strip("mmm")\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value="banana")
            emBed.add_field(name="ลองใช้ strip", value='โดยการพิม !strip ข้อความที่มีช่องว่าง', inline=False)
            await message.channel.send(embed=emBed)
    
        # String เมทธอด split
        elif message.content == "!string split":
            emBed = discord.Embed(title="string.split", description="นำข้อความที่ไม่ต้องการออกเเละเเปลงข้อความที่เหลือให้อยู่ในรูปเเบบของ List", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "apple#banana#cherry#orange""\nx = txt.split("#")\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value="['apple', 'banana', 'cherry', 'orange']")
            emBed.add_field(name="ตัวอย่างเพิ่มเติม", value='สามารถกำหนดว่าจะเอาstringตัวทีจะให้เอาออกกี่ตัว', inline=False)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "apple#banana#cherry#orange""\nx = txt.split("#", 1)\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value="['apple', 'banana#cherry#orange']")
            emBed.add_field(name="ลองใช้ split", value='โดยการพิม !split คำที่ต้องการเอาออก, ข้อความที่ต้องการ', inline=False)
            await message.channel.send(embed=emBed)

        # String เมทธอด swapcase
        elif message.content == "!string swapcase":
            emBed = discord.Embed(title="string.swapcase", description="สลับข้อความตัวเล็กให้เป็นตัวใหญ่เเละสลับข้อความตัวใหญ่ให้เป็นตัวเล็ก", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "Apple bANANA"\nx = txt.swapcase()\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value="aPPLE Bnana")
            emBed.add_field(name="ลองใช้ swapcase", value='โดยการพิม !swapcase ข้อความที่ต้องการ', inline=False)
            await message.channel.send(embed=emBed)

        # String เมทธอด upper
        elif message.content == "!string upper":
            emBed = discord.Embed(title="string.upper", description="เปลี่ยนข้อความให้เป็นตัวใหญ่ทั้งหมด", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "apple"\nx = txt.upper()\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value="APPLE")
            emBed.add_field(name="ลองใช้ upper", value='โดยการพิม !upper ข้อความ', inline=False)
            await message.channel.send(embed=emBed)




def setup(bot):
    bot.add_cog(string_data(bot))
