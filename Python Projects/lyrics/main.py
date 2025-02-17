import time

def print_lirik():
    lirik = [
        ("Your morning eyes, I could stare like watching stars", 1, 0.08),
        ("I could walk you by, and I'll tell without a thought", 1.5, 0.05),
        ("You'd be mine, would you mind if I took your hand tonight?", 0.6, 0.03),
        ("Know you're all that I want this life", 0.4, 0.06),
        ("", 0.3, 0.0),
        ("", 0.5, 0.07),
        ("I'll imagine we fell in love", 0.7, 0.04),
        ("I'll nap under moonlight skies with you", 0.6, 0.035),
        ("I think I'll picture us, you with the waves", 0.5, 0.045),
        ("The ocean's colors on your face", 0.4, 0.05),
        ("I'll leave my heart with your air", 0.5, 0.04),
        ("So let me fly with you", 0.6, 0.03),
        ("Will you be forever with me?", 0.7, 0.05),
        ("", 0.3, 0.0),
        ("", 0.5, 0.06),
        ("My love will always stay by you", 0.7, 0.035),
        ("I'll keep it safe, so don't you worry a thing", 0.5, 0.04),
        ("I'll tell you I love you more", 0.6, 0.03),
        ("It's stuck with you forever, so promise you won't let it go", 0.5, 0.045),
        ("I'll trust the universe will always bring me to you", 0.7, 0.05),
        ("", 0.3, 0.0),
        ("", 0.5, 0.04),
        ("I'll imagine we fell in love", 0.7, 0.035),
        ("I'll nap under moonlight skies with you", 0.6, 0.03),
        ("I think I'll picture us, you with the waves", 0.5, 0.045),
        ("The ocean's colors on your face", 0.4, 0.05),
        ("I'll leave my heart with your air", 0.5, 0.04),
        ("So let me fly with you", 0.6, 0.03),
        ("Will you be forever with me?", 0.7, 0.05),
    ]

    for teks, delay_baris, delay_huruf in lirik:
        for c in teks:
            print(c, end='', flush=True)
            time.sleep(delay_huruf)
        print()
        time.sleep(delay_baris)

if __name__ == "__main__":
    print_lirik()
