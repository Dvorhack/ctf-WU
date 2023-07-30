#!/usr/bin/env python3

####################
# Author: Dvorhack #
#
# Description 
#   This script is used for managing my write-ups
#   'check' will check if some dir doesn't have the .metadata.yml and the unfinished writeups
#   'update' will update the db.md file 
####################

import argparse, glob, os, shutil, yaml

def get_main_parser():
    parser = argparse.ArgumentParser(prog="manage")
    parser.add_argument('action', help='check or update', nargs='?', choices=('check', 'update', 'stats'))
    return parser

def get_all_ctf():
    files = glob.glob('*/')
    return list(filter(lambda f: os.path.isdir(f), files))

def get_cat_of_ctf(ctf: str):
    files = glob.glob(f'{ctf}/*/')
    return filter(lambda f: os.path.isdir(f), files)

def check():
    filesDepth3 = glob.glob('*/*/*')
    dirsDepth3 = filter(lambda f: os.path.isdir(f), filesDepth3)

    for dir in dirsDepth3:
        if not os.path.isfile(f'{dir}/.meta.yml'):
            print(f'{dir} doesn\'t have metadata file')
            shutil.copyfile('./template_meta.yml', f'{dir}/.meta.yml')

def stats():
    ctfs = get_all_ctf()
    print(f'There is {len(ctfs)}')
    for ctf in ctfs:
        print('\t- '+ ctf)
        for cat in get_cat_of_ctf(ctf):
            print(f'\t\t- {cat}')

def build_db(challs: dict):
    f = open('README.md','w')
    f.write('# Write-ups CTF\n\nWrite-ups repo\n')
    to_write = {}

    for name, chall in challs.items():
        cat = chall['category']
        typ = chall[cat]['type']
        to_write[cat] = to_write.get(cat,{})
        to_write[cat][typ] = to_write[cat].get(typ,[])
        for note in chall[cat]['notes']:
            to_write[cat][typ].append((note, name))

    for cat, data in to_write.items():
        f.write(f'## {cat}\n')

        for typ, notes in data.items():
            f.write(f'### {typ}\n')

            for note in notes:
                f.write(f'- {note[0]} -> [{note[1]}](./{note[1]}/)\n')

def update():
    filesDepth3 = glob.glob('*/*/*')
    dirsDepth3 = filter(lambda f: os.path.isdir(f), filesDepth3)

    challs_data = {}

    for dir in dirsDepth3:
        if not os.path.isfile(f'{dir}/.meta.yml'):
            Exception(f'No meta.yml file in {dir}')
        
        with open(f'{dir}/.meta.yml') as f:
            meta = yaml.load(f, Loader=yaml.loader.SafeLoader)
            if meta['finished']:
                challs_data[dir] = meta.copy()
            else:
                print(f'{dir} unfinished')
    
    build_db(challs_data)
        


if __name__ == "__main__":
    parser = get_main_parser()
    args = parser.parse_args()

    match args.action:
        case 'check':
            check()
        case 'update':
            update()
        case 'stats':
            stats()
        case other:
            print(f'Unknown arg {args.action}')
            exit(-1)