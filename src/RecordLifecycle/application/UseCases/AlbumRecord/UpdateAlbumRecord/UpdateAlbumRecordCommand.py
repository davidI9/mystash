from dataclasses import dataclass
from src.RecordLifecycle.domain.ValueObjects.AuthorId import AuthorId
from src.RecordLifecycle.domain.ValueObjects.RecordId import RecordId
from src.RecordLifecycle.domain.ValueObjects.RecordTitle import RecordTitle
from src.RecordLifecycle.domain.ValueObjects.CreationDate import CreationDate
from src.RecordLifecycle.domain.ValueObjects.ArtistName import ArtistName
from src.RecordLifecycle.domain.ValueObjects.GenreName import GenreName

@dataclass(frozen=True)
class UpdateAlbumRecordCommand:
    author: AuthorId 
    album_title: RecordTitle
    date: CreationDate
    id: RecordId
    artist: ArtistName
    main_genre: GenreName