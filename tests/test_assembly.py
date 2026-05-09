from pbg_chromosome_rep1.document import build_document


def test_build_document_returns_dict():
    doc = build_document()
    assert isinstance(doc, dict)
