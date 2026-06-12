# req_lint.py — Week 1 exercise

WEAK_WORDS = ["appropriate", "adequate", "as required", "etc", "and/or", "as needed", "periodically"]
MAX_WORDS = 30

def check_requirement(req_text):
    """Check one requirement line. Return a list of issue strings."""
    issues = []

    # TODO 1: if "shall" is not in req_text (lowercase it first!),
    #         add "Missing 'shall'" to issues
    if "shall" not in req_text.lower():
        issues.append("missing 'shall'")

    # TODO 2: loop over WEAK_WORDS; if a word is in req_text (lowercased),
    #         add f"Weak word: '{word}'" to issues
    for WORD in WEAK_WORDS:
        if WORD in req_text.lower():
            issues.append(f"Weak word: '{WORD}'")
    # TODO 3: count words with len(req_text.split()); if over MAX_WORDS,
    #         add f"Too long: {count} words"
    countLen=len(req_text.split())
    if countLen>=MAX_WORDS:
        issues.append(f"Too long: {countLen} words")

    return issues

def main():
    with open("sample_reqs.txt", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            issues = check_requirement(line)
            #print(f"total lines {line}")
            #print(f"issu list {issues}")
            req_id = line.split(":")[0]
            if issues:
                print(f"{req_id}: FAIL")
                for issue in issues:
                    print(f"   - {issue}")
            else:
                print(f"{req_id}: PASS")

if __name__ == "__main__":
    main()