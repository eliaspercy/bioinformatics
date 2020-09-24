import numpy


def row_sums(matrix):
    row_sums = [['Row Sums']]

    for i in range(1, matrix.shape[0]):
        x = 0
        for j in range(1, matrix.shape[1]):
            x += float(matrix[i, j])
        row_sums += [[x]]
    np_row_sums = numpy.array(row_sums)
    return np_row_sums


def Q(d, r, rs1, rs2):
    return (r - 1) * float(d) - float(rs1) - float(rs2)


def Q_scores_axis(matrix, matrix_with_RS, r):
    Q_scores_ = [matrix[0]]
    for i in range(1, matrix_with_RS.shape[0]):
        Q_scores_row = [matrix[i, 0]]
        for j in range(1, matrix_with_RS.shape[0]):
            if i == j:
                Q_scores_row += [0]
            else:
                Q_scores_row += [Q(matrix_with_RS[i, j], r, matrix_with_RS[i, matrix_with_RS.shape[0]],
                                    matrix_with_RS[j, matrix_with_RS.shape[0]])]
        Q_scores_ += [Q_scores_row]
    Q_scores_matrix = numpy.array(Q_scores_)
    return Q_scores_matrix


def Q_scores_sans_axis(matrix_with_RS, r):
    Q_scores_ = []
    for i in range(1, matrix_with_RS.shape[0]):
        Q_scores_row = []
        for j in range(1, matrix_with_RS.shape[0]):
            if i == j:
                Q_scores_row += [0]
            else:
                Q_scores_row += [Q(matrix_with_RS[i, j], r, matrix_with_RS[i, matrix_with_RS.shape[0]],
                                    matrix_with_RS[j, matrix_with_RS.shape[0]])]
        Q_scores_ += [Q_scores_row]
    Q_scores_matrix = numpy.array(Q_scores_)
    return Q_scores_matrix


def d(ab, ac, bc):
    return (ac + bc - ab) / 2


def cluster(matrix, ic, jc):
    new_matrix = numpy.delete(matrix, [ic, jc], axis=1)
    new_col = [str(matrix[ic, 0] + matrix[jc, 0])]
    for t in range(1, new_matrix.shape[1]):
        new_col += [d(float(matrix[ic, jc]), float(new_matrix[ic, t]), float(new_matrix[jc, t]))]
    new_matrix = numpy.delete(new_matrix, [ic, jc], axis=0)
    new_matrix = numpy.row_stack((new_matrix, new_col))
    new_col += [0]
    new_matrix = numpy.column_stack((new_matrix, new_col))
    return new_matrix


def al(matrix):
    r = matrix.shape[0] - 1
    if r == 1:
        return  # Finished

    the_row_sums = row_sums(matrix)
    matrix_with_RS = numpy.append(matrix, the_row_sums, axis=1)
    print("Distances and Row Sums: ")
    print(matrix_with_RS)
    print("\n")

    Q_scores_matrix = Q_scores_axis(matrix, matrix_with_RS, r)
    print("Q Scores: ")
    print(Q_scores_matrix)
    print("\n")

    Q_scores_only = Q_scores_sans_axis(matrix_with_RS, r)

    min_q = numpy.amin(Q_scores_only)
    solutions = numpy.argwhere(Q_scores_only == min_q)
    ic = solutions[0, 0] + 1
    jc = solutions[0, 1] + 1

    new_matrix = cluster(matrix, ic, jc)

    al(new_matrix)


def NJ(textfile):
    contents = open(textfile).read()
    LoL = [item.split() for item in contents.split('\n')]
    matrix = numpy.array(LoL)

    al(matrix)

