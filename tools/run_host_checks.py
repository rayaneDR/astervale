"""Run real Java engine tests with a selected JDK, preserving Unicode output."""
from pathlib import Path
import os,shutil,subprocess
ROOT=Path(__file__).resolve().parents[1]
configured=Path(os.environ.get('JAVA_HOME',''))/'bin'
local=next((ROOT/'tools/bin').glob('jdk-*/bin'),None)
binpath=configured if (configured/'javac.exe').exists() or (configured/'javac').exists() else local
def tool(name):
    if binpath:return str(binpath/(name+('.exe' if os.name=='nt' else '')))
    return shutil.which(name) or name
classes=ROOT/'output/classes';classes.mkdir(parents=True,exist_ok=True)
def run(args):subprocess.run(args,cwd=ROOT,check=True)
run([tool('javac'),'--release','17','-d',str(classes),'layer/src/main/java/org/astervale/panel/IntentEngine.java','assistant/Benchmark.java','assistant/SafetyTests.java'])
run([tool('java'),'-cp',str(classes),'SafetyTests','layer/src/main/assets/commands.tsv'])
run([tool('java'),'-cp',str(classes),'Benchmark','layer/src/main/assets/commands.tsv','assistant/benchmark.tsv','docs/LANGUAGE_BENCHMARK.md'])
run([shutil.which('python') or 'python','-m','unittest','discover','-s','tests','-v'])
