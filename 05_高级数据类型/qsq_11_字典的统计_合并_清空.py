xiaoming_dict = {"name": "xiaoming",
            "age": 18,
            "height": 1.85,
            "weight": 75.5}

# 1. 统计字典键值对的数量
len(xiaoming_dict)

# 2. 合并字典
tem_dict = {"gender": True,
            "age": 20}
xiaoming_dict.update(tem_dict)
print(xiaoming_dict)  # 如果被合并的字典中包含已经存在的键值对，会覆盖原有的键值对

# 3. 清空字典
xiaoming_dict.clear()
print(xiaoming_dict)