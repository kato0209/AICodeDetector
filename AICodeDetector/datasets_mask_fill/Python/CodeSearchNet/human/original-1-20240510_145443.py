
    # Parse arguments
    usage = "usage: nvd3.py [options]"
    parser = OptionParser(usage=usage,
                          version=("python-nvd3 - Charts generator with "
                                   "nvd3.js and d3.js"))
    parser.add_option("-q", "--quiet",
                      action="store_false", dest="verbose", default=True,
          