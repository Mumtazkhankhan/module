def allocate(blocks, processes, method):
    remaining = blocks[:]
    allocation = [-1] * len(processes)

    for i, size in enumerate(processes):
        candidates = [j for j, free in enumerate(remaining) if free >= size]
        if not candidates:
            continue

        if method == "First Fit":
            chosen = candidates[0]
        elif method == "Best Fit":
            chosen = min(candidates, key=lambda j: remaining[j])
        else:  # Worst Fit
            chosen = max(candidates, key=lambda j: remaining[j])

        allocation[i] = chosen
        remaining[chosen] -= size

    print(f"\n{method}")
    print("Process size | Block assigned | Remaining block space")
    for i, size in enumerate(processes):
        block = allocation[i]
        if block == -1:
            print(f"{size:12} | Not allocated | -")
        else:
            print(f"{size:12} | Block {block + 1:<8} | {remaining[block]}")

if __name__ == "__main__":
    # Sizes are illustrative units; this is a simulation, not real RAM allocation.
    blocks = [100, 500, 200, 300, 600]
    processes = [212, 417, 112, 426]
    print("Memory blocks:", blocks)
    print("Process sizes:", processes)
    for method in ("First Fit", "Best Fit", "Worst Fit"):
        allocate(blocks, processes, method)
