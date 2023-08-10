import pytest

from ktlkuda.sync import SyncMainDataDictionary
from ktlkuda.sync import SyncTorrentPeersDictionary


@pytest.mark.parametrize("maindata_func", ["sync_maindata", "sync.maindata"])
@pytest.mark.parametrize("rid", [None, 0, 1, 100000])
def test_sync_maindata(client, maindata_func, rid):
    assert isinstance(client.func(maindata_func)(rid=rid), SyncMainDataDictionary)


@pytest.mark.parametrize("rid", (None, 0, 1, 100000))
def test_sync_maindata_delta(client, rid):
    assert isinstance(client.sync.maindata(rid=rid), SyncMainDataDictionary)
    assert isinstance(client.sync.maindata.delta(), SyncMainDataDictionary)
    assert isinstance(client.sync.maindata.delta(), SyncMainDataDictionary)


def test_sync_maindata_reset(client):
    client.sync.maindata.delta()
    assert client.sync.maindata._rid != 0
    client.sync.maindata.reset_rid()
    assert client.sync.maindata._rid == 0


@pytest.mark.parametrize("rid", (None, 0, 1, 100000))
def test_sync_torrent_peers(client, rid, orig_torrent):
    assert isinstance(
        client.sync_torrent_peers(rid=rid, torrent_hash=orig_torrent.hash),
        SyncTorrentPeersDictionary,
    )
    assert isinstance(
        client.sync.torrent_peers(rid=rid, torrent_hash=orig_torrent.hash),
        SyncTorrentPeersDictionary,
    )
    assert isinstance(
        client.sync.torrent_peers.delta(torrent_hash=orig_torrent.hash),
        SyncTorrentPeersDictionary,
    )

    client.sync.torrent_peers.reset_rid()
    assert client.sync.torrent_peers._rid == 0
