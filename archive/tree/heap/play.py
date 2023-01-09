import itertools
import heapq


# create a heap with existing items
# 1.add one by one O(nlogn)
# 2. heapify O(n)

# max heap trick
maxHeap = [1, 2, 3]
maxHeap = [-x for x in maxHeap]

heapq.heapify(maxHeap)


print(heapq.heappop(maxHeap))


# heapsort

# time O(nlogn)
# space O(n)
def heapsort(iterable):
    h = [x for x in iterable]
    heapq.heapify(h)
    # for value in iterable:
    #     heapq.heappush(h, value)

    return [heapq.heappop(h) for i in range(len(h))]


res = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])

print(res)

# priority queue
h = []
heapq.heappush(h, (5, 'write code'))
heapq.heappush(h, (7, 'release product'))
heapq.heappush(h, (1, 'write spec'))
heapq.heappush(h, (3, 'create tests'))
print(heapq.heappop(h))


# task queue can be remove
# Removing the entry or changing its priority is more difficult because it would break the heap structure invariants.
# So, a possible solution is to mark the entry as removed and add a new entry with the revised priority:
pq = []                         # list of entries arranged in a heap
entry_finder = {}               # mapping of tasks to entries
REMOVED = '<removed-task>'      # placeholder for a removed task
counter = itertools.count()     # unique sequence count


def add_task(task, priority=0):
    'Add a new task or update the priority of an existing task'
    if task in entry_finder:
        remove_task(task)
    count = next(counter)
    entry = [priority, count, task]
    entry_finder[task] = entry
    heapq.heappush(pq, entry)


def remove_task(task):
    'Mark an existing task as REMOVED.  Raise KeyError if not found.'
    entry = entry_finder.pop(task)
    entry[-1] = REMOVED


def pop_task():
    'Remove and return the lowest priority task. Raise KeyError if empty.'
    while pq:
        priority, count, task = heapq.heappop(pq)
        if task is not REMOVED:
            del entry_finder[task]
            return task
    raise KeyError('pop from an empty priority queue')
