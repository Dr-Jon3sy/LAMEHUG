from pathlib import Path

def gen_pdf(loc):
    if loc.exists():
        return True
    try:
        text = "this is a totally legit pdf"
        # magic pdf bullshit
        content_bytes = f"BT /F1 24 Tf 72 720 Td ({text}) Tj ET".encode("latin-1")
        content_obj = b"<< /Length " + str(len(content_bytes)).encode("ascii") + b" >>\nstream\n" + content_bytes + b"\nendstream"
        # more magic
        objs = [
            b"<< /Type /Catalog /Pages 2 0 R >>",
            b"<< /Type /Pages /Count 1 /Kids [3 0 R] >>",
            b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] "
            b"/Resources << /Font << /F1 4 0 R >> >> "
            b"/Contents 5 0 R >>",
            b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>",
            content_obj,
        ]
        header = b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n"
        parts = [header]
        offsets = [0]  
        cursor = len(header)
        for i, body in enumerate(objs, start=1):
            obj_bytes = f"{i} 0 obj\n".encode("ascii") + body + b"\nendobj\n"
            offsets.append(cursor)
            parts.append(obj_bytes)
            cursor += len(obj_bytes)
        #
        # xref stuff
        #
        xref_offset = cursor
        xref = [b"xref\n", f"0 {len(offsets)}\n".encode("ascii")]
        xref.append(b"0000000000 65535 f \n")
        for off in offsets[1:]:
            xref.append(f"{off:010d} 00000 n \n".encode("ascii"))
        parts.extend(xref)
        trailer = (
            b"trailer\n<< /Size " + str(len(offsets)).encode("ascii") +
            b" /Root 1 0 R >>\nstartxref\n" +
            str(xref_offset).encode("ascii") + b"\n%%EOF"
        )
        parts.append(trailer)

        loc.write_bytes(b"".join(parts))
    except Exception as e:
        print(f"Error: {e}")
        return None
    return True