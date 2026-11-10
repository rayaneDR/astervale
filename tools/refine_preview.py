from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
p=ROOT/'site/styles.css';s=p.read_text(encoding='utf-8')
s=s.replace('.phone{--scale:1;', '.phone{container-type:inline-size;--scale:1;')
s=s.replace('font-size:calc(72px * var(--scale))','font-size:min(calc(72px * var(--scale)),24cqw)')
s=s.replace('font-size:calc(80px * var(--scale))','font-size:min(calc(80px * var(--scale)),25cqw)')
p.write_text(s,encoding='utf-8')
print('Bound large clock typography to its phone container; body text scaling preserved.')
