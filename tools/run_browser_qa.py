from pathlib import Path
import subprocess,shutil
root=Path(__file__).resolve().parents[1]
code=(root/'tools/browser-qa.js').read_text(encoding='utf-8')
result=subprocess.run([shutil.which('node'),str(root/'node_modules/@playwright/cli/playwright-cli.js'),'run-code',code],cwd=root,capture_output=True)
(root/'output/playwright/qa-result.txt').write_bytes(result.stdout+result.stderr)
print((result.stdout+result.stderr).decode('utf-8',errors='replace')[-6500:])
raise SystemExit(result.returncode)
