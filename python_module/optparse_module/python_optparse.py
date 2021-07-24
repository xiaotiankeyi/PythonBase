# optparse模块处理命令行参数

import optparse
from optparse import OptionParser


class handle():
    def __init__(self):
        self.op = optparse.OptionParser()

        self.op.add_option("-s", '--server', dest="server")

        self.accept, self.args = self.op.parse_args(self)

        self.verify_args(self.accept, self.args)

    def verify_args(self, accept, args):
        pass


def func_main():
    parser = OptionParser()
    parser.add_option(
        "-f",
        "--file",
        dest="filename",
        help="write report to FILE",
        metavar="FILE")
    parser.add_option(
        "-q",
        "--quiet",
        action="store_false",
        dest="verbose",
        default=True,
        help="don't print status messages to stdout")

    (options, args) = parser.parse_args()


if __name__ == "__main__":
    # handle()
    func_main()