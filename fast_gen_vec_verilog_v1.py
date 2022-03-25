#!/homea01/users/tytu/anaconda3/bin/python3.7
# coding: utf-8

import os
from os.path import join
import sys
import getopt

#def list_file(path):
#    file_name = []
#    for file in os.listdir(path):
#        if file.endswith('.in'):
#            file_name.append(file)
#    return file_name

def list_file(path):
    file_name = []
    root = path
    alllist = os.walk(root)
    for root, dirs, files in alllist:
        for f in files:
            fullpath = join(root, f)
            if fullpath.endswith('.in.repeatclk') or fullpath.endswith('.in.temp'):
                file_name.append(fullpath)
    return file_name


def write_file(run_name, folder_name, vecgen, file, latency, mode):
    with open(run_name, 'w', encoding='utf-8') as f:
        f.write("#! /bin/bash\n")
        f.write("vecgenpath=\'/DR00/............dddd")
        x = '${vecgenpath}/'
        for file_name in file:
            f.write(f'{x}{vecgen}\t{file_name}\t{latency}\t{mode}\n')
            print(f'{x}{vecgen}\t{file_name}\t{latency}\t{mode}\n')
    return run_name

def print_usage():
    print('fast_gen_vec_verilog.py OPTIONS')
    print('OPTIONS')
    print('{:>6} {}'.format('-h', 'tell you how to use this program'))
    print('{:>6} {:<20}{}'.format('-f','--file_path', 'enter vector path'))
    print('{:>6} {:<20}{}'.format('-r','--run_name', 'enter run file name'))
    print('{:>6} {:<20}{}'.format('-l','--latency', 'enter latency'))
    print('{:>6} {:<20}{}'.format('-m','--mode', 'enter x8 or x16 mode'))
    print('{:>6} {:<20}{}'.format('-v','--version', 'enter vector version => Hyper_plus_vecgen_v2'))

def main():
    short_opts = 'hf:r:v:l:m:'
    long_opts = 'file_path= run_name='.split()
    try:
        opts, args = getopt.getopt(sys.argv[1:], short_opts, long_opts)
    except getopt.GetoptError:
        print_usage()
        sys.exit(2)
    
    file_path = ''
    run_name = ''
    mode = 'x16'
    vec_version = 'Hyper_plus_vecgen_v2'
    latency = '7'
    for opt, arg in opts:
        if opt == '-h':
            print_usage()
            sys.exit(0)
        elif opt in ("-f", "--file_path"):
            file_path = arg
        elif opt in ("-r", "--run_name"):
            run_name = arg
        elif opt in ("-v", "--version"):
            vec_version = arg
        elif opt in ("-l", "--latency"):
            latency = arg
        elif opt in ("-m", "--mode"):
            mode = arg
    
    if not file_path or not run_name:
        print_usage()
        sys.exit(2)
    
    file = list_file(file_path)
    result_file = write_file(run_name, file_path, vec_version, file, latency, mode)
    os.chmod(result_file, 0o750)

if __name__ == '__main__':
    main()


