import defendatron
from facehuggershield.huggingface.set_environment_variables import set_huggingface_environment_variables

print("Activating facehugger shield...")
def activate(
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
        "transformers.tools.agents",
    ],
    nullscream_whitelist=[
    ],
    nullscream_function_blacklist=[],
    activate_shadowlogger=True,
    activate_darklock=True,
    activate_nullscream=True,
    show_stdout=True
):
    set_huggingface_environment_variables(
        allow_downloads=False,

    )
    defendatron.activate(
        nullscream_blacklist=nullscream_blacklist,
        nullscream_whitelist=nullscream_whitelist,
        nullscream_function_blacklist=nullscream_function_blacklist,
        activate_shadowlogger=activate_shadowlogger,
        activate_darklock=activate_darklock,
        activate_nullscream=activate_nullscream,
        show_stdout=show_stdout
    )
