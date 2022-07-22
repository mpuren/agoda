
import json
from typing import List
import numpy as np
import sys

def sort_entries(entries: List, columns: "List[(int, int, int, int)]", *,
                 skip_error: bool = True) -> int:

    e_coords = np.array([e["box"] for e in entries], dtype="int")
    e_center_x = e_coords[:,0] + e_coords[:,2] // 2
    e_center_y = e_coords[:,1] + e_coords[:,3] // 2

    buckets = np.array([e["box"] for e in columns], dtype="int")
    # (x,y,w,h) => (x0,y0,x1,y1)
    x0 = buckets[:,0]
    y0 = buckets[:,1]
    x1 = buckets[:,0] + buckets[:,2]
    y1 = buckets[:,1] + buckets[:,3]

    bucket_has = np.logical_and.reduce([
        x0[:, np.newaxis] <= e_center_x[np.newaxis,:],
        x1[:, np.newaxis] > e_center_x[np.newaxis,:],
        y0[:, np.newaxis] <= e_center_y[np.newaxis,:],
        y1[:, np.newaxis] > e_center_y[np.newaxis,:]
    ])
 
    keys = np.argmax(bucket_has, axis=0)

    # error_txt = "The box ({}) is not included in any columns"

    for i, e in enumerate(entries):
        k = int(keys[i])
        if not bucket_has[k, i]:
            err = f"The entry {e} is not included in any column."
            e["key"] = (np.inf, np.inf)
            if not skip_error:
                raise RuntimeError(err)
        else:
            e["key"] = (k, int(e_center_y[i]))
    entries.sort(key = lambda e: e["key"])
    
def process(path_in, path_out):

    with open(path_in) as f:
        data = json.load(f)

    types_to_sort = ('ENTRY', "TITLE_LEVEL_2")

    entries = [e for e in data if e["type"] in types_to_sort]
    columns = [e for e in data if e["type"] == 'COLUMN_LEVEL_1']
    sort_entries(entries, columns)
    all = [e for e in data if e["type"] not in types_to_sort]
    all.extend(entries)
    
    with open(path_out, "w") as f:
        json.dump(all, f, indent=True, ensure_ascii=False)


if len(sys.argv) != 3:
    print("""
    Usage: {} input.json output.json

    Reorder the entries of a json file.
    """
    .format(sys.argv[0]))
    exit(1)

process(sys.argv[1], sys.argv[2])

