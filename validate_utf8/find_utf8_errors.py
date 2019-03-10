from collections import namedtuple

Utf8Error = namedtuple("Utf8Error", ("reason", "extract"))


def find_utf8_errors(bytestring, context=30):
    byte_start_index = 0
    errors = []
    while True:
        to_consider = bytestring[byte_start_index:]
        try:
            to_consider.decode("utf-8")
        except UnicodeDecodeError as e:
            start_index = max(0, e.start - context)
            start_highlight_index = context
            end_index = e.end + context
            extract = to_consider[start_index:end_index]
            formatted_extract = (
                "  "
                + extract.decode("latin-1")
                + "\n"
                + "  "
                + (" " * start_highlight_index + "^")
            )
            errors.append(Utf8Error(e.reason, formatted_extract))
            byte_start_index += e.end
        else:
            break
    return errors
