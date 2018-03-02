#!/usr/bin/python3

import requests
import click
import xml.etree.ElementTree as ET
from colorama import init, Fore, Back, Style

init(autoreset=True)

google_maven_url = 'https://dl.google.com/dl/android/maven2/{}/maven-metadata.xml'

support_libraries = [
    'com.android.support:support-compat',
    'com.android.support:support-core-utils',
    'com.android.support:support-core-ui',
    'com.android.support:support-media-compat',
    'com.android.support:support-fragment',
    'com.android.support:multidex',
    'com.android.support:appcompat-v7',
    'com.android.support:cardview-v7',
    'com.android.support:gridlayout-v7',
    'com.android.support:mediarouter-v7',
    'com.android.support:palette-v7',
    'com.android.support:recyclerview-v7',
    'com.android.support:preference-v7',
    'com.android.support:support-v13',
    'com.android.support:preference-v14',
    'com.android.support:preference-leanback-v17',
    'com.android.support:leanback-v17',
    'com.android.support:support-vector-drawable',
    'com.android.support:animated-vector-drawable',
    'com.android.support:support-annotations',
    'com.android.support:design',
    'com.android.support:customtabs',
    'com.android.support:percent',
    'com.android.support:exifinterface',
    'com.android.support:recommendation',
    'com.android.support:wear'
]

artifacts = map(lambda x: x.split(':')[1], support_libraries)

def fetch_metadata(name):
    path = name.replace('.', '/').replace(':', '/')
    url = google_maven_url.format(path)
    xml = requests.get(url).text
    tree = ET.fromstring(xml)
    gid = tree.find('groupId').text
    aid = tree.find('artifactId').text
    assert '{}:{}'.format(gid, aid) == name
    version = tree.find('versioning')
    latest = version.find('latest').text
    release = version.find('release').text
    versions = []
    for v in version.find('versions').findall('version'):
        versions.append(v.text)
    return {'gid': gid, 'aid': aid, 'latest': latest, 'release': release, 'versions': versions}


@click.command()
@click.option('--list', is_flag = True, help='List all android support libraries')
@click.option('--lib', type=click.Choice(artifacts), help='Dump detail information of given lib name')
def process(list, lib):
    if (list):
        print()
        print('Available android support libraries:')
        for x in artifacts:
            print(Fore.GREEN + '* ' + x)
        print('See https://developer.android.com/topic/libraries/support-library/features.html\n')
    elif (lib):
        print()
        metadata = fetch_metadata("com.android.support:" + lib)
        id = '{}:{}'.format(metadata['gid'], metadata['aid'])
        print(Fore.GREEN + id)
        print('---------')
        print('{:20}{}{}'.format('LATEST VERSION:', Fore.GREEN, metadata['latest']))
        print('{:20}{}{}'.format('RELEASE VERSION:', Fore.GREEN, metadata['latest']))
        print('{:20}{}{}'.format('INSTALL:', Fore.GREEN, 'implementation \'{}:{}:{}\''.format(metadata['gid'], metadata['aid'], metadata['release'])))
        print('{:20}{}{}'.format('CHANGES:', Fore.GREEN, 'https://developer.android.com/topic/libraries/support-library/revisions.html'))
        print()
    else:
        print('use --help for more information')

if __name__ == '__main__':
    process()