sample_dict = {"a": "apple", "b": "ball"}
sample_dict.update({"b": "boy", "c": "cat"})
print(sample_dict["a"], sample_dict.get("b"), sample_dict.get("c"))
