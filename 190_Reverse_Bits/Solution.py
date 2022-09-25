class Solution:
    def reverseBits(self, n: int) -> int:
        one = 0x00000001
        reverse_number = 0
        for _ in range(32):
            reverse_number = reverse_number << 1 | (n & one)
            n = n >> 1
        return reverse_number