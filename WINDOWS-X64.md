# pdf.SMT — Windows x64 build

Status: build configuration prepared, not executed. No executable or MSI is included yet.

## GitHub build

1. Fork https://github.com/storytold/pdfcraft/fork to your account as `pdf-SMT`.
2. Apply this source edition to that fork on branch `build/pdf-smt-windows-x64`.
3. Enable Actions for the fork if GitHub asks. The branch push starts the build; alternatively
   select **Actions → pdf.SMT Windows x64 → Run workflow**, selecting that branch.
4. After the job passes, download the `pdf.SMT-Windows-x64` artifact. It contains the MSI,
   portable ZIP, and checksums. An artifact ZIP is a download wrapper, not the installer itself.

Expected outputs at the current source version:
- `pdf.SMT-0.9.0-windows-x64.msi`
- `pdf.SMT-0.9.0-windows-x64-portable.zip` (launch `pdf.SMT.exe` after extracting)
- `SHA256SUMS.txt`

The build uses Windows Server 2022, MSVC x64, Rust 1.95.0, WiX 5.0.2, pinned optional CJK fonts,
and verified OCR models. It runs asset validation, desktop/UI tests, PE architecture checks,
MSI database checks and a CLI launch check before uploading files. Interactive app launch and
PDF editing still need testing on a Windows desktop after compilation.

No signing certificate is configured. The first build will be unsigned and Windows may show
an unknown-publisher warning. Upstream's signing identities are not used.

## Local Windows build

Install Git, Rust 1.95+, Visual Studio Build Tools with Desktop development with C++ and the
Windows SDK, .NET SDK and WiX 5.0.2. In PowerShell from this source directory:

```powershell
dotnet tool install --global wix --version 5.0.2
rustup target add x86_64-pc-windows-msvc
git clone https://github.com/storytold/craft-fonts ../craft-fonts
git -C ../craft-fonts checkout 3d9ab3a132ed0eff457e424226a435a901da30d3
$env:CRAFT_FONTS_DIR = (Resolve-Path ../craft-fonts).Path
./packaging/windows/package.ps1 -Arch x64
```

Outputs go to `dist/release`. Preserve all licences and notices when distributing.
Original upstream workflows are retained under `.github/upstream-workflows` as reference;
only the pdf.SMT x64 workflow is active.
