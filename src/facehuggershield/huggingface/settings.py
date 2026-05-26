"""
====================================================================
--------------------------------------------------------------------
HUGGINGFACE ENVIRONMENT VARIABLES WARNING
--------------------------------------------------------------------
====================================================================

====================================================================
--------------------------------------------------------------------
HUGGINGFACE.CO IS A WEBSITE THAT HOSTS AI MODELS AND ALLOWS PEOPLE
TO CREATE SERVERS THAT CAN USE THESE MODELS. SOME OF THE DEFAULT
SETTINGS PRESENT A SECURITY RISK. HUGGINGFACE.CO LIBRARIES SHOULD
FIX THEIR DEFAULT SETTINGS AND REMOVE THE ABILITY TO DOWNLOAD AND
EXECUTE CODE. CAREFULLY READ THE FOLLOWING SETTINGS AND COMMENTS
BEFORE YOU CHANGE ANYTHING. DO NOT CHANGE ANYTHING UNLESS YOU KNOW
WHAT YOU ARE DOING.
--------------------------------------------------------------------
====================================================================
"""

"""Environment defaults for Hugging Face privacy and sandboxing."""
import os

####################################################################
# This flag controls whether the host application may temporarily
# opt into downloads while using the policy pack.
####################################################################
HF_ALLOW_DOWNLOADS = True

####################################################################
# HF_HUB_DISABLE_TELEMETRY is used to disable telemetry for
# huggingface models. Never enable telemetry. Setting this to "0"
# will send telemetry to huggingface. Huggingface libraries should
# NOT have the ability to send telemetry.
####################################################################
HF_HUB_DISABLE_TELEMETRY = "1"  # Never change this variable

####################################################################
# HF_HUB_OFFLINE
# 1 == Disable internet access.
# Internet access will only be used when downloading models with the
# model manager or setup wizard.
####################################################################
HF_HUB_OFFLINE = "1"

####################################################################
# HF_CACHE_DIR is the directory where Hugging Face models are stored.
# By default FacehuggerShield keeps this under a package-scoped cache
# root instead of using the shared Hugging Face default directory.
####################################################################
HF_CACHE_DIR = os.path.join(
    os.path.expanduser("~"), ".cache", "facehuggershield", "huggingface"
)

####################################################################
# HF_HOME is the directory where huggingface models are stored.
# We set this to HF_CACHE_DIR
####################################################################
HF_HOME = HF_CACHE_DIR

####################################################################
# HF_ASSETS_CACHE is the directory where huggingface assets are
# stored. Default value is "$HF_HOME/assets"
# Here we hard code it to the same directory as HF_HOME
####################################################################
HF_ASSETS_CACHE = HF_CACHE_DIR

####################################################################
# HF_ENDPOINT is the huggingface endpoint.
# Default value is "https://huggingface.co" but we blank it out to
# force offline behavior unless the host application explicitly opts
# into downloads.
####################################################################
HF_ENDPOINT = ""

####################################################################
# HF_INFERENCE_ENDPOINT is the huggingface inference endpoint.
# Default value is "https://api-inference.huggingface.com" but we
# have changed it to ""
# in order to force prevention of internet access. This ensures
# that no inadvertent data
# transmissions occur, maintaining privacy and security by avoiding
# external API calls.
####################################################################
HF_INFERENCE_ENDPOINT = ""

####################################################################
# HF_HUB_DISABLE_PROGRESS_BARS is used to disable progress bars for
# huggingface models.
# Default value is "0", which keeps download progress visible when a
# host application explicitly enables network access.
####################################################################
HF_HUB_DISABLE_PROGRESS_BARS = "0"

####################################################################
# HF_HUB_DISABLE_SYMLINKS_WARNING is used to suppress warnings
# related to symlink creation.
# Default value is "0". Keeping this setting as default aids in
# debugging file system issues,
# especially on Windows where symlink creation might require
# elevated permissions.
####################################################################
HF_HUB_DISABLE_SYMLINKS_WARNING = "0"

####################################################################
# HF_HUB_DISABLE_EXPERIMENTAL_WARNING is used to disable warnings
# for experimental features.
# Default value is "0". By not changing this, users are kept
# informed about the potential
# instability of experimental features, enhancing awareness and
# preventive caution.
####################################################################
HF_HUB_DISABLE_EXPERIMENTAL_WARNING = "0"

####################################################################
# HF_TOKEN is used for authentication. By setting this to an empty
# string "",
# we ensure that no credentials are stored or used inadvertently,
# enhancing security by preventing unauthorized access to private
# repositories or features.
####################################################################
HF_TOKEN = ""

####################################################################
# HF_HUB_VERBOSITY is set to "error" to minimize logging output.
# This setting reduces the
# risk of sensitive information being logged accidentally, thereby
# enhancing privacy and security.
####################################################################
HF_HUB_VERBOSITY = "error"

####################################################################
# HF_HUB_LOCAL_DIR_AUTO_SYMLINK_THRESHOLD is set to "0" to disable
# the use of symlinks.
# This can prevent symlink attacks and avoids complications on
# systems where symlinks
# are not well-supported, enhancing file system security.
####################################################################
HF_HUB_LOCAL_DIR_AUTO_SYMLINK_THRESHOLD = "0"

####################################################################
# HF_HUB_DOWNLOAD_TIMEOUT and HF_HUB_ETAG_TIMEOUT are set to "30"
# seconds to balance between
# usability and security. Increased timeouts reduce the risk of
# interruptions during data
# transfers which could leave files in an insecure state.
####################################################################
HF_HUB_DOWNLOAD_TIMEOUT = "30"
HF_HUB_ETAG_TIMEOUT = "30"

####################################################################
# HF_HUB_DISABLE_IMPLICIT_TOKEN is set to "1" to avoid automatically
# sending authentication tokens
# with each request. This prevents potential leaks of credentials
# and ensures that tokens are
# only sent when explicitly required by the user, thereby
# enhancing security.
####################################################################
HF_HUB_DISABLE_IMPLICIT_TOKEN = "1"

####################################################################
# HF_DATASETS_OFFLINE and TRANSFORMERS_OFFLINE are set to "1" to
# ensure that all operations
# with datasets and transformers are conducted offline.
# This eliminates any reliance on
# external networks, which maximizes security by preventing
# exposure to network-based threats.
####################################################################
HF_DATASETS_OFFLINE = "1"
TRANSFORMERS_OFFLINE = "1"

####################################################################
# DIFFUSERS_VERBOSITY is set to "error" to keep the logging level
# minimal for the diffusers
# library, consistent with the setting for other Hugging Face tools.
# This consistency helps in
# maintaining a secure and quiet operational environment.
####################################################################
DIFFUSERS_VERBOSITY = "error"

####################################################################
# Prevents remote code from being downloaded from huggingface and
# executed on the host machine.
# Huge security risk if set to True. Huggingface Transformers
# library should not have this capability - no library should.
# Note that this is not an environment variable and is passed into
# functions which download models and code.
# For example, the stabilityai zeyphr library has a flag to
# trust remote code.
# Allegedly, this is safe, but I do not trust it.
# Never set this to True unless you are explicitly researching or
# auditing remote-code execution behavior.
####################################################################
TRUST_REMOTE_CODE = "False"

####################################################################
# DEFAULT_HF_HUB_OFFLINE is set to "0" to allow for online access
# do not change this value, we will switch to it when
# we want to allow online access (when using download features)
####################################################################
DEFAULT_HF_HUB_OFFLINE = "0"

####################################################################
# DEFAULT_HF_DATASETS_OFFLINE = "0" to allow for online access
# do not change this value, we will switch to it when
# we want to allow online access (when using download features)
####################################################################
DEFAULT_HF_DATASETS_OFFLINE = "0"

###################################################################
# TRANSFORMERS_OFFLINE is set to "0" to allow for online access
# do not change this value, we will switch to it when
# we want to allow online access (when using download features)
####################################################################
DEFAULT_TRANSFORMERS_OFFLINE = "0"

####################################################################
# DEFAULT_HF_ENDPOINT is the default huggingface endpoint.
# Default value is "https://huggingface.co"
# This is used when the HF_HUB_OFFLINE is set to "0"
# and online access is allowed.
# You may change this value if you want to use a different endpoint.
####################################################################
DEFAULT_HF_ENDPOINT = "https://huggingface.co"

####################################################################
# DEFAULT_HF_INFERENCE_ENDPOINT is the default huggingface inference
# endpoint.
# Default value is "https://api-inference.huggingface.com"
# This is used when the HF_HUB_OFFLINE is set to "0"
# and online access is allowed.
# You may change this value if you want to use a different endpoint.
# This value is reserved for hosts that opt into online inference.
####################################################################
DEFAULT_HF_INFERENCE_ENDPOINT = "https://api-inference.huggingface.com"
