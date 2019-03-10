from validate_utf8 import find_utf8_errors, Utf8Error


def test_find_utf8_errors():
    bad = b"28 COURTHOUSE-GROUND FLOOR\xe1,,,REP,Straight Ticket,"
    errors = list(find_utf8_errors(bad))
    assert [
        Utf8Error(
            reason="invalid continuation byte",
            extract=(
                "  28 COURTHOUSE-GROUND FLOORá,,,REP,Straight Ticket,\n"
                "                                ^"
            )
        )
    ] == errors
