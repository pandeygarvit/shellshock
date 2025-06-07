import docker

client = docker.from_env()

user_containers = {}

def start_challenge_container(user_id: int, image_name: str = "testchallenge:latest") -> str:
  if user_id in user_containers:
    return f"You already have a running container: `{user_containers[user_id].short_id}`"
  try:
    container = client.containers.run(
      image=image_name,
      detach=True,
      tty=True,
      stdin_open=True,
      mem_limit="128m",
      nano_cpus=int(0.25 * 1e9),      # 0.25 CPU = 250000000 nanocpus
      pids_limit=100,
      read_only=True,
      tmpfs={"/tmp": ""},
      network_mode="none",
      remove=True,  # Auto-remove after stop
      name=f"challenge_{user_id}"
    )
    user_containers[user_id] = container
    return f"Challenge container started! ID: `{container.short_id}`"
  except Exception as e:
    return f"Failed to start container: {str(e)}"