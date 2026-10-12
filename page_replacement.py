def fifo(pages, capacity):
    frames = []
    next_to_replace = 0
    faults = 0
    print("\nFIFO")
    for page in pages:
        hit = page in frames
        if not hit:
            faults += 1
            if len(frames) < capacity:
                frames.append(page)
            else:
                frames[next_to_replace] = page
                next_to_replace = (next_to_replace + 1) % capacity
        print(f"Page {page}: frames={frames} {'HIT' if hit else 'FAULT'}")
    print("Total page faults:", faults)

def lru(pages, capacity):
    frames = []
    last_used = {}
    faults = 0
    print("\nLRU")
    for index, page in enumerate(pages):
        hit = page in frames
        if not hit:
            faults += 1
            if len(frames) < capacity:
                frames.append(page)
            else:
                least_recent = min(frames, key=lambda p: last_used[p])
                frames[frames.index(least_recent)] = page
        last_used[page] = index
        print(f"Page {page}: frames={frames} {'HIT' if hit else 'FAULT'}")
    print("Total page faults:", faults)

if __name__ == "__main__":
    # Example reference string and frame count; change them to experiment.
    pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    capacity = 3
    print("Reference string:", pages)
    print("Number of frames:", capacity)
    fifo(pages, capacity)
    lru(pages, capacity)
