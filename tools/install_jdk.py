"""Install official Temurin archive in ignored tools/bin after SHA256 verification."""
import hashlib,json,pathlib,urllib.request,zipfile
from research import ROOT,OUT
package=json.loads((OUT/'jdk.json').read_bytes())[0]['binary']['package']
url=package['link']
if not url.startswith('https://github.com/adoptium/temurin21-binaries/releases/download/'):raise SystemExit('Unexpected JDK source')
dest=ROOT/'tools/bin';dest.mkdir(parents=True,exist_ok=True)
archive=dest/'jdk21.zip'
urllib.request.urlretrieve(url,archive)
if hashlib.file_digest(archive.open('rb'),'sha256').hexdigest()!=package['checksum']:raise SystemExit('Checksum mismatch')
with zipfile.ZipFile(archive) as z:
    for item in z.infolist():
        target=(dest/item.filename).resolve()
        if not target.is_relative_to(dest.resolve()):raise SystemExit('Unsafe archive entry')
    z.extractall(dest)
print('Verified JDK:',next(dest.glob('jdk-*/bin/java.exe')))
