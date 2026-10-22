# pdf.SMT

A rebranded source edition of [PdfCraft](https://github.com/storytold/pdfcraft).

Upstream revision: `ec0a965074f376a5bf610435948e4e5184bf3299` (0.9.0 source tree).

## Status

Source changes prepared; **not compiled or runtime-tested**. This package is not an installer.
The upstream app is alpha. Its existing features, UI layout and limitations are inherited.
Rust/Cargo were unavailable in the preparation environment.

For the Windows x64 installer and portable build, see [WINDOWS-X64.md](WINDOWS-X64.md).

## Build the desktop application

Install Rust **1.95 or later** and platform dependencies described in `docs/development.md`.
Run from this folder:

```sh
cargo xtask models
cargo run --release -p pdfcraft
```

The window and menus use **pdf.SMT**. Internal Cargo crate names and executable names remain
`pdfcraft` for build compatibility. The desktop output is `target/release/pdfcraft`
(or `pdfcraft.exe` on Windows); you may rename a portable executable to `pdf.SMT.exe`.

For Japanese and other supported CJK fonts, clone the optional upstream `craft-fonts`
repository beside this folder and set `CRAFT_FONTS_DIR` to its path before building.

## Web and packaging

See `packaging/web/README.md` for the WebAssembly build and hosting instructions.
Platform packaging scripts live in `packaging/`. They require platform tools and external
build inputs. Original signing credentials are not included. The original release workflow
is upstream infrastructure, not a configured pdf.SMT release service.

## Changes

- Product labels, window titles, translation catalogues and packaging display names use pdf.SMT.
- Separate application ID (`app.smt.pdf`), settings folders and Windows MSI upgrade identity.
- Original legacy settings migration disabled so this fork does not move another app's data.
- ArtCraft marks and old screenshots removed; existing text font renders the pdf.SMT wordmark.
- Community promotion replaced by an explicitly labelled upstream-source link.
- Update checks do not offer original PdfCraft binaries as pdf.SMT updates.
- PDF engine algorithms and editing functionality retained.

## Validation still required

Run `cargo fmt --check`, scoped Clippy and tests, `cargo xtask layers`,
`cargo xtask assets --write`, `cargo xtask assets`, and a WASM check.
Then test open/render/edit/save on sample PDFs, launch the UI, and validate installers
on each target OS. No feature-parity or release-readiness claim is made by this source package.

## Licence and attribution

Based on PdfCraft by the ArtCraft team and contributors. This is an independent modified edition.
Original copyright and licence notices are retained in `LICENSE-MIT`, `LICENSE-APACHE`,
`NOTICE` and the attribution manifest. Internal source names credit upstream.
Changes in this source edition: 2026-10-20, pdf.SMT branding and fork identity.
