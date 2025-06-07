from discord import app_commands, Interaction

@app_commands.command(
  name="sync",
  description="Force sync all global commands"
)
async def manual_sync(interaction: Interaction):
  await interaction.response.defer(thinking=True)
  try:
    synced = await interaction.client.tree.sync()
    await interaction.followup.send(f"Synced {len(synced)} global command(s).")
  except Exception as e:
    await interaction.followup.send(f"Sync failed: {e}")