from PIL import Image, ExifTags
import sys
import subprocess
import os


def convert_to_degress(value):
    """Helper function to convert the GPS coordinates
    stored in the EXIF to degress in float format"""
    d0 = value[0][0]
    d1 = value[0][1]
    d = float(d0) / float(d1)
    m0 = value[1][0]
    m1 = value[1][1]
    m = float(m0) / float(m1)

    s0 = value[2][0]
    s1 = value[2][1]
    s = float(s0) / float(s1)

    return d + (m / 60.0) + (s / 3600.0)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Pass file with image as a parameter")
    else:
        img = Image.open(sys.argv[1])
        # print(ExifTags.GPSTAGS) # exif tags docs
        exif_data = img._getexif()
        if exif_data != None:
            exif_data = list(exif_data.items())[0][1]
            latitude = convert_to_degress(exif_data[2])
            longitude = convert_to_degress(exif_data[4])

            with open(".coords.txt", "w") as out_f:
                out_f.write(f"{latitude};{longitude}")

            cmd = ["./hw16.py", ".coords.txt"]
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
            process.wait()
            for line in process.stdout:
                print(line.decode(), end="")

            os.remove(".coords.txt")
        else:
            print("Image has no geotags")