import defendatron

print("Activating facehugger shield...")
defendatron.activate(
    nullscream_blacklist=[
        "huggingface_hub.commands",
        "huggingface_hub.templates",
        "huggingface_hub._commit_api",
        "huggingface_hub._commit_scheduler",
        "huggingface_hub._infernece_endpoints",
        "huggingface_hub._login",
        "huggingface_hub._snapshot_download",
        "huggingface_hub._space_api",
        "huggingface_hub._tensorboard_logger",
        "huggingface_hub._webhooks_payload",
        "huggingface_hub._webhooks_server",
        "huggingface_hub.community",
        "huggingface_hub.fastai_utils",
        "huggingface_hub.file_download",
        "huggingface_hub.hf_api",
        "huggingface_hub.inference_api",
        "huggingface_hub.repocard",
        "huggingface_hub.repocard_data",
        "huggingface_hub.utils._gitcredential",
        "huggingface_hub.utils._headers",
        "huggingface_hub.utils._headers",
        "huggingface_hub.utils._telemetry",
        "transformers.utils.hub.PushToHubMixin",
    ],
    nullscream_whitelist=[
        "huggingface_hub.utils",
    ],
    activate_shadowlogger=True,
    activate_lockdown=True,
    activate_nullscream=True,
)
