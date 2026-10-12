def report(name, processes):
    # Each process is (PID/name, arrival time, burst time).
    time = 0
    rows = []
    for pid, arrival, burst in processes:
        time = max(time, arrival)
        start = time
        time += burst
        completion = time
        turnaround = completion - arrival
        waiting = turnaround - burst
        rows.append((pid, arrival, burst, completion, turnaround, waiting))

    print(f"\n{name}")
    print("PID  Arrival  Burst  Complete  Turnaround  Waiting")
    for row in rows:
        print(f"{row[0]:<4} {row[1]:<8} {row[2]:<6} {row[3]:<9} {row[4]:<11} {row[5]}")
    print("Average waiting time:", round(sum(r[5] for r in rows) / len(rows), 2))

def round_robin(processes, quantum):
    remaining = {pid: burst for pid, arrival, burst in processes}
    arrivals = {pid: arrival for pid, arrival, burst in processes}
    bursts = {pid: burst for pid, arrival, burst in processes}
    completion = {}
    time = 0
    ready = []
    pending = sorted(processes, key=lambda p: p[1])
    i = 0

    while len(completion) < len(processes):
        while i < len(pending) and pending[i][1] <= time:
            ready.append(pending[i][0])
            i += 1
        if not ready:
            time = pending[i][1]
            continue
        pid = ready.pop(0)
        run = min(quantum, remaining[pid])
        time += run
        remaining[pid] -= run
        while i < len(pending) and pending[i][1] <= time:
            ready.append(pending[i][0])
            i += 1
        if remaining[pid] > 0:
            ready.append(pid)
        else:
            completion[pid] = time

    print(f"\nRound Robin (quantum={quantum})")
    print("PID  Arrival  Burst  Complete  Turnaround  Waiting")
    waits = []
    for pid, arrival, burst in processes:
        tat = completion[pid] - arrival
        wait = tat - burst
        waits.append(wait)
        print(f"{pid:<4} {arrival:<8} {burst:<6} {completion[pid]:<9} {tat:<11} {wait}")
    print("Average waiting time:", round(sum(waits) / len(waits), 2))

if __name__ == "__main__":
    # Edit these sample processes to test other inputs.
    processes = [("P1", 0, 5), ("P2", 1, 3), ("P3", 2, 8), ("P4", 3, 6)]
    print("Sample processes (name, arrival time, burst time):", processes)
    report("FCFS", sorted(processes, key=lambda p: (p[1], p[0])))
    report("Non-preemptive SJF (all sample jobs considered by arrival order)", sorted(processes, key=lambda p: (p[1], p[2])))
    round_robin(processes, quantum=2)
