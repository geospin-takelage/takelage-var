import re
import takeltest

testinfra_hosts = takeltest.hosts()


def test_takeltest_system_role_fortune_configure(host, testvars):
    if 'fortune-anarchism' in testvars['anarchism_packages']:
        with host.sudo():
            file = host.file('/root/.bashrc')
            expected = '''
echo
/usr/games/fortune -s anarchism
echo
'''
            assert re.search(expected, file.content_string) is not None
