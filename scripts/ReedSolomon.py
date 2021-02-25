#!/usr/bin/python3
import numpy as np
import math


def recover(parity_matrix=[], encoding_matrix=[], corrupted_string="", corrupted_char="_", shards=4, max_shards=3):
    encoding_matrix_np = np.array(encoding_matrix).reshape(max_shards, shards)

    parity_matrix_np = np.array(parity_matrix).reshape(
        max_shards + shards, shards)

    print("Parity Matrix (P):\n", parity_matrix_np)

    string_matrix = np.array([0 if ord(c) == ord(corrupted_char) else ord(c) for c in corrupted_string]) \
        .reshape(shards, shards)
    
    print("Corrupted String Matrix, 0 is corrupted (S):\n", string_matrix)

    missing_shards = set()
    for idxx, val in np.ndenumerate(string_matrix):
        if val == 0:
            missing_shards.add(idxx[0])

    missing_shards = list(missing_shards)

    missing_shards_parity_matrix_np = np.delete(
        parity_matrix_np, missing_shards, 0)

    print("Parity matrix without missing shards (Ps):\n", missing_shards_parity_matrix_np)

    identity_matrix = np.delete(np.identity(shards), missing_shards, 0)

    encoding_matrix_np = np.vstack((identity_matrix, encoding_matrix_np))

    print("Encoding matrix without missing shards (Es):\n", encoding_matrix_np)

    recovered_matrix = np.linalg.inv(encoding_matrix_np).dot(
        missing_shards_parity_matrix_np)

    print("Recovered Matrix (Es^-1 * Ps):\n", recovered_matrix)

    recovered_string = [chr(round(ascii))
                        for ascii in recovered_matrix.flatten()]
    # [print(ascii, round(ascii)) for ascii in recovered_matrix.flatten()]

    print("Recovered string:\n", "".join(recovered_string))


recover(
    [69, 115, 112, 101, 114, 97, 109, 111, 115, 32, 112, 117, 98, 108, 105, 99,
        2639/4, 763, 792, 3009/4, 1011/2, 559, 599, 1139/2, 967/20, 148/5, 49, 981/20],
    encoding_matrix=[3, 2, 1/4, 2, 2, 1, 1/2, 2, 0, 0, 1/4, 1/5],
    corrupted_string="Es_era_os _ublic",
    corrupted_char="_",
    shards=4,
    max_shards=3
)
