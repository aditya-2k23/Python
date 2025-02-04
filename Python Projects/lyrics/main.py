import time

def print_lirik():
    lirik = [
        ("Your morning eyes, I could stare like watching stars", 18.87, 0.04),
        ("I could walk you by, and I'll tell without a thought", 26.05, 0.05),
        ("You'd be mine", 32.60, 0.03),
        ("Would you mind if I took your hand tonight", 34.66, 0.03),
        ("Know you're all that I want - this life", 40.12, 0.06),
        ("I'll imagine we fell in love", 47.86, 0.04),
        ("I'll nap under moonlight skies with you", 50.51, 0.035),
        ("I think I'll picture us, you with the waves", 54.53, 0.045),
        ("The ocean's colors on your face", 58.14, 0.05),
        ("I'll leave my heart with your air", 62.02, 0.04),
        ("So let me fly with you", 65.95, 0.03),
        ("Will you be forever with me?", 69.29, 0.05),
        ("", 75.69, 0.0),
        ("My love will always stay by you", 106.56, 0.035),
        ("I'll keep it safe, so don't you worry a thing", 112.46, 0.04),
        ("I'll tell you I love you more", 117.73, 0.03),
        ("It's stuck with you forever, so promise you won't let it go", 121.05, 0.045),
        ("I'll trust the universe will always bring me to you", 127.90, 0.05),
        ("I'll imagine we fell in love", 136.40, 0.035),
        ("I'll nap under moonlight skies with you", 139.00, 0.03),
        ("I think I'll picture us, you with the waves", 142.90, 0.045),
        ("The ocean's colors on your face", 146.53, 0.05),
        ("I'll leave my heart with your air", 150.07, 0.04),
        ("So let me fly with you", 154.47, 0.03),
        ("Will you be forever with me?", 157.88, 0.05),
    ]

    for teks, delay_baris, delay_huruf in lirik:
        for c in teks:
            print(c, end='', flush=True)
            time.sleep(delay_huruf)
        print()
        time.sleep(delay_baris)

if __name__ == "__main__":
    print_lirik()
