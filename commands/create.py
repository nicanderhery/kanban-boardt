"""
This module contains the create command for the kanban bot.
"""
import discord

from client import client


@client.tree.command()
@discord.app_commands.describe(name="Project's name")
async def create(interaction: discord.Interaction, name: str) -> None:
    """
    Creates a project with the given name.
    Args:
        interaction (discord.Interaction): The interaction that triggered this command.
        name (str): The name of the project.
    """
    response = interaction.response

    # Return error if the command is not used in a server or by a member
    if not interaction.guild:
        return await response.send_message(f"{interaction.user.mention}\n"
                                           f"This command can only be used in a server",
                                           ephemeral=True)
    if not isinstance(interaction.user, discord.Member):
        return await response.send_message(f"{interaction.user.mention}\n"
                                           f"This command can only be used by a member",
                                           ephemeral=True)

    # TODO: Check if project already exists in the database

    # Defers the response to avoid the 3 seconds timeout and replace response with followup
    await response.defer(ephemeral=True)
    response = interaction.followup

    categories = ("Product Backlog", "Sprint Backlog", "In Progress", "Done")
    try:
        # Create the category channels for the project in discord
        product_categories = [await interaction.guild.create_category(f"{name} - {category}")
                              for category in categories]
        for category in product_categories:
            # Limit the permissions of the project channels
            await category.set_permissions(interaction.guild.me,
                                           view_channel=True, manage_channels=True)
            await category.set_permissions(interaction.user,
                                           view_channel=True, manage_channels=True)
            await category.set_permissions(interaction.guild.default_role, view_channel=False)
            # TODO: Add the board to the database

        # TODO: Add the project to the database
        # Confirm that the project was created successfully
        await response.send(f"{interaction.user.mention}\n"
                            f"Project {name} created successfully.")

    except discord.HTTPException as error:
        await response.send(f"{interaction.user.mention}\n"
                            f"An error occurred while creating the project",
                            embed=discord.Embed(description=str(error), color=discord.Color.red()))
