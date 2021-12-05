import discord
from discord.ext import commands

class lecture_replay(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    # ลองใช้ islower
    @commands.command()
    async def lecture(self, ctx):
        emBed = discord.Embed(title="รวมคลิป Lecture วิชา PSIT 2021", description="อาจารย์ผู้สอน รศ.ดร. โชติพัชร์ ภรณวลัย\n\n[PSIT2021 Week 01: Introduction](https://www.youtube.com/watch?v=l6Ui5svn-YU)\n"
        "[PSIT2021 Week 02: Conditionals](https://www.youtube.com/watch?v=KT_g3BiUMXc)\n"
        "[PSIT2021 Week 03: Problem Solving Framework](https://youtu.be/vzELf1LROws)\n"
        "[PSIT2021 Week 04: TurtleWorld](https://www.youtube.com/watch?v=vzELf1LROws)\n"
        "[PSIT2021 Week 05: Iteration](https://www.youtube.com/watch?v=gmlIJMB-478)\n"
        "[PSIT2021 Week 06: String and File part 1](https://www.youtube.com/watch?v=IpjYo9C9chw)\n"
        "[PSIT2021 Week 07: String and File part 2](https://www.youtube.com/watch?v=l6Ui5svn-YU)\n"
        "[PSIT2021 Week 08: List and Tuple part 1](https://www.youtube.com/watch?v=VKd2gckdyqU)\n"
        "[PSIT2021 Week 09: List and Tuple part 2](https://www.youtube.com/watch?v=iiYCZTt3FtU)\n"
        "[PSIT2021 Week 11: Dictionary, Set and Mix](https://www.youtube.com/watch?v=mX5EDoAOrb4)\n"
        "[PSIT2021 Week 13: Algorithm Complexity](https://www.youtube.com/watch?v=yrGqliqvx8A)\n"
        "[PSIT2021 Week 14: Recursion, Library, Goodies](https://www.youtube.com/watch?v=pve2p6NCOWo)\n"
        "[PSIT2021 Week 16: Standard Library, Third-Party Library, Greedy Algorithm](https://www.youtube.com/watch?v=VhAi3QGLj34)\n", color=0x6F9DC3)
        emBed.set_thumbnail(url="https://cdn.discordapp.com/attachments/908412010897743904/917076946372943922/Chotipat.jpg")
        emBed.set_footer(text="Created by 2P1B", icon_url="https://cdn.discordapp.com/attachments/895008902712807494/902127838344380446/image-removebg-preview.png")
        await ctx.send(embed=emBed)
    

def setup(bot):
    bot.add_cog(lecture_replay(bot))
