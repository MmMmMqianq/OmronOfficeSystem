import binascii


s = "abc"
b_s1 = b"abc"
b_s2 = b"\x61\x62\x63"  # b_s1和b_s2两个是完全等价的，print的结果完全一样

# string转bytes
b = s.encode(encoding="utf-8")
print("b = ", b, type(b))

# bytes转string
s2 = b.decode(encoding="utf-8")
print("s2 = ", s2, type(s2))

# string编码后的bytes转由十六进制表示的string
s1 = b.hex()
print("s1 = ", s1, type(s1))

# 由每两个十六进制数码为一组构成的字符串转为编码后的bytes
b1 = bytes.fromhex(s1)
print("b1 = ", b1, type(b1))

# string编码后的bytes转16进制的bytes
b_16 = binascii.b2a_hex(b)
print("b_16 = ", b_16, type(b_16))

# 16进制的bytes转string编码后的bytes
b_s3 = binascii.a2b_hex(b_16)
print("b_s3 = ", b_s3, type(b_s3))

# 将string编码后的bytes转换为string
s1 = b_s3.decode(encoding="utf-8")
print("s1 = ", s1, type(s1))
