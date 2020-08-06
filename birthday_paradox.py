import random
import hashlib

def our_hash_function(random_key):
    return int(hashlib.sha256(f"{random_key}".encode()).hexdigest(), 16)

def how_many_before_collision(length_of_list):
    all_indices = set()
    collision = False

    indices_made = 0

    while not collision:
        random_key = random.random()

        hashed_key = our_hash_function(random_key)

        new_index = hashed_key % length_of_list

        if new_index in all_indices:
            collision = True

        all_indices.add(new_index)
        indices_made += 1

    print(f"hashes before collition, {indices_made}, buckets: {length_of_list}, load factor: {indices_made/length_of_list*100}")

how_many_before_collision(4096)
        