import unittest,xml.etree.ElementTree as ET,json,zipfile,sys,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))

class SourceContracts(unittest.TestCase):
    def test_manifest_never_syncs_vendor_blobs(self):
        root=ET.parse(ROOT/'manifests/a51.xml').getroot()
        paths=[]
        for p in root.findall('project'):
            path=p.attrib['path'];paths.append(path)
            self.assertFalse(path.startswith('vendor/'))
            self.assertRegex(p.attrib['revision'],r'^[0-9a-f]{40}$')
        self.assertEqual(len(paths),len(set(paths)))
        self.assertIn('device/samsung/a51',paths)
        self.assertIn('kernel/samsung/universal9611',paths)
    def test_unprivileged_layer_has_no_network_or_screen_access(self):
        root=ET.parse(ROOT/'layer/src/main/AndroidManifest.xml').getroot()
        ns='{http://schemas.android.com/apk/res/android}'
        permissions={e.attrib[ns+'name'] for e in root.findall('uses-permission')}
        for forbidden in ['INTERNET','READ_SMS','READ_CALL_LOG','QUERY_ALL_PACKAGES','WRITE_SECURE_SETTINGS']:
            self.assertNotIn('android.permission.'+forbidden,permissions)
        for service in root.findall('application/service'):
            self.assertEqual(service.attrib[ns+'exported'],'false')
            self.assertNotIn('Accessibility',service.attrib[ns+'name'])
    def test_module_cannot_write_sysfs_or_flash_partitions(self):
        content='\n'.join(p.read_text() for p in (ROOT/'module').glob('*.sh'))
        for forbidden in ['dd if=','fastboot','/dev/block/','chmod 777','setenforce','scaling_min_freq','thermal_zone','zram']:
            self.assertNotIn(forbidden,content)
        # No boot-time autorun script and no mounted framework replacement.
        self.assertFalse((ROOT/'module/service.sh').exists())
        self.assertFalse((ROOT/'module/post-fs-data.sh').exists())
        self.assertFalse((ROOT/'module/system').exists())
    def test_all_android_xml_is_parseable(self):
        for folder in ['android','layer/src/main']:
            for p in (ROOT/folder).rglob('*.xml'):
                ET.parse(p)
    def test_language_coverage_and_conflict_cases(self):
        lines=(ROOT/'layer/src/main/assets/commands.tsv').read_text(encoding='utf-8').splitlines()
        locales={l.split('\t')[0] for l in lines if l and not l.startswith('#')}
        self.assertEqual(locales,{'en','ar','ary','ary-Latn','fr','es','pt','ru','tr','hi','zh'})
        cases=(ROOT/'assistant/benchmark.tsv').read_text(encoding='utf-8')
        self.assertIn('Open Wi-Fi and Bluetooth\tUNKNOWN',cases)
        self.assertIn('3afak coupe le wifi\tWIFI',cases)
    def test_site_contains_no_external_script_or_tracking(self):
        for p in (ROOT/'site').glob('*.html'):
            self.assertNotRegex(p.read_text(encoding='utf-8'),r'<script[^>]+src=["\']https?://')
        self.assertNotIn('fetch(', (ROOT/'site/preview.js').read_text(encoding='utf-8'))

if __name__=='__main__':unittest.main()
