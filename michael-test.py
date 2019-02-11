#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import chess
import chess.engine

engine = chess.engine.SimpleEngine.popen_uci("stockfish")

board = chess.Board()
while not board.is_game_over():
    result = engine.play(board, chess.engine.Limit(time=0.100))
    board.push(result.move)
    print("===============")
    print(result.move)
    print(board)

engine.quit()

