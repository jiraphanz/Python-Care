import discord
from discord.ext import commands

class lecture_replay(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    # ลองใช้ islower
    @commands.command()
    async def lecture(self, ctx):
        emBed = discord.Embed(title="รวมคลิป Lecture วิชา PSIT 2021", description="ลิงค์คลิปการเรียนการสอนทั้งหมด (กดที่ link เพื่อดูสื่อการสอนในสัปดาห์นั้นๆ):\n[PSIT2021 Week 01: Introduction](https://www.youtube.com/watch?v=l6Ui5svn-YU)\n"
        "[PSIT2021 Week 02: Conditionals](https://www.youtube.com/watch?v=KT_g3BiUMXc) [link](https://colab.research.google.com/drive/1Ce3t-jdJu5EGlzWufWkLVqoRLHJAyBEx)\n"
        "[PSIT2021 Week 03: Problem Solving Framework](https://youtu.be/vzELf1LROws)\n"
        "[PSIT2021 Week 04: TurtleWorld](https://www.youtube.com/watch?v=vzELf1LROws) [link](https://colab.research.google.com/drive/1NeRHeCVCvraFq6R-3euk5KvrT-DjJ-d-?usp=sharing&fbclid=IwAR1xyYSg535fvwhO1xuz2XrvBOVxPnu-cAKOcIskDrS4sjJ10LofHnAkNNc)\n"
        "[PSIT2021 Week 05: Iteration](https://www.youtube.com/watch?v=gmlIJMB-478) [link](https://colab.research.google.com/drive/1pLQq7hTKb6-09CJ0wZpMZTSMWRaHGuKj?usp=sharing&fbclid=IwAR2jDlbKP8XrfUtWznXp5whJrvgEJ8Z47uQpwefivrH-s28eQWxWeTrXqJw)\n"
        "[PSIT2021 Week 06: String and File part 1](https://www.youtube.com/watch?v=IpjYo9C9chw) [link](https://colab.research.google.com/drive/1BeGRinAn5BUplgaQVfEyHGOba0tejgck?usp=sharing&fbclid=IwAR3iqfZ1z2s92c4aIoxDqcePi9CC5DLdCTLXAhCCfm0v1WBHrwGEpjraoQc)\n"
        "[PSIT2021 Week 07: String and File part 2](https://www.youtube.com/watch?v=l6Ui5svn-YU) [link](https://colab.research.google.com/drive/1BeGRinAn5BUplgaQVfEyHGOba0tejgck?usp=sharing&fbclid=IwAR3iqfZ1z2s92c4aIoxDqcePi9CC5DLdCTLXAhCCfm0v1WBHrwGEpjraoQc)\n"
        "[PSIT2021 Week 08: List and Tuple part 1](https://www.youtube.com/watch?v=VKd2gckdyqU) [link](https://colab.research.google.com/drive/1vT1DcRYnRCUstYlFHDmh2TQUZC9WqHJk?usp=sharing&fbclid=IwAR1Vx_bhneA-s_c3Q0MM6b0u8U5r5KKdGS_TqpTcs6HdTBz7GLArFb61CF4)\n"
        "[PSIT2021 Week 09: List and Tuple part 2](https://www.youtube.com/watch?v=iiYCZTt3FtU) [link](https://colab.research.google.com/drive/1vT1DcRYnRCUstYlFHDmh2TQUZC9WqHJk?usp=sharing&fbclid=IwAR1Vx_bhneA-s_c3Q0MM6b0u8U5r5KKdGS_TqpTcs6HdTBz7GLArFb61CF4)\n"
        "[PSIT2021 Week 11: Dictionary, Set and Mix](https://www.youtube.com/watch?v=mX5EDoAOrb4) [link](https://colab.research.google.com/drive/117VPn9WTf2taTXlNKi7D8dLZI1-0v2iR)\n"
        "[PSIT2021 Week 13: Algorithm Complexity](https://www.youtube.com/watch?v=yrGqliqvx8A) [link](https://colab.research.google.com/drive/1OECqkEqPmaDPTh84Q7Er7mNNFusqNt3x)\n"
        "[PSIT2021 Week 14: Recursion, Library, Goodies](https://www.youtube.com/watch?v=pve2p6NCOWo) [link](https://colab.research.google.com/drive/1DOhyQDEsRV08vVsbotkr6xyjCCmtvkEd)\n"
        "[PSIT2021 Week 16: Standard Library, Third-Party Library, Greedy Algorithm](https://www.youtube.com/watch?v=VhAi3QGLj34) [link](https://colab.research.google.com/drive/1X4vd7wCgXOTP9YovbAui4KgNtXx-UNOH)\n", color=0x6F9DC3)
        emBed.set_thumbnail(url="https://cdn.discordapp.com/attachments/895008902712807494/902127838344380446/image-removebg-preview.png")
        emBed.set_footer(text="อาจารย์ผู้สอน รศ.ดร. โชติพัชร์ ภรณวลัย", icon_url="https://cdn.discordapp.com/attachments/908412010897743904/917076946372943922/Chotipat.jpg")
        await ctx.send(embed=emBed)
    

def setup(bot):
    bot.add_cog(lecture_replay(bot))
