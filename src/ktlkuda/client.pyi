from typing import Any
from typing import Mapping
from typing import Optional
from typing import Text

from ktlkuda._types import KwargsT
from ktlkuda.app import AppAPIMixIn
from ktlkuda.auth import AuthAPIMixIn
from ktlkuda.log import LogAPIMixIn
from ktlkuda.request import Request
from ktlkuda.rss import RSSAPIMixIn
from ktlkuda.search import SearchAPIMixIn
from ktlkuda.sync import SyncAPIMixIn
from ktlkuda.torrents import TorrentsAPIMixIn
from ktlkuda.transfer import TransferAPIMixIn

class Client(
    LogAPIMixIn,
    SyncAPIMixIn,
    TransferAPIMixIn,
    TorrentsAPIMixIn,
    RSSAPIMixIn,
    SearchAPIMixIn,
    AuthAPIMixIn,
    AppAPIMixIn,
    Request,
):
    def __init__(
        self,
        host: Text = "",
        port: Optional[Text | int] = None,
        username: Optional[Text] = None,
        password: Optional[Text] = None,
        EXTRA_HEADERS: Optional[Mapping[Text, Text]] = None,
        REQUESTS_ARGS: Optional[Mapping[Text, Any]] = None,
        VERIFY_WEBUI_CERTIFICATE: Optional[bool] = True,
        FORCE_SCHEME_FROM_HOST: Optional[bool] = False,
        RAISE_NOTIMPLEMENTEDERROR_FOR_UNIMPLEMENTED_API_ENDPOINTS: Optional[
            bool
        ] = False,
        RAISE_ERROR_FOR_UNSUPPORTED_QBITTORRENT_VERSIONS: Optional[bool] = False,
        VERBOSE_RESPONSE_LOGGING: Optional[bool] = False,
        SIMPLE_RESPONSES: Optional[bool] = False,
        DISABLE_LOGGING_DEBUG_OUTPUT: Optional[bool] = False,
        **kwargs: KwargsT
    ) -> None: ...
