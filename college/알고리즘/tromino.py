def fillCenterExcept(board,mrow,mcol,part):
    global tromino_count
    tromino_count += 1
    if part != 1:
        board[mrow-1][mcol-1] = tromino_count
    if part != 2:
        board[mrow-1][mcol] = tromino_count
    if part != 3:
        board[mrow][mcol-1] = tromino_count
    if part != 4:
        board[mrow][mcol] = tromino_count





def tromino(board, srow, scol, size, xrow, xcol):
    if size == 1:
        return
    else:
        mrow = srow + size // 2
        mcol = scol + size // 2
        xrow1, xcol1 = mrow -1 , mcol -1 
        xrow2, xcol2 = mrow -1 , mcol
        xrow3, xcol3 = mrow , mcol -1 
        xrow4, xcol4 = mrow, mcol

        if xrow < mrow and xcol <mcol:
            fillCenterExcept(board,mrow,mcol,1)
            xrow1, xcol1 = xrow, xcol
        elif xrow < mrow and xcol >= mcol:
            fillCenterExcept(board,mrow,mcol,2)
            xrow2, xcol3 = xrow, xcol
        elif xrow >= mrow and xcol <mcol:
            fillCenterExcept(board,mrow,mcol,3)
            xrow3, xcol3 = xrow, xcol
        elif xrow >= mrow and xcol >=mcol:
            fillCenterExcept(board,mrow,mcol,4)
            xrow4, xcol4 = xrow, xcol
        tromino(board, srow, scol, size//2, xrow1, xcol1)
        tromino(board, srow, mcol, size//2, xrow2, xcol2)
        tromino(board, mrow, scol, size//2, xrow3, xcol3)
        tromino(board, mrow, mcol, size//2, xrow4, xcol4)

