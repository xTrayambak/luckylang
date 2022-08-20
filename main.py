import argparse
import os

from lucky.runtime import Runtime

class Interface:
    def __init__(self):
        arg_parser = argparse.ArgumentParser()
        arg_parser.add_argument('--compile', '-c', help = 'Compile a Lucky source file.', type = str, default = None, required = False)
        arg_parser.add_argument('--optimization-level', '-ol', help = 'The level of optimization (-o2 recommended, -o3 and above produce unstable binaries)', type = int, default = 1, required = False)
        arg_parser.add_argument('--version', '-v', help = 'Get the version of the Lucky runtime environment you are currently running.', action = 'store_true')
        arg_parser.add_argument('--output', '-o', help = 'The file to output the binary into.', type = str, default = None, required = False)

        self.arg_parser = arg_parser
        self.__version = '0.0.1-r1'

    def run(self):
        args = self.arg_parser.parse_args()

        if args.version:
            print(f'Lucky Runtime Environment {self.__version}')
            exit(0)

        if args.compile:
            source_file = args.compile
            if not os.path.exists(source_file):
                print('lucky: error: source file not found')
                exit(-1)

            if not os.path.isfile(source_file):
                print('lucky: error: source file is a directory. Did you mean "lucky project run"?')
                exit(-1)

            if args.output != None:
                output_file = args.output
            else:
                output_file = 'a.out'

            if args.optimization_level != None:
                opt_level = args.optimization_level
            else:
                opt_level = args.optimization_level

            rtime = Runtime(source_file)

            exit(0)

        self.show_help()
        exit(0)

    def show_help(self):
        print('''Usage: lucky [arguments]
Lucky Runtime Environment

Options:
\t
\t--compile [-c]\t:\tCompile a source file into a binary, without a Lucky project.
\t--version [-v]\t:\tDisplay the version of the runtime installed.
\t--optimization-level [-ol]\t:\tThe level of optimization that the binary should go through (-o2 is recommended, -o3 and above generate unstable binaries. Defaults to -o1)
\t--output [-o]\t:\tThe file to output the binary to.
        '''
        )

if __name__ == '__main__':
    interface = Interface()
    interface.run()
