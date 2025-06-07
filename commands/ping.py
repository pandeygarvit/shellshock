from discord import app_commands, Interaction

@app_commands.command(
  name="ping",
  description="Replies with Pong!"
)
async def ping(interaction: Interaction):
  await interaction.response.send_message("Pong!")
