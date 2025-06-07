from discord import app_commands, Interaction
from service.docker_manager import start_challenge_container

@app_commands.command(
  name="start-challenge",
  description="Starts new cyber escape room challenge"
)
async def start_challenge(interaction: Interaction):
  await interaction.response.defer(thinking=True)

  user_id = interaction.user.id
  response = start_challenge_container(user_id)

  await interaction.followup.send(response)