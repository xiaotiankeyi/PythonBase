import optparse


class handle():
    def __init__(self):
        self.op = optparse.OptionParser()

        self.op.add_option("-s", '--server', dest="server")

        self.accept, self.args = self.op.parse_args(self)

        self.verify_args(self.accept, self.args)

    def verify_args(self, accept, args):
        pass