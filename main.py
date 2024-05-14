import sys
import utils

def get_mktStatus():
    if len(sys.argv)>1:
        try:
            return utils.MktStatus(sys.argv[1])
        except ValueError:
            raise NotImplementedError("Undefined Market Status")
    else:
        raise NotImplementedError("Undefined Market Status")

if __name__ ==  '__main__':
    mkt_status = get_mktStatus()
    print(mkt_status)