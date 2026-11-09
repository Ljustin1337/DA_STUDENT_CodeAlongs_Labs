#!/usr/bin/env python3
"""One Job at a Time: see DataChallengeOverview&Steps.md for the steps."""

import json

DATA_FILE = "/Users/jlee333/Desktop/DA_STUDENT_CodeAlongs_Labs/module-1-python-foundations/data-challenges/one-job-at-a-time/pantry_donations.csv"  # edit the filepath with the data


# ===== Day 1 =====

# Step 1: Write the Read-and-Validate Pair, Each With a Docstring
def read_donations(path):
    """Read the donation log into one raw string per record."""
    records = []
    with open(path) as f:
        for line in f.read().splitlines()[1:]:
            if line.strip():
                records.append(line)
    return records


def validate_donation(record):
    # TODO: add a one-sentence docstring naming its one job
    """ Return a verdict or reason of a record"""
    # TODO: assign `parts` to `record` split on commas
    parts = record.split(",")
    # TODO: return False, "wrong field count" if `parts` lacks 5 fields
    if len(parts) != 5: 
        return (False, "wrong field count")
    # TODO: return False, "missing category" if parts[2].strip() is ""
    if parts[2].strip() == "":
        return (False,"missing category")
    # TODO: in a try, call float(parts[3])
    try:
        float(parts[3])
    except ValueError:
        return (False, "pounds is not a number")
    return (True,"")
      
    # TODO: in except ValueError, return False, "pounds is not a number"
    # TODO: return True and ""


# TODO: assign `records` to read_donations(DATA_FILE), `valid` to []
records = read_donations(DATA_FILE)
valid = []
# TODO: loop over `records`; unpack validate_donation(record) as ok, reason
for record in records:
    ok, reasons = validate_donation(record) 
# TODO: if `ok`, append `record` to `valid`
    if ok:
        valid.append(record)
# TODO: else print "rejected", the record's ID plus ":", and `reason`
    else:
        print("rejected", record.split(",")[0] + ":", reasons)
print(len(valid), "usable records out of", len(records))

# Step 1, answer 1:
#
# Step 1, answer 2:
#


# Step 2: Write `summarize_donations()` for the Category Breakdown Only
def summarize_donations(valid_records):
    # TODO: add a one-sentence docstring naming its one job
    """ Adding values into the donation lines """
    # TODO: assign `by_category` to {} and `total_pounds` to 0.0

    by_category = {}
    total_pounds = 0.0
    # TODO: loop over `valid_records`; split each record on commas into `parts`

    for records in valid_records:
        parts = record.split(",")
        category = parts[2]
        pounds = float(parts[3])
    # TODO: assign `category` to parts[2], `pounds` to float(parts[3])
    # TODO: if `category` is not in `by_category`, add an entry for it

        if category not in by_category:
            by_category[category] = {"donations": 0, "pounds": 0.0}
    # TODO: start that entry as {"donations": 0, "pounds": 0.0
    # TODO: add 1 to its "donations" and `pounds` to its "pounds"
        by_category[category]["donations"] += 1
        by_category[category]["pounds"] += pounds
        total_pounds += pounds             

    # TODO: add `pounds` to `total_pounds`
    # TODO: return a dict of "records", "total_pounds" and "by_category"
    return { "records": len(valid_records),
             "total_pounds": total_pounds,
             "by_category": by_category,
    }
    
    


# TODO: assign `summary` to summarize_donations(valid)
summary = summarize_donations(valid)
print("records:", summary["records"], "| total pounds:",
      summary["total_pounds"])
for category, stats in summary["by_category"].items():
    print(category, stats["donations"], "donations,", stats["pounds"],
          "lbs")

# Step 2, answer 1:
#


# ===== Day 2 =====

# Step 3: Add `export_summary()` and `run_pipeline()`, Then Print Docstrings
def export_summary(summary, path):
    """Summary Dictionary for JSON file to return to path"""
    with open(path, "w")as f:
        json.dump(summary, f, indent=2)
    return path    
    # TODO: add a one-sentence docstring naming its one job
    # TODO: in a with open(path, "w") block, json.dump `summary`, indent=2
    # TODO: return `path`
    


def run_pipeline(in_path, out_path, summarize):
    """Read, Validate, and expoting the log in one call"""
    kept = []
    for record in read_donations(in_path):
        ok, reason = validate_donation(record)
        if ok:
            kept.append(record)
    return export_summary(summarize(kept), out_path)
        

    # TODO: add a one-sentence docstring naming its one job
    # TODO: assign `kept` to [] and loop over read_donations(in_path)
    # TODO: append each record that validate_donation() passes to `kept`
    # TODO: return export_summary() of summarize(kept) and `out_path`
    


written = run_pipeline(DATA_FILE, "donation_summary.json",
                       summarize_donations)
print("wrote", written)
for func in [read_donations, validate_donation, summarize_donations,
             export_summary]:
    print(func.__name__ + ":", func.__doc__.splitlines()[0])

# Step 3, answer 1:
#
# Step 3, answer 2:
#


# Step 4: Swap In `summarize_by_day()` and Count the Functions You Edited
def summarize_by_day(valid_records):
    """Total donation count and pounds aquired per day"""
    by_day = {}
    total_pounds = 0.0

    for records in valid_records:
        parts = record.split(",")
        day = parts[4]
        pounds = float(parts[3])


        if day not in by_day:
            by_day[day] = {"donations": 0, "pounds": 0.0}
        
        by_day[day]["donations"] += 1
        by_day[day]["pounds"] += pounds
        total_pounds += pounds             

    return { 
        "records": len(valid_records),
        "total_pounds": total_pounds,
        "by_day": by_day,
    }
    # TODO: add a one-sentence docstring naming its one job
    # TODO: return the same dict shape, with "by_day" keyed by parts[4]

    


# TODO: call run_pipeline(DATA_FILE, "donation_summary.json", summarize_by_day)

run_pipeline(DATA_FILE, "donation_summary.json", summarize_by_day)
# TODO: replace None with json.load() of "donation_summary.json"

with open("donation_summary.json") as f:
    reloaded = json.load(f)

print("records:", reloaded["records"], "| total pounds:",
      reloaded["total_pounds"])
for day, stats in sorted(reloaded["by_day"].items()):
    print(day, stats["donations"], "donations,", stats["pounds"], "lbs")

# Step 4, answer 1:

#
# Step 4, answer 2:
#
