import qrcode as qr

img = qr.make("https://www.youtube.com/channel/UCPG0Sbj8likHvfSQc9ttNGQ/playlists")
img.save("channels4_profile.jpg")