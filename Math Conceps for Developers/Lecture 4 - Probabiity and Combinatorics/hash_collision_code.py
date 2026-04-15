import hashlib
import os

def truncated_has(data: bytes, bits: int, algo: str = "sha256") -> bytes:

    # Returns the first "bits" of the digest as bytes ( rounded up to whole bytes )

    if bits <= 0:
        raise ValueError("bits must be a positive integer")

    h = hashlib.new(algo)
    h.update(data)
    digest = h.digest()

    nbytes = (bits + 7) // 8
    out = bytearray(digest[:nbytes])

    # If bits isn't a multiple of 8, mask the last byte to keep only needed bits.

    r = bits % 8
    if r != 0:
        mask = 0xFF & (0xFF << (8 - r))
        out[-1] &= mask

    return bytes(out)

def find_truncated_collision(bits: int = 24, algo: str = "sha256", max_tries: int = 5_000_000):

    # Finds two different inputs that collide on the first "bits" of "algo" digest.
    # Returns (msg1, msg2, truncated_diegest, tries)

    seen = {}

    for i in range(1, max_tries + 1 ):
        msg = os.urandom(16) # random 16 bytes message
        d = truncated_has(msg, bits, algo)

        if d in seen and seen[d] != msg:
            return seen[d], msg, d, i

        seen[d] = msg

        raise RuntimeError(f"No collision found in {max_tries} tries. Increase max_tries or reduce bits")

    # Example usage
if __name__ == "__main__":
        m1, m2, d, tries = find_truncated_collision(bits=24, algo="sha256")
        print("Found collision!")
        print("tries:", tries)
        print("digest prefix:", d.hex())
        print("m1:", m1.hex())
        print("m2:", m2.hex())
