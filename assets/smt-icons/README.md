# pdf.SMT icons

Approved by SMT on 2026-10-22. Generated custom SMT ribbon lettering and folded-document artwork, under MIT OR Apache-2.0. Red/white app artwork and inverted white/red PDF document artwork are separate resources. The owner explicitly requested the red document style; no Adobe logo is embedded.

`app.png` and `document.png` are the 1024 px transparent PNG masters, converted from the approved generated artwork. `packaging/smt-icons.py` converts them with Pillow to multi-resolution ICO (16–256 px), ICNS (up to 1024 px), and the 256 px runtime PNG. Existing upstream artwork remains attributed separately.

Windows embeds app.ico as resource 1 and document.ico as resource 2. The MSI uses the app icon for shortcuts and resource 2 for the PDF file association when the user selects pdf.SMT as default. macOS bundles both ICNS files and declares the document icon separately in Info.plist. Finder/Explorer may show document thumbnails instead of file icons when previews are enabled.
