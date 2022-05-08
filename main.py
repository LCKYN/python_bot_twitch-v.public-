from config.twitchio_config import TwitchIOConfig
from constant.command_aliases import CommandAliases
from constant.computer_spec import ComputerSpec
from constant.game_category import GameCategory
from constant.user import User
from dialogue.command_not_found import CommandNotFound
from game.current_game import CurrentGame
from mapping.apex_legends_method_mapping import ApexLegendsMethodMapping
from mapping.valorant_method_mapping import ValorantMethodMapping
from mapping.game_mapping import GameMapping
from twitchio.ext import commands


class Main(commands.Bot):
    def __init__(self):
        super().__init__(
            token=TwitchIOConfig.TOKEN["tmi_token"],
            prefix=TwitchIOConfig.PREFIX,
            initial_channels=TwitchIOConfig.CHANNEL,
        )

        # attribute
        self.game_mapping = GameMapping().GAME_MAPPING
        self.method_mapping_from_game_name = {
            GameCategory.APEX_LEGENDS: ApexLegendsMethodMapping(),
            GameCategory.VALORANT: ValorantMethodMapping(),
        }

    # say hello when someone join
    async def event_join(self, channel, user):
        if user.name.lower() not in User.ignore_user:
            await self.connected_channels[0].send(f"Hello, {user.name}. Welcome to my channel 😍")

    @commands.command(name="apex", aliases=CommandAliases.GAME)
    async def apex(self, ctx: commands.Context, option: str = None):
        game = ctx.message.content[1:].split(" ")[0]
        game = game.lower()

        if game not in self.game_mapping:
            return

        game = self.game_mapping[game]

        if not option or option.lower() not in self.method_mapping_from_game_name[game].method_mapping:
            await ctx.send("Please enter an option such as rank, arena or info 🧐")
            await ctx.send(CommandNotFound.example[game])
            return

        # get data then send!!
        option = option.lower()
        output = self.method_mapping_from_game_name[game].method_mapping[option]()

        if isinstance(output, list):
            for text in output:
                await ctx.send(text)
            return

        if isinstance(output, str):
            await ctx.send(output)
            return

    @commands.command(name="rank", aliases=CommandAliases.OPTION)
    async def rank(self, ctx: commands.Context, game: str = None):
        command = ctx.message.content[1:].split(" ")[0]
        if not game:

            current_game = CurrentGame().get_current_game()
            if current_game == "" or current_game == GameCategory.JUST_CHATTING:
                await ctx.send(f"Now is {GameCategory.JUST_CHATTING}. Please enter a game such as apex, vlr 🥳")
                await ctx.send(CommandNotFound.example[game])
                return
            game = current_game

        game = game.lower()
        if game in GameMapping.GAME_MAPPING:
            output = self.method_mapping_from_game_name[GameMapping.GAME_MAPPING[game]].method_mapping[command]()

            if isinstance(output, list):
                for text in output:
                    await ctx.send(text)
                return

            if isinstance(output, str):
                await ctx.send(output)
                return

    @commands.command(name="spec", aliases=CommandAliases.COMPUTER_SPEC)
    async def computer_spec(self, ctx: commands.Context, game: str = None):
        command = ctx.message.content[1:].lower()
        if command == "spec":
            output = [f"{k}: {v}" for k, v in ComputerSpec.COMPUTER_SPEC.items()]
        elif command in ComputerSpec.COMPUTER_SPEC:
            output = f"{command}: {ComputerSpec.COMPUTER_SPEC[command]}"

        if isinstance(output, list):
            for text in output:
                await ctx.send(text)
            return

        if isinstance(output, str):
            await ctx.send(output)
            return


if __name__ == "__main__":
    bot = Main()
    bot.run()
