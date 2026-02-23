from __future__ import annotations

from pathlib import Path
from zipfile import ZipFile

from pypdf import PdfReader


def pdf_report(path: Path) -> dict:
    reader = PdfReader(str(path))
    meta = reader.metadata or {}

    annots = 0
    annot_types: dict[str, int] = {}
    embedded_files = 0
    xmp_present = False

    try:
        root = reader.trailer["/Root"]
        xmp_present = "/Metadata" in root
    except Exception:
        pass

    for page in reader.pages:
        try:
            a = page.get("/Annots")
            if not a:
                continue
            annots += len(a)
            for ref in a:
                try:
                    obj = ref.get_object()
                    subtype = obj.get("/Subtype")
                    key = str(subtype) if subtype is not None else "(none)"
                    annot_types[key] = annot_types.get(key, 0) + 1
                except Exception:
                    annot_types["(unreadable)"] = annot_types.get("(unreadable)", 0) + 1
        except Exception:
            annot_types["(page_error)"] = annot_types.get("(page_error)", 0) + 1

    try:
        root = reader.trailer["/Root"]
        names = root.get("/Names")
        if names and "/EmbeddedFiles" in names:
            ef = names["/EmbeddedFiles"]
            if "/Names" in ef:
                embedded_files = max(0, len(ef["/Names"]) // 2)
    except Exception:
        pass

    def mget(k: str) -> str:
        v = meta.get(k)
        return "" if v is None else str(v)

    return {
        "file": path.name,
        "pages": len(reader.pages),
        "annotations": annots,
        "annotation_types": dict(sorted(annot_types.items(), key=lambda kv: (-kv[1], kv[0]))),
        "embedded_files": embedded_files,
        "title": mget("/Title"),
        "author": mget("/Author"),
        "creator": mget("/Creator"),
        "producer": mget("/Producer"),
        "xmp_metadata_present": xmp_present,
    }


def zip_report(path: Path) -> dict:
    with ZipFile(path, "r") as z:
        entries = [i.filename for i in z.infolist() if not i.is_dir()]
    return {"file": path.name, "count": len(entries), "entries": entries}


def main() -> int:
    base = Path(__file__).resolve().parent
    pdfs = [
        base / "protective-computing-acmart.pdf",
        base / "cover-letter.pdf",
    ]
    zips = [base / "protective-computing-acmart-source.zip"]

    ok = True

    for p in pdfs:
        if not p.exists():
            print(f"MISSING PDF: {p}")
            ok = False
            continue
        r = pdf_report(p)
        print(f"PDF: {r['file']}")
        print(f"  pages: {r['pages']}")
        print(f"  annotations: {r['annotations']}")
        if r["annotations"]:
            print("  annotation types:")
            for t, c in r["annotation_types"].items():
                print(f"    - {t}: {c}")
        print(f"  embedded files: {r['embedded_files']}")
        print(f"  /Title: {r['title']}")
        print(f"  /Author: {r['author']}")
        print(f"  /Creator: {r['creator']}")
        print(f"  /Producer: {r['producer']}")
        print(f"  XMP metadata present: {r['xmp_metadata_present']}")

    for z in zips:
        if not z.exists():
            print(f"MISSING ZIP: {z}")
            ok = False
            continue
        r = zip_report(z)
        print(f"ZIP: {r['file']}")
        print(f"  entries: {r['count']}")
        for e in r["entries"]:
            print(f"   - {e}")

    return 0 if ok else 2


if __name__ == "__main__":
    raise SystemExit(main())
