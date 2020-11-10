from itertools import permutations


class Solution:

    def evaluate(self, board):
        toPop = set()
        lines = []
        colors = {}

        for c in range(len(board)):
            for i in range(len(board[c])):
                try:
                    colors[f'{board[c][i]}'].append((c, i))
                except KeyError:
                    colors[f'{board[c][i]}'] = [(c, i)]

        for points in colors.values():
            for x, y in [(1, 0), (0, 1), (1, 1), (-1, 1)]:
                ps = set(points)
                for p in ps:
                    if (p[0] - x, p[1] - y) in ps and (p[0] + x, p[1] + y) in ps:
                        toPop.update({p, (p[0] - x, p[1] - y), (p[0] + x, p[1] + y)})
                        ps = ps - {(p[0] - x, p[1] - y), (p[0] + x, p[1] + y)}
                        f, b = 2, 2
                        while (p[0] + f*x, p[1] + f*y) in ps:
                            toPop.update({(p[0] + f*x, p[1] + f*y)})
                            ps = ps - {(p[0] + f*x, p[1] + f*y)}
                            f += 1
                        while (p[0] - b*x, p[1] - b*y) in ps:
                            toPop.update({(p[0] - b*x, p[1] - b*y)})
                            ps = ps - {(p[0] - b*x, p[1] - b*y)}
                            b += 1
                        lines.append(f + b - 1)
        '''for c in board:
            print(c)
        print('lines:', lines)'''

        for x, y in toPop:
            board[x][y] = 0

        for col in board:
            while 0 in col:
                col.remove(0)

        score = sum([line**2 for line in lines]) * len(lines)

        return score

    def getMaxScore(self, count, up, mid, down, col, changeCount):
        scores = set()

        board = [[], [], [], [], []]
        totalScore = 0
        for i in range(len(col)):
            board[col[i]] += [down[i], mid[i], up[i]]
            e = 1
            while True:
                etapScore = self.evaluate(board)
                if etapScore == 0:
                    break
                totalScore += etapScore * e
                e += 1
        scores.add(totalScore)

        if changeCount == 1:
            for pos in range(len(col)):
                for np in range(5):
                    for nc in permutations([up, mid, down]):
                        board = [[], [], [], [], []]
                        totalScore = 0
                        for i in range(len(col)):
                            if i == pos:
                                board[np] += [nc[0][i], nc[1][i], nc[2][i]]
                            else:
                                board[col[i]] += [down[i], mid[i], up[i]]
                            e = 1
                            while True:
                                etapScore = self.evaluate(board)
                                if etapScore == 0:
                                    break
                                totalScore += etapScore * e
                                e += 1
                        scores.add(totalScore)

        elif changeCount == 2:
            for pos in range(len(col)):
                for pos2 in range(len(col)):
                    for np in range(5):
                        for nc in permutations([up, mid, down]):
                            for np2 in range(5):
                                for nc2 in permutations([up, mid, down]):
                                    board = [[], [], [], [], []]
                                    totalScore = 0
                                    for i in range(len(col)):
                                        if i == pos:
                                            board[np] += [nc[0][i], nc[1][i], nc[2][i]]

                                        elif i == pos2:
                                            board[np2] += [nc2[0][i], nc2[1][i], nc2[2][i]]
                                        else:
                                            board[col[i]] += [down[i], mid[i], up[i]]
                                        e = 1
                                        while True:
                                            etapScore = self.evaluate(board)
                                            if etapScore == 0:
                                                break
                                            totalScore += etapScore * e
                                            e += 1

                                    scores.add(totalScore)
        print(scores)
        return max(scores)