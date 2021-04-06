def serialize_doc(doc):
    if not doc:
        return {}
    doc["_id"] = serialize_id(doc["_id"])
    return doc


def serialize_docs(docs_cursor):
    if not docs_cursor:
        return []
    docs = []
    for doc in docs_cursor:
        print(doc)
        docs.append(doc)
    return list(map(serialize_doc, docs))


def serialize_id(oid):
    if not oid:
        return ""
    return str(oid)


def serialize_ids(oids):
    if not oids:
        return ""
    return list(map(serialize_id, oids))
