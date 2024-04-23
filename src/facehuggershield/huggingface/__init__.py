########################################################################
# Importing an installing this module disables certain modules.
########################################################################
from nullscream import install_nullscream
install_nullscream(
    blacklist=[
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
    whitelist=[
        "huggingface_hub.utils",
    ]
)

########################################################################
# Importing this module ensures that the internet is completely disabled
########################################################################

from lockdown.network import no_internet_socket


########################################################################
# Importing this module ensures that disk access is restricted
########################################################################

from lockdown.os.restrict_os_access import RestrictOSAccess
restrict_os_access = RestrictOSAccess()
restrict_os_access.install()
