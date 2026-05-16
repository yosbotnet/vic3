from fetch_transcripts import slugify_title


def test_slugify_strips_in_victoria_3_suffix():
    assert slugify_title("Shipbuilding Tutorial in Victoria 3") == "shipbuilding"


def test_slugify_strips_tutorial_word():
    assert slugify_title("Deficit Spending Tutorial in Victoria 3") == "deficit-spending"


def test_slugify_strips_version_tags():
    assert (
        slugify_title("How to Pass Laws in Update 1.12 - Victoria 3")
        == "how-to-pass-laws"
    )
    assert (
        slugify_title("Subjecthood and Citizenship Laws Tutorial in Victoria 3's 1.10 Update")
        == "subjecthood-and-citizenship-laws"
    )


def test_slugify_collapses_non_alnum():
    assert slugify_title("World Market & Trade Center!") == "world-market-trade-center"


def test_slugify_lowercases():
    assert slugify_title("FOO Bar") == "foo-bar"


def test_slugify_handles_apostrophes():
    assert slugify_title("Victoria 3's Power Blocs") == "power-blocs"


from fetch_transcripts import VideoMeta, format_transcript_markdown


def _meta() -> VideoMeta:
    return VideoMeta(
        title="Shipbuilding Tutorial in Victoria 3",
        video_id="ct-PUjt6M8c",
        url="https://www.youtube.com/watch?v=ct-PUjt6M8c",
        duration_seconds=1554,
        playlist="tutorials",
        playlist_index=1,
    )


def test_format_includes_frontmatter():
    transcript = [
        {"text": "Hello world", "start": 0.0},
        {"text": "and welcome", "start": 5.2},
    ]
    out = format_transcript_markdown(_meta(), transcript, source="youtube-transcript-api", fetched_at="2026-05-16")
    assert out.startswith("---\n")
    assert 'title: "Shipbuilding Tutorial in Victoria 3"' in out
    assert "video_id: ct-PUjt6M8c" in out
    assert "playlist: tutorials" in out
    assert "playlist_index: 1" in out
    assert "caption_source: youtube-transcript-api" in out
    assert "fetched_at: 2026-05-16" in out


def test_format_emits_timestamp_marker_at_start():
    transcript = [{"text": "Hello world", "start": 0.0}]
    out = format_transcript_markdown(_meta(), transcript, source="youtube-transcript-api", fetched_at="2026-05-16")
    assert "[00:00] Hello world" in out


def test_format_emits_timestamp_every_30_seconds():
    transcript = [
        {"text": "first", "start": 0.0},
        {"text": "still in first chunk", "start": 15.0},
        {"text": "second chunk", "start": 32.0},
        {"text": "still second", "start": 45.0},
        {"text": "third chunk", "start": 65.0},
    ]
    out = format_transcript_markdown(_meta(), transcript, source="youtube-transcript-api", fetched_at="2026-05-16")
    assert "[00:00]" in out
    assert "[00:32]" in out
    assert "[01:05]" in out
    assert "[00:15]" not in out
    assert "[00:45]" not in out


def test_format_quotes_title_with_special_chars():
    meta = VideoMeta(
        title='Victoria 3\'s "Best" Tutorial',
        video_id="x",
        url="https://example",
        duration_seconds=10,
        playlist="tutorials",
        playlist_index=1,
    )
    out = format_transcript_markdown(meta, [{"text": "hi", "start": 0.0}], source="youtube-transcript-api", fetched_at="2026-05-16")
    import yaml
    front = out.split("---\n", 2)[1]
    parsed = yaml.safe_load(front)
    assert parsed["title"] == 'Victoria 3\'s "Best" Tutorial'


from fetch_transcripts import output_filename


def test_output_filename_slug_naming():
    meta = VideoMeta(
        title="Shipbuilding Tutorial in Victoria 3",
        video_id="x", url="u", duration_seconds=0,
        playlist="tutorials", playlist_index=1,
    )
    assert output_filename(meta, naming="slug") == "01-shipbuilding.md"


def test_output_filename_pads_to_two_digits():
    meta = VideoMeta(
        title="Foo", video_id="x", url="u", duration_seconds=0,
        playlist="tutorials", playlist_index=7,
    )
    assert output_filename(meta, naming="slug") == "07-foo.md"


def test_output_filename_episode_naming():
    meta = VideoMeta(
        title="Victoria 3: Japan Becomes a Superpower! | The Great Wave - ep1",
        video_id="x", url="u", duration_seconds=0,
        playlist="great-wave-japan", playlist_index=1,
    )
    assert output_filename(meta, naming="episode") == "ep01.md"


def test_output_filename_episode_naming_two_digit():
    meta = VideoMeta(
        title="...ep17", video_id="x", url="u", duration_seconds=0,
        playlist="great-wave-japan", playlist_index=17,
    )
    assert output_filename(meta, naming="episode") == "ep17.md"
