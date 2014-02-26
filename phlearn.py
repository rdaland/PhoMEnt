"""0) import megatableau.py, geneval.py, optimizer.py
1) parse args
2) make empty megatableau (megatableau.py)
3) using arg1 (training data) update mt (geneval.py)
4) using arg3 (alphabet) and arg4 (k), add non-attested forms to mt (geneval.py) *
5) using arg2 (constraints), add violations to mt (geneval.py)
6) (optionally write mt to file)
7) calculate weights (optimizer.py)
8) output stuff


* Beautiful world: if the user supplies an alphabet file, use it to agument tableau; otherwise, search training data for all segments and use those."""