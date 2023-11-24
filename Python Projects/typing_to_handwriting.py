import pywhatkit as pw

txt = """Python is a programming language that lets you work quickly and integrate systems more effectively.
Python's convenience has made it the most popular language for machine learning and artificial intelligence. Python's flexibility has allowed Anyscale to make ML/AI scalable from laptops to clusters."""

pw.text_to_handwriting(txt, "demo1.png", [0, 0, 138])
print(" END ")
