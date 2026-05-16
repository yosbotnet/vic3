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
