def serialize_doc(doc):
    if not doc:
        return {}
    doc["_id"] = serialize_id(doc["_id"])
    return doc


def serialize_id(oid):
    if not oid:
        return ""
    return str(oid)
