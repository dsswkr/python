# CRC32 체크썸 구하기 
import zlib

s = b'abcd'
crc1 = zlib.crc32(s)
crc2 = zlib.adler32(s)

print("crc32 checksum = " + str(crc1))    # CRC32 체크썸
print("adler32 checksum = " + str(crc2))  # ADLER32 체크썸

# 결과
# crc32 checksum = 3984772369
# adler32 checksum = 64487819
