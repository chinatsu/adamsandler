from discord.ext import commands
import discord
import random
from stats import origins, races, genders, attributes, startingskills, civilskills, talents, weapons, defence, instruments, tags
import pprint

class Divinity():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="test")
    async def testcommand(self):
        await self.bot.say("I'm 31 now. I think I'm beginning to understand what life is, what romance is, and what a relationship means.")

    @commands.command(name="memebuild")
    async def memebuild(self):
        build = {"origin": random.choice(origins + races),
                 "civil_abilities": [random.choice(civilskills)],
                 "attributes": [],
                 "combat_abilities": [],
                 "skills": [],
                 "instrument": random.choice(instruments),
                 "tags": []
        }

        build["gender"] = random.choice(genders) if build["origin"] in races else "Default"

        attributepoints = 3

        if build["origin"] == "Human": build["civil_abilities"].append("Bartering")
        elif build["origin"] == "Elf": build["civil_abilities"].append("Loremaster")
        elif build["origin"] == "Dwarf": build["civil_abilities"].append("Sneaking")
        elif build["origin"] == "Lizard": build["civil_abilities"].append("Persuasion")

        for _ in range(0, 2):
            ability = random.choice(list(startingskills.keys()) + weapons + defence)
            if ability == "Polymorph":
                attributepoints += 1
            build["combat_abilities"].append(ability)

        if build["combat_abilities"][0] in list(startingskills.keys()) and build["combat_abilities"][1] in list(startingskills.keys()):
            c = 3 - random.randint(1, 2)
        elif build["combat_abilities"][0] not in list(startingskills.keys()) and build["combat_abilities"][1] not in list(startingskills.keys()):
            c = 0
        else:
            c = 3

        for idx, ability in enumerate(build["combat_abilities"]):
            if ability in startingskills.keys():
                for _ in range(0, c):
                    skill = random.choice(startingskills[ability])
                    while skill in build["skills"]:
                        skill = random.choice(startingskills[ability])
                    build["skills"].append(skill)
                c = 3 - c

        for _ in range(0, attributepoints):
            build["attributes"].append(random.choice(attributes))

        for _ in range(0, 2):
            tag = random.choice(tags)
            while tag in build["tags"]:
                tag = random.choice(tags)
            build["tags"].append(tag)

        while True:
            talent = random.choice(talents)
            if talent not in ["Demon", "Duck Duck Goose", "Elemental Ranger", "Executioner", "Guerilla", "Ice King", "The Pawn", "Picture of Health"]:
                break
            elif talent == "Demon" and "Pyrokinetic" in build["combat_abilities"]: break
            elif talent == "Duck Duck Goose" and "Huntsman" in build["combat_abilities"]: break
            elif talent == "Elemental Ranger" and "Huntsman" in build["combat_abilities"]: break
            elif talent == "Executioner" and "Warfare" in combatabailities: break
            elif talent == "Guerilla" and "Sneaking" in civilskills: break
            elif talent == "Ice King" and "Hydrosophist" in build["combat_abilities"]: break
            elif talent == "The Pawn" and "Scoundrel" in build["combat_abilities"]: break
            elif talent == "Picture of Health" and "Warfare" in build["combat_abilities"]: break
        build["talent"] = talent

        embed=discord.Embed(title="Your new character", color=0xd78cff)
        embed.add_field(name="Origin", value=build["origin"], inline=True)
        if build["gender"] != "Default": embed.add_field(name="Gender", value=build["gender"], inline=True)
        embed.add_field(name="Attributes", value=", ".join(build["attributes"]), inline=False)
        embed.add_field(name="Civil Abilities", value=build["civil_abilities"][0], inline=False)
        embed.add_field(name="Combat Abilities", value=", ".join(build["combat_abilities"]), inline=True)
        embed.add_field(name="Skills", value=", ".join(build["skills"]) if len(build["skills"]) > 0 else "None", inline=True)
        embed.add_field(name="Talents", value=build["talent"], inline=True)
        embed.add_field(name="Tags", value=", ".join(build["tags"]), inline=True)
        embed.add_field(name="Instrument", value=build["instrument"], inline=True)
        await self.bot.say(embed=embed)

def setup(bot):
    bot.add_cog(Divinity(bot))
