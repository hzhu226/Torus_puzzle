import copy
def print_succ(state):
    x = state.index(0)
    if x == 0:
        state_1 = copy.deepcopy(state)
        state_1[x], state_1[6] = state_1[6], state_1[x]
        state_2 = copy.deepcopy(state)
        state_2[x], state_2[2] = state_2[2], state_2[x]
        state_3 = copy.deepcopy(state)
        state_3[x], state_3[1] = state_3[1], state_3[x]
        state_4 = copy.deepcopy(state)
        state_4[x], state_4[3] = state_4[3], state_4[x]
    if x == 1:
        state_1 = copy.deepcopy(state)
        state_1[x], state_1[7] = state_1[7], state_1[x]
        state_2 = copy.deepcopy(state)
        state_2[x], state_2[0] = state_2[0], state_2[x]
        state_3 = copy.deepcopy(state)
        state_3[x], state_3[2] = state_3[2], state_3[x]
        state_4 = copy.deepcopy(state)
        state_4[x], state_4[4] = state_4[4], state_4[x]
    if x == 2:
        state_1 = copy.deepcopy(state)
        state_1[x], state_1[8] = state_1[8], state_1[x]
        state_2 = copy.deepcopy(state)
        state_2[x], state_2[1] = state_2[1], state_2[x]
        state_3 = copy.deepcopy(state)
        state_3[x], state_3[0] = state_3[0], state_3[x]
        state_4 = copy.deepcopy(state)
        state_4[x], state_4[5] = state_4[5], state_4[x]
    if x == 3:
        state_1 = copy.deepcopy(state)
        state_1[x], state_1[0] = state_1[0], state_1[x]
        state_2 = copy.deepcopy(state)
        state_2[x], state_2[5] = state_2[5], state_2[x]
        state_3 = copy.deepcopy(state)
        state_3[x], state_3[4] = state_3[4], state_3[x]
        state_4 = copy.deepcopy(state)
        state_4[x], state_4[6] = state_4[6], state_4[x]
    if x == 4:
        state_1 = copy.deepcopy(state)
        state_1[x], state_1[1] = state_1[1], state_1[x]
        state_2 = copy.deepcopy(state)
        state_2[x], state_2[3] = state_2[3], state_2[x]
        state_3 = copy.deepcopy(state)
        state_3[x], state_3[5] = state_3[5], state_3[x]
        state_4 = copy.deepcopy(state)
        state_4[x], state_4[7] = state_4[7], state_4[x]
    if x == 5:
        state_1 = copy.deepcopy(state)
        state_1[x], state_1[2] = state_1[2], state_1[x]
        state_2 = copy.deepcopy(state)
        state_2[x], state_2[4] = state_2[4], state_2[x]
        state_3 = copy.deepcopy(state)
        state_3[x], state_3[3] = state_3[3], state_3[x]
        state_4 = copy.deepcopy(state)
        state_4[x], state_4[8] = state_4[8], state_4[x]
    if x == 6:
        state_1 = copy.deepcopy(state)
        state_1[x], state_1[3] = state_1[3], state_1[x]
        state_2 = copy.deepcopy(state)
        state_2[x], state_2[8] = state_2[8], state_2[x]
        state_3 = copy.deepcopy(state)
        state_3[x], state_3[7] = state_3[7], state_3[x]
        state_4 = copy.deepcopy(state)
        state_4[x], state_4[0] = state_4[0], state_4[x]
    if x == 7:
        state_1 = copy.deepcopy(state)
        state_1[x], state_1[4] = state_1[4], state_1[x]
        state_2 = copy.deepcopy(state)
        state_2[x], state_2[6] = state_2[6], state_2[x]
        state_3 = copy.deepcopy(state)
        state_3[x], state_3[8] = state_3[8], state_3[x]
        state_4 = copy.deepcopy(state)
        state_4[x], state_4[1] = state_4[1], state_4[x]
    if x == 8:
        state_1 = copy.deepcopy(state)
        state_1[x], state_1[5] = state_1[5], state_1[x]
        state_2 = copy.deepcopy(state)
        state_2[x], state_2[7] = state_2[7], state_2[x]
        state_3 = copy.deepcopy(state)
        state_3[x], state_3[6] = state_3[6], state_3[x]
        state_4 = copy.deepcopy(state)
        state_4[x], state_4[2] = state_4[2], state_4[x]

    state_all = [state_1, state_2, state_3, state_4]
    sorted(state_all)
    initial = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    a = 0
    for x in state_all[0]:
        if  x != 0 and x != initial[state_all[0].index(x)]:
            a = a + 1
    print(str(state_all[0]) + ' h=' + str(a))
    b = 0
    for x in state_all[1]:
        if x != 0 and x != initial[state_all[1].index(x)]:
            b = b + 1
    print(str(state_all[1]) + ' h=' + str(b))
    c = 0
    for x in state_all[2]:
        if x != 0 and x != initial[state_all[2].index(x)]:
            c = c + 1
    print(str(state_all[2]) + ' h=' + str(c))
    d = 0
    for x in state_all[3]:
        if x != 0  and x != initial[state_all[3].index(x)]:
            d = d + 1
    print(str(state_all[3]) + ' h=' + str(d))

''' author: hobbes
    source: cs540 canvas
'''
class PriorityQueue(object):
    def __init__(self):
        self.queue = []
        self.max_len = 0

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, state_dict):
        in_open = False
        for x in self.queue:
            if state_dict['state'] == x['state']:
                in_open = True
                if state_dict['g'] < x['g']:
                    x['g'] = state_dict['g']

        if not in_open:
            self.queue.append(state_dict)

        if len(self.queue) > self.max_len:
            self.max_len = len(self.queue)

    def requeue(self, from_closed):
        self.queue.append(from_closed)
        if len(self.queue) > self.max_len:
            self.max_len = len(self.queue)

    def pop(self):
        minf = 0
        for i in range(1, len(self.queue)):
            if self.queue[i]['f'] < self.queue[minf]['f']:
                minf = i
        state = self.queue[minf]
        del self.queue[minf]
        return state

def count_h(state):
    initial = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    h = 0
    for x in state:
        if x != 0 and x != initial[state.index(x)]:
            h = h + 1
    return h

def generate_succ(state):
    x = state.index(0)
    if x == 0:
        state_1 = copy.deepcopy(state)
        state_1[x], state_1[6] = state_1[6], state_1[x]
        state_2 = copy.deepcopy(state)
        state_2[x], state_2[2] = state_2[2], state_2[x]
        state_3 = copy.deepcopy(state)
        state_3[x], state_3[1] = state_3[1], state_3[x]
        state_4 = copy.deepcopy(state)
        state_4[x], state_4[3] = state_4[3], state_4[x]
    if x == 1:
        state_1 = copy.deepcopy(state)
        state_1[x], state_1[7] = state_1[7], state_1[x]
        state_2 = copy.deepcopy(state)
        state_2[x], state_2[0] = state_2[0], state_2[x]
        state_3 = copy.deepcopy(state)
        state_3[x], state_3[2] = state_3[2], state_3[x]
        state_4 = copy.deepcopy(state)
        state_4[x], state_4[4] = state_4[4], state_4[x]
    if x == 2:
        state_1 = copy.deepcopy(state)
        state_1[x], state_1[8] = state_1[8], state_1[x]
        state_2 = copy.deepcopy(state)
        state_2[x], state_2[1] = state_2[1], state_2[x]
        state_3 = copy.deepcopy(state)
        state_3[x], state_3[0] = state_3[0], state_3[x]
        state_4 = copy.deepcopy(state)
        state_4[x], state_4[5] = state_4[5], state_4[x]
    if x == 3:
        state_1 = copy.deepcopy(state)
        state_1[x], state_1[0] = state_1[0], state_1[x]
        state_2 = copy.deepcopy(state)
        state_2[x], state_2[5] = state_2[5], state_2[x]
        state_3 = copy.deepcopy(state)
        state_3[x], state_3[4] = state_3[4], state_3[x]
        state_4 = copy.deepcopy(state)
        state_4[x], state_4[6] = state_4[6], state_4[x]
    if x == 4:
        state_1 = copy.deepcopy(state)
        state_1[x], state_1[1] = state_1[1], state_1[x]
        state_2 = copy.deepcopy(state)
        state_2[x], state_2[3] = state_2[3], state_2[x]
        state_3 = copy.deepcopy(state)
        state_3[x], state_3[5] = state_3[5], state_3[x]
        state_4 = copy.deepcopy(state)
        state_4[x], state_4[7] = state_4[7], state_4[x]
    if x == 5:
        state_1 = copy.deepcopy(state)
        state_1[x], state_1[2] = state_1[2], state_1[x]
        state_2 = copy.deepcopy(state)
        state_2[x], state_2[4] = state_2[4], state_2[x]
        state_3 = copy.deepcopy(state)
        state_3[x], state_3[3] = state_3[3], state_3[x]
        state_4 = copy.deepcopy(state)
        state_4[x], state_4[8] = state_4[8], state_4[x]
    if x == 6:
        state_1 = copy.deepcopy(state)
        state_1[x], state_1[3] = state_1[3], state_1[x]
        state_2 = copy.deepcopy(state)
        state_2[x], state_2[8] = state_2[8], state_2[x]
        state_3 = copy.deepcopy(state)
        state_3[x], state_3[7] = state_3[7], state_3[x]
        state_4 = copy.deepcopy(state)
        state_4[x], state_4[0] = state_4[0], state_4[x]
    if x == 7:
        state_1 = copy.deepcopy(state)
        state_1[x], state_1[4] = state_1[4], state_1[x]
        state_2 = copy.deepcopy(state)
        state_2[x], state_2[6] = state_2[6], state_2[x]
        state_3 = copy.deepcopy(state)
        state_3[x], state_3[8] = state_3[8], state_3[x]
        state_4 = copy.deepcopy(state)
        state_4[x], state_4[1] = state_4[1], state_4[x]
    if x == 8:
        state_1 = copy.deepcopy(state)
        state_1[x], state_1[5] = state_1[5], state_1[x]
        state_2 = copy.deepcopy(state)
        state_2[x], state_2[7] = state_2[7], state_2[x]
        state_3 = copy.deepcopy(state)
        state_3[x], state_3[6] = state_3[6], state_3[x]
        state_4 = copy.deepcopy(state)
        state_4[x], state_4[2] = state_4[2], state_4[x]
    succ = []
    succ.append(state_1)
    succ.append(state_2)
    succ.append(state_3)
    succ.append(state_4)
    return succ


def solve(state):
    h = count_h(state)
    g = 0
    f = g + h
    state_dict = {'state': state, 'h': h, 'g': g, 'parent': 'None', 'f': f}
    close_list = []
    pq = PriorityQueue()
    pq.enqueue(state_dict)

    while not pq.is_empty():
        state0 = pq.pop()
        close_list.append(state0)

        if state0['state'] == [1, 2, 3, 4, 5, 6, 7, 8, 0]:
            break
        succ = generate_succ(state0['state'])
        for x in succ:
            succ_dict = {}
            succ_dict['state'] = x
            succ_dict['h'] = count_h(x)
            succ_dict['g'] = state0['g'] + 1
            succ_dict['parent'] = state0['state']
            succ_dict['f'] = succ_dict['h'] + succ_dict['g']
            pq.enqueue(succ_dict)

    goal_dict = close_list[len(close_list) - 1]


    route = []
    route.append(goal_dict)
    print(route)
    is_initial = True
    prev = copy.deepcopy(goal_dict)
    while is_initial:
        for x in range(len(close_list)):
            if close_list[x]['state'] == prev['parent']:
                route.append(close_list[x])
                prev = close_list[x]
                if close_list[x]['parent'] == 'None':
                    is_initial = False
                break

    route.reverse()
    z = 0

    for y in route:
        print(str(y['state']) + '  h=' + str(y['h']) + '  moves: ' + str(z))
        z = z + 1
    print('Max queue length: ', pq.max_len)