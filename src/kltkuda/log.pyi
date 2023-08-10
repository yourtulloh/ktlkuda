from typing import Optional
from typing import Text

from ktlkuda._types import KwargsT
from ktlkuda._types import ListInputT
from ktlkuda.app import AppAPIMixIn
from ktlkuda.definitions import ClientCache
from ktlkuda.definitions import List
from ktlkuda.definitions import ListEntry

class LogPeer(ListEntry): ...

class LogPeersList(List[LogPeer]):
    def __init__(
        self,
        list_entries: ListInputT,
        client: Optional[LogAPIMixIn] = None,
    ) -> None: ...

class LogEntry(ListEntry): ...

class LogMainList(List[LogEntry]):
    def __init__(
        self,
        list_entries: ListInputT,
        client: Optional[LogAPIMixIn] = None,
    ) -> None: ...

class Log(ClientCache):
    main: _Main
    def __init__(self, client: LogAPIMixIn) -> None: ...
    def peers(
        self,
        last_known_id: Optional[Text | int] = None,
        **kwargs: KwargsT,
    ) -> LogPeersList: ...

    class _Main(ClientCache):
        def _api_call(
            self,
            normal: Optional[bool] = None,
            info: Optional[bool] = None,
            warning: Optional[bool] = None,
            critical: Optional[bool] = None,
            last_known_id: Optional[bool] = None,
            **kwargs: KwargsT
        ) -> LogMainList: ...
        def __call__(
            self,
            normal: Optional[bool] = True,
            info: Optional[bool] = True,
            warning: Optional[bool] = True,
            critical: Optional[bool] = True,
            last_known_id: Optional[bool] = None,
            **kwargs: KwargsT
        ) -> LogMainList: ...
        def info(
            self,
            last_known_id: Optional[Text | int] = None,
            **kwargs: KwargsT,
        ) -> LogMainList: ...
        def normal(
            self,
            last_known_id: Optional[Text | int] = None,
            **kwargs: KwargsT,
        ) -> LogMainList: ...
        def warning(
            self,
            last_known_id: Optional[Text | int] = None,
            **kwargs: KwargsT,
        ) -> LogMainList: ...
        def critical(
            self,
            last_known_id: Optional[Text | int] = None,
            **kwargs: KwargsT,
        ) -> LogMainList: ...

class LogAPIMixIn(AppAPIMixIn):
    @property
    def log(self) -> Log: ...
    def log_main(
        self,
        normal: Optional[bool] = None,
        info: Optional[bool] = None,
        warning: Optional[bool] = None,
        critical: Optional[bool] = None,
        last_known_id: Optional[bool] = None,
        **kwargs: KwargsT
    ) -> LogMainList: ...
    def log_peers(
        self,
        last_known_id: Optional[Text | int] = None,
        **kwargs: KwargsT,
    ) -> LogPeersList: ...
