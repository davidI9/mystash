from src.RecordLifecycle.infrastructure.Controllers.AlbumRecords.CreateAlbumRecord import create_album_record_endpoint


def test_create_album_record_endpoint_returns_router():
    router = create_album_record_endpoint(None)

    assert router is not None
    assert any(getattr(route, "path", None) == "/create_record" for route in router.routes)
