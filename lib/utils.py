
def plot_policy(q, border):
    s = ''
    idx = q.argmax(axis=2)
    nrows, ncols = border.shape
    for i in range(nrows):
        for j in range(ncols):
            if border[i, j]:
                s += ' '
            elif idx[i,j] == 0:
                s += u'\u2190'
            elif idx[i,j] == 1:
                s += u'\u2192'
            elif idx[i,j] == 2:
                s += u'\u2191'
            elif idx[i,j] == 3:
                s += u'\u2193'
            else:
                raise ValueError()
            s += '\t'
        s += '\n'

    print s
