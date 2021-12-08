import discord
from discord.ext import commands

class list_data(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    # ลองใช้เมธอด List

    # ลองใช้ append
    @commands.command()
    async def append(self, ctx, *, par):
        list = []
        x = par
        list.append(x)
        emBed = discord.Embed(title="ลองใช้ append", description="", color=0x6F9DC3)
        emBed.add_field(name="ตัวอย่างโค้ด", value='list = "[]"\nx = {0}\nlist.append(x)' .format(par))
        emBed.add_field(name="ผลลัพธ์", value='{0}' .format(list))
        await ctx.channel.send(embed=emBed)

    # รับข้อความจาก User ใน Topic ต่างๆ
    @commands.Cog.listener("on_message")
    async def on_message(self, message):

        #  List
        if message.content == "!list":
            emBed = discord.Embed(title="List", description="List ใช้เก็บข้อมูลหลายๆ อันในตัวแปรเดียวอยู่ในกรอบสี่เหลี่ยม \
            \nList Method ที่ใช้บ่อยในการทำโจทย์พิมพ์ !list ตามด้วยชื่อ Method เพื่อเรียกดู", color=0x6F9DC3)
            emBed.add_field(name="append", value='เพิ่มสมาชิกใน List')
            emBed.add_field(name="clear", value='ลบสมาชิกทั้งหมดใน List')
            emBed.add_field(name="copy", value='คืนค่าทั้งหมดใน List')
            emBed.add_field(name="count", value='ตรวจสอบคำที่เจอว่ามีอยู่กี่ครั้ง')
            emBed.add_field(name="extend", value='ใช้เพิ่มข้อมูลเข้ามายัง List')
            emBed.add_field(name="index", value='ระบุตำแหน่งของข้อมูลแต่ละตัวที่อยู่ใน List')
            emBed.add_field(name="pop", value='ลบข้อมูลในตำแหน่งที่ระบุใน List')
            emBed.add_field(name="remove", value='ลบข้อมูลที่ระบุใน List')
            emBed.add_field(name="reverse", value='สลับข้อมูลทั้งหมดใน List')
            emBed.add_field(name="sort", value='เรียงตัวอักษรหรือตัวเลขจากน้อยไปมาก') 
            await message.channel.send(embed=emBed)

        #  List เมธอด append   
        elif message.content == "!list append":
            emBed = discord.Embed(title="list.append", description="ทำหน้าที่เพิ่มสมาชิกเข้าไปในตำเเหน่งสุดท้ายของ List", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='fruits = ["apple", "banana", "cherry"]\nx = fruits.append("orange")')
            emBed.add_field(name="ผลลัพธ์", value='["apple", "banana", "cherry", "orange"]')
            emBed.add_field(name="ลองใช้ append", value='โดยการ !lappend (ข้อความที่ต้องการ)', inline=False)
            await message.channel.send(embed=emBed)

        #  List เมธอด clear
        elif message.content == "!list clear":
            emBed = discord.Embed(title="list.clear", description="ทำหน้าที่ลบสมาชิกทั้งหมดใน List", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='fruits = ["apple", "banana", "cherry"]\nx = fruits.clear()')
            emBed.add_field(name="ผลลัพธ์", value="[]")
            emBed.add_field(name="ลองใช้ clear", value='โดยการพิม !lclear(ข้อความที่ต้องการ)', inline=False)
            await message.channel.send(embed=emBed)

        #  List เมธอด copy
        elif message.content == "!list copy":
            emBed = discord.Embed(title="list.copy", description="ทำหน้าที่คืนค่าทั้งหมดใน List", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='fruits = ["apple", "banana", "cherry"]\nx = fruits.copy()')
            emBed.add_field(name="ผลลัพธ์", value="[]")
            emBed.add_field(name="ลองใช้ copy", value='โดยการพิม !lcopy (ข้อความที่ต้องการ)', inline=False)
            await message.channel.send(embed=emBed)

        #  List เมธอด count
        elif message.content == "!list count":
            emBed = discord.Embed(title="list.count", description="ใช้ตรวจสอบว่ามีคำที่ปรากฏอยู่ในสตริงต้นทางกี่ครั้ง", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='fruits = ["apple", "banana", "cherry"]\nx = fruits.count("cherry")')
            emBed.add_field(name="ผลลัพธ์", value="1")
            emBed.add_field(name="ลองใช้ ", value='โดยการพิม !lcount (ข้อความที่ต้องการ)', inline=False)
            await message.channel.send(embed=emBed)

        #  List เมธอด extend
        elif message.content == "!list extend":
            emBed = discord.Embed(title="list.extend", description="ใช้เพิ่มข้อมูลจาก iterable มาต่อ List ไว้ข้างหลังอีกที", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value="fruits = ['apple', 'banana', 'cherry']\ncars = ['Ford', 'BMW', 'Volvo']\nx = fruits.extend(cars)")
            emBed.add_field(name="ผลลัพธ์", value='["apple", "banana", "cherry", "Ford", "BMW", "Volvo"]')
            emBed.add_field(name="ลองใช้ extend", value='โดยการพิม !lextend', inline=False)
            await message.channel.send(embed=emBed)

        #  List เมธอด index
        elif message.content == "!list index":
            emBed = discord.Embed(title="list.index", description="ทำหน้าที่ระบุตำแหน่งของข้อมูลแต่ละตัวที่อยู่ใน List", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='fruits =["apple", "banana", "cherry"]\nx = fruits.index("cherry")')
            emBed.add_field(name="ผลลัพธ์", value=2)
            emBed.add_field(name="ลองใช้ index", value='โดยการพิม !lindex', inline=False)
            await message.channel.send(embed=emBed)

        #  List เมธอด pop
        elif message.content == "!list pop":
            emBed = discord.Embed(title="list.pop", description="Method ที่ลบข้อมูลณ ตำแหน่งที่ระบุ", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='fruits =["apple", "banana", "cherry"]\nx = fruits.pop(1)')
            emBed.add_field(name="ผลลัพธ์", value=["apple", "cherry"])
            emBed.add_field(name="ลองใช้ pop", value='โดยการพิม !lpop (ข้อความที่ต้องการ)', inline=False)
            await message.channel.send(embed=emBed)

        #  List เมธอด remove
        elif message.content == "!list remove":
            emBed = discord.Embed(title="list.remove", description="Method ที่ลบข้อมูลที่ระบุ", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='fruits =["apple", "banana", "cherry"]\nx = fruits.remove("banana")')
            emBed.add_field(name="ผลลัพธ์", value=["apple", "cherry"])
            emBed.add_field(name="ลองใช้ remove", value='โดยการพิม !lremove (ข้อความที่ต้องการ)', inline=False)
            await message.channel.send(embed=emBed)

        #  List เมธอด reverse
        elif message.content == "!list reverse":
            emBed = discord.Embed(title="list.reverse", description="Method ทีย้อนกลับหรือสลับข้อมูลทั้งหมด", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='fruits =["apple", "banana", "cherry"]\nx = fruits.reverse()')
            emBed.add_field(name="ผลลัพธ์", value=["cherry", "banana", "apple"])
            emBed.add_field(name="ลองใช้ reverse", value='โดยการพิม !lreverse (ข้อความที่ต้องการ)', inline=False)
            await message.channel.send(embed=emBed)

        #  List เมธอด sort
        elif message.content == "!list sort":
            emBed = discord.Embed(title="list.sort", description="Method ทีใช้เรียงตัวอักษรหรือตัวเลขจากน้อยไปมาก เเละยังสามารถใช้ร่วมกับ reverse ได้ด้วย", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='cars = ["Ford", "BMW", "Volvo"]\nx = cars.sort()')
            emBed.add_field(name="ผลลัพธ์", value=["BMW", "Ford", "Volvo"])
            emBed.add_field(name="ลองใช้ sort", value='โดยการพิม !lsort (ข้อความที่ต้องการ)', inline=False)
            await message.channel.send(embed=emBed)
            

def setup(bot):
    bot.add_cog(list_data(bot))
