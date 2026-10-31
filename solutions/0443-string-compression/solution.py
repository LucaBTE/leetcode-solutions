class Solution:
    def compress(self, chars: list[str]) -> int:
        read = 0
        write = 0

        while read < len(chars):
            current = chars[read]
            count = 0

            while read < len(chars) and chars[read] == current:
                count += 1
                read += 1

            chars[write] = current
            write += 1


            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write
