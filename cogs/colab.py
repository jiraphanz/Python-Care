import discord
from discord.ext import commands

class colab(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    # ลองใช้ islower
    @commands.command()
    async def lecture(self, ctx):
        emBed = discord.Embed(title="รวมลิงค์ Google Colab Research ที่ใช้ในการเรียนการสอน วิชา PSIT 2021", description="ลิงค์ Google Colab Research การเรียนการสอนทั้งหมด:\n[PSIT2021 Week 01: Introduction](-)\n"
        "[PSIT2021 Week 02: Conditionals](https://colab.research.google.com/drive/1Ce3t-jdJu5EGlzWufWkLVqoRLHJAyBEx)\n"
        "[PSIT2021 Week 03: ](-)\n"
        "[PSIT2021 Week 04: TurtleWorld](https://colab.research.google.com/drive/1NeRHeCVCvraFq6R-3euk5KvrT-DjJ-d-?usp=sharing&fbclid=IwAR1xyYSg535fvwhO1xuz2XrvBOVxPnu-cAKOcIskDrS4sjJ10LofHnAkNNc)\n"
        "[PSIT2021 Week 05: Iteration](https://colab.research.google.com/drive/1pLQq7hTKb6-09CJ0wZpMZTSMWRaHGuKj?usp=sharing&fbclid=IwAR2jDlbKP8XrfUtWznXp5whJrvgEJ8Z47uQpwefivrH-s28eQWxWeTrXqJw)\n"
        "[PSIT2021 Week 06: String and Files](https://colab.research.google.com/drive/1BeGRinAn5BUplgaQVfEyHGOba0tejgck?usp=sharing&fbclid=IwAR3iqfZ1z2s92c4aIoxDqcePi9CC5DLdCTLXAhCCfm0v1WBHrwGEpjraoQc)\n"
        "[PSIT2021 Week 07: ](-)\n"
        "[PSIT2021 Week 08: List and Tuple part ](https://colab.research.google.com/drive/1vT1DcRYnRCUstYlFHDmh2TQUZC9WqHJk?usp=sharing&fbclid=IwAR1Vx_bhneA-s_c3Q0MM6b0u8U5r5KKdGS_TqpTcs6HdTBz7GLArFb61CF4)\n"
        "[PSIT2021 Week 09: Dictionary, Set and Mix](https://colab.research.google.com/drive/117VPn9WTf2taTXlNKi7D8dLZI1-0v2iR)\n"
        "[PSIT2021 Week 11: Algorithm Complexity](https://colab.research.google.com/drive/1OECqkEqPmaDPTh84Q7Er7mNNFusqNt3x)\n"
        "[PSIT2021 Week 13: ](-)\n"
        "[PSIT2021 Week 14: Recursion, Library, Goodies](https://colab.research.google.com/drive/1DOhyQDEsRV08vVsbotkr6xyjCCmtvkEd)\n"
        "[PSIT2021 Week 16: Standard Library, Third-Party Library, Greedy Algorithm](https://colab.research.google.com/drive/1X4vd7wCgXOTP9YovbAui4KgNtXx-UNOH)\n", color=0x6F9DC3)
        emBed.set_thumbnail(url="https://cdn.discordapp.com/attachments/895008902712807494/902127838344380446/image-removebg-preview.png")
        emBed.set_footer(text="อาจารย์ผู้สอน รศ.ดร. โชติพัชร์ ภรณวลัย", icon_url="https://cdn.discordapp.com/attachments/908412010897743904/917076946372943922/Chotipat.jpg")
        await ctx.send(embed=emBed)
    

def setup(bot):
    bot.add_cog(colab(bot))
