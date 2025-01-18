def setup():
    from .system import System as osystem
    from data import Data as odata
    import sys
    sys.path.append("./utils")
    sys.path.append("./data")
    sys.path.append("./assets")
    sys.path.append("./ui")
    globals()["System"] = osystem()
    globals()["Data"] = odata()
